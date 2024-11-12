from insert_vendedor import insertar_vendedor
from insert_venta import insertar_venta
from consult_vendedores import consultar_vendedores
from consult_ventas import consultar_ventas
from consult_mejor_vendedor import consultar_mejor_vendedor

def menu():
    while True:
        print("\nMenú Principal:")
        print("1. Insertar un nuevo vendedor")
        print("2. Insertar una nueva venta")
        print("3. Consultar todos los vendedores")
        print("4. Consultar todas las ventas")
        print("5. Consultar el mejor vendedor del mes")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            insertar_vendedor()
        elif opcion == '2':
            insertar_venta()
        elif opcion == '3':
            consultar_vendedores()
        elif opcion == '4':
            consultar_ventas()
        elif opcion == '5':
            consultar_mejor_vendedor()
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
