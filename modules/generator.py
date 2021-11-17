# Llamo al modulo de la clase y sus atributos, e importo el modulo para randomizar los caracteres de la clase
from modules.char_generator import CharGenerator
import random

# Declaro la clase dentro de una variable
gen = CharGenerator()

# Funcion que va a generar Usuario-mail-Contraseña 
def generate_all():

    # Generamos un bloque try-except para que solo sean valores enteros los que tenga que poner el usuario y poder seguir
    try:
        length_us = int(input("\nIngrese el largo del usuario: "))
        if length_us >= 10:
            temp_us = random.sample(gen.letters(), length_us)
        
        else:
            print("***ERROR***")
            print("---El minimo para el usuario es 10---")
            print("***ERROR***")
            return generate_all()

        length_pw = int(input("\nIngrese el largo de la contraseña: "))
        if length_pw >= 20:
            temp_pw  = random.sample(gen.all_characters(), length_pw)

        else:
            print("***ERROR***")
            print("---El minimo para la contraseña es 20---")
            print("***ERROR***")
            return generate_all()

        temp_email = random.choice(gen.email())
        
    except:
        print("***ERROR***")
        print("¡¡¡SOLO NUMEROS ENTEROS!!!")
        print("***ERROR***")
        return generate_all()

    # Guardamos los datos en una cadena string
    user = "".join(temp_us)
    password = "".join(temp_pw)
    email = "".join(temp_email)

    # Mostramos los datos generados
    print(f"El usuario es: {user}{email}, y la contraseña es: {password}")

# Funcion que solo genera usuario
def generate_user():

    # Generamos un bloque try-except para que solo sean valores enteros los que tenga que poner el usuario y poder seguir
    try:
        length_us = int(input("\nIngrese el largo del usuario: "))
        if length_us >= 10:
            temp_us = random.sample(gen.letters(), length_us)
        
        else:
            print("***ERROR***")
            print("---El minimo para el usuario es 10---")
            print("***ERROR***")
            return generate_user()
        
    except:
        print("***ERROR***")
        print("¡¡¡SOLO NUMEROS ENTEROS!!!")
        print("***ERROR***")
        return generate_user()

    # Guardamos los datos en una cadena string
    user = "".join(temp_us)

    # Mostramos los datos generados
    print(f"El usuario es: {user}")

# Funcion que solo genera contraseña
def generate_password():
    
    # Generamos un bloque try-except para que solo sean valores enteros los que tenga que poner el usuario y poder seguir
    try:
        length_pw = int(input("\nIngrese el largo de la contraseña: "))
        if length_pw >= 20:
            temp_pw  = random.sample(gen.all_characters(), length_pw)

        else:
            print("***ERROR***")
            print("---El minimo para la contraseña es 20---")
            print("***ERROR***")
            return generate_password()

    except:
        print("***ERROR***")
        print("¡¡¡SOLO NUMEROS ENTEROS!!!")
        print("***ERROR***")
        return generate_password()

    # Guardamos los datos en una cadena string
    password = "".join(temp_pw)
    
    # Mostramos los datos generados
    print(f"La contraseña generada es: {password}")