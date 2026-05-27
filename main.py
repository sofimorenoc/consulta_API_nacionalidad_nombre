from api_nacionalidad import (
    validar_texto,
    consultar_nacionalidad,
    obtener_pais_mas_probable,
    formatear_probabilidad
)


def mostrar_resultado(nombre, datos):
    """
   Muestra en pantalla los resultados obtenidos de la consulta a la API.
   
   PARAMETERS
       nombre (str): nombre ingresado por el usuario
       datos (dict): diccionario con la información devuelta por la API
   
   RETURNS
       None
   """
    
    print(f"\nNombre consultado: {nombre}")
    print(f"Cantidad de registros: {datos['count']}")

    print("Países probables:")
    for i, pais in enumerate(datos["country"], start=1):
        codigo = pais["country_id"]
        probabilidad = formatear_probabilidad(pais["probability"])
        print(f"{i}. {codigo} - {probabilidad}")

    pais_mas_probable = obtener_pais_mas_probable(datos)
    print(f"País más probable: {pais_mas_probable}")


def main():
    """
   Ejecuta el programa principal del predictor de nacionalidad.
   
   Muestra un menú interactivo que permite:
   - consultar un nombre
   - comparar dos nombres
   - finalizar el programa
   
   También maneja errores de ingreso y de consulta a la API.
   """
    while True:
        print("\n===== Predictor de nacionalidad =====")
        print("1. Consultar un nombre")
        print("2. Comparar 2 nombres")
        print("3. Salir")

        opcion = input("Elegí una opción: ")

        try:
            if opcion == "1":
                nombre = input("Ingresá un nombre: ")
                nombre = validar_texto(nombre)

                datos = consultar_nacionalidad(nombre)
                mostrar_resultado(nombre, datos)

            elif opcion == "2":
                nombre1 = validar_texto(input("Ingresá el primer nombre: "))
                nombre2 = validar_texto(input("Ingresá el segundo nombre: "))

                datos1 = consultar_nacionalidad(nombre1)
                datos2 = consultar_nacionalidad(nombre2)

                pais1 = obtener_pais_mas_probable(datos1)
                pais2 = obtener_pais_mas_probable(datos2)

                print("\nResumen de predicciones:")
                print(f"{nombre1} -> {pais1}")
                print(f"{nombre2} -> {pais2}")

            elif opcion == "3":
                print("Programa finalizado.")
                break

            else:
                print("Opción inválida. Elegí 1, 2 o 3.")

        except ValueError as error:
            print(f"Error: {error}")

        except Exception as error:
            print(f"Ocurrió un error: {error}")


main()


