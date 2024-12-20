import transform


# Docstring del módulo
"""
Este módulo proporciona una interfaz para que el usuario introduzca una cadena 
y seleccione una transformación para convertirla a mayúsculas, minúsculas o capitalizarla.
Utiliza funciones del módulo 'transform' para realizar las transformaciones.
"""

def main():
    """Función principal que gestiona la entrada del usuario y realiza 
    las transformaciones de texto según la opción seleccionada.
    """
    string = input("Introdueix un string: ")

    print("Quina transformació vols?")
    print("[1] Text amb tot majúscules")
    print("[2] Text amb tot minúscuies")
    print("[3] Text capitalitzat ")

    opcio = input("opció escollida: ")

    if opcio == "1":
        print(transform.to_upper_case(string))
    elif opcio == "2":
        print(transform.to_lower_case(string))
    elif opcio == "3":
        print(transform.to_capitalize(string))
    else:
        print("opció no reconeguda")


if __name__ == '__main__':
    main()
