# Exportamos el modulo y los atributos que se van a utilizar 
from modules.generator import generate_all, generate_password, generate_user

# ───────────────────────────────────────────────────────────────
# ─██████████████───██████──██████─██████████████─██████████████─
# ─██░░░░░░░░░░██───██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
# ─██░░██████░░██───██░░██──██░░██─██░░██████████─██░░██████████─
# ─██░░██──██░░██───██░░██──██░░██─██░░██─────────██░░██─────────
# ─██░░██████░░████─██░░██──██░░██─██░░██████████─██░░██████████─
# ─██░░░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
# ─██░░████████░░██─██░░██──██░░██─██████████░░██─██████████░░██─
# ─██░░██────██░░██─██░░██──██░░██─────────██░░██─────────██░░██─
# ─██░░████████░░██─██░░██████░░██─██████████░░██─██████████░░██─
# ─██░░░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
# ─████████████████─██████████████─██████████████─██████████████─
# ───────────────────────────────────────────────────────────────

# Declaro una funcion para que consulte si quiere seguir usando las opciones
def seguir_con_programa():

    try:
        print ("/" * 50)
        print("Quiere utilizar una opcion mas? Y(si) // N(no)")
        x = str(input(">"))
        print ("/" * 50)
        if x in ["y", "Y", "Yes", "YES", "yes"]:
            return options()
        elif x in ["n", "N", "No", "NO", "no"]:
            print ("/" * 50)
            print ("Muchas gracias por usar el programa, espero que le haya servido")
            print ("/" * 50)
            exit
    except:
        print ("************ERROR************")
        print ("Solo se admite (Y/y) or (N/n)")
        print ("************ERROR************")

# Funcion para inicializar opciones
def options():
    print("****************************************************")
    print("****************************************************")
    print("** 1 => Generar Usuario (Con correo) y Contraseña **")
    print("** 2 => Generar solo usuario                      **")
    print("** 3 => Generar solo contraseña                   **")
    print("** 0 => Salir                                     **")
    print("****************************************************")
    print("****************************************************")
    print("<<Ingrese la opcion deseada>>")
    op = int(input(">"))
    if op == 1:
        # Se llama a la funcion generate_all del modulo generator
        generate_all()
        # Preguntamos si queremos seguir utilizando el programa
        seguir_con_programa()
    elif op == 2:
        # Se llama a la funcion generate_user del modulo generator
        generate_user()
        seguir_con_programa()
    elif op == 3:
        # Se llama a la funcion generate_password del modulo generator
        generate_password()
        seguir_con_programa()
    elif op == 0:
        print("Gracias por usar el programa :) ")
        exit

# Funcion que inicializa el programa
def main():
    print("/" * 50)
    print("Hola, Bienvenido al generador de Usuario y Contraseña")
    print("/" * 50)
    options()
main()

