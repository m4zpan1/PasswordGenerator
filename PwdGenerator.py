import random
import string
import os
import time

def evaluar_seguridad(password):
    longitud = len(password)
    tipos = {
        'mayus': any(c.isupper() for c in password),
        'minus': any(c.islower() for c in password),
        'digito': any(c.isdigit() for c in password),
        'signo': any(c in string.punctuation for c in password),
    }
    puntaje = sum(tipos.values())

    if longitud < 8:
        return "Muy poco segura"
    elif longitud < 12 and puntaje < 3:
        return "Poco segura"
    elif longitud < 15 and puntaje < 4:
        return "Moderadamente segura"
    elif longitud >= 15 and puntaje == 4:
        return "Muy segura"
    else:
        return "Segura"

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def generar_contraseña():
    ascii_art_title = """
\033[1;31m┏━━━┳┓┏┓┏┳━━━┳━━━┓╋╋╋╋╋╋╋╋╋╋╋╋╋┏┓
┃┏━┓┃┃┃┃┃┣┓┏┓┃┏━┓┃╋╋╋╋╋╋╋╋╋╋╋╋┏┛┗┓
┃┗━┛┃┃┃┃┃┃┃┃┃┃┃╋┗╋━━┳━┓┏━━┳━┳━┻┓┏╋━━┳━┓
┃┏━━┫┗┛┗┛┃┃┃┃┃┃┏━┫┃━┫┏┓┫┃━┫┏┫┏┓┃┃┃┏┓┃┏┛
┃┃╋╋┗┓┏┓┏╋┛┗┛┃┗┻━┃┃━┫┃┃┃┃━┫┃┃┏┓┃┗┫┗┛┃┃
┗┛╋╋╋┗┛┗┛┗━━━┻━━━┻━━┻┛┗┻━━┻┛┗┛┗┻━┻━━┻┛\033[0m
"""
    print(ascii_art_title)

    while True:
        try:
            longitud = int(input("Ingresa la longitud deseada para tu contraseña entre 8 y 50 caracteres: "))
            if 8 <= longitud <= 50:
                break
            else:
                print("Por favor, ingresa un número entre 8 y 50.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

    caracteres_elegidos = []

    def get_yes_no_input(prompt):
        rojo = "\033[1;31m"
        reset = "\033[0m"
        while True:
            response = input(f"{rojo}{prompt}{reset}").lower()
            if response in ['si', 'no']:
                return response
            else:
                print(f"{rojo}Respuesta inválida. Por favor, ingresa '{rojo}si{reset}' o '{rojo}no{reset}'.{reset}")

    if get_yes_no_input("¿Incluir letras MAYÚSCULAS 𝗔𝗕𝗖? si o no: ") == 'si':
        caracteres_elegidos.append(string.ascii_uppercase)
    if get_yes_no_input("¿Incluir letras minúsculas 𝗮𝗯𝗰? si o no: ") == 'si':
        caracteres_elegidos.append(string.ascii_lowercase)
    if get_yes_no_input("¿Incluir NÚMEROS 𝟭𝟮𝟯? si o no: ") == 'si':
        caracteres_elegidos.append(string.digits)
    if get_yes_no_input("¿Incluir SÍMBOLOS #$&? si o no: ") == 'si':
        caracteres_elegidos.append(string.punctuation)

    if not caracteres_elegidos:
        print("¡Atención! Debes seleccionar al menos un tipo de carácter para generar la contraseña.")
        time.sleep(2)
        clear_console()
        print(ascii_art_title)
        return

    caracteres_totales = "".join(caracteres_elegidos)
    password_list = []

    for char_set in caracteres_elegidos:
        password_list.append(random.choice(char_set))

    for _ in range(longitud - len(password_list)):
        password_list.append(random.choice(caracteres_totales))

    random.shuffle(password_list)
    contraseña = "".join(password_list)
    seguridad = evaluar_seguridad(contraseña)

    clear_console()
    print(ascii_art_title)
    rojo = "\033[1;31m"
    reset = "\033[0m"
    print(f"\nTu contraseña generada es: \n👉  {rojo}{contraseña}{reset}  ")
    print(f"Nivel de seguridad:   {rojo}{seguridad}{reset}  ")

generar_contraseña()