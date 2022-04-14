"""
Se requiere de un programa que realice un mantenimiento de inventario,
para una tienda pequeña. 
El mismo consta de ingreso de mercadería, egreso de mercadería,
eliminar mercadería y buscar mercadería.
El programa debe de tener un menú principal de la tienda con dos
opciones la primera denominada inventario y la segunda salir.
Una vez el cliente ingrese a la primera opción se deberá desplegar un
menú con las opciones descritas anteriormente y deberá agregar una
opción de reporte para ver la mercadería en la tienda.
Usted debe de contemplar las variables a almacenar en el inventario.
"""

# Menus
# menu principal
from subprogramas import menu_principal as mp
# menu de inventario
from subprogramas import menu_inventario as mi

productos = {}

while True:
    print()
    mp.menu_principal()

    while True:
        try:
            opc = int(input('Qué desea hacer?: '))
            print()
            break
        except ValueError:
            print('Ingrese una opción válida')

    if opc == 1:
        while True:
            mi.menu_inventario()
            while True:
                try:
                    opc = int(input('Qué desea hacer?: '))
                    print()
                    break
                except ValueError:
                    print('Ingrese una opción válida')

            if opc == 1:
                print('\t\tIngresar datos del producto\n')
                codigo = input('Código: ')
                while True:
                    if codigo in productos.keys():
                        print('Código ya existente!')
                        codigo = input('Código: ')
                    elif codigo not in productos.keys():
                        break
                        
                nombre = input('Nombre: ')
                while True:
                    try:
                        precio = int(input('Precio: '))
                        break
                    except ValueError:
                        print('Ingrese un valor entero')

                while True:
                    try:
                        cantidad = int(input('Cantidad: '))
                        break
                    except ValueError:
                        print('Ingrese un valor entero')
                productos[codigo] = dict(Código = codigo, Nombre = nombre, Precio = precio, Cantidad = cantidad)
                print()

            elif opc == 2:
                print('\t\tProducto a egresar\n')
                codigo = input('Código: ')
                print()
                if codigo in productos.keys():
                    print('Producto encontrado!\n')
                    cantidad = int(input('Cantidad a vender: '))
                    if productos[codigo]['Cantidad'] < cantidad:
                        print('No tienes disponibilidad suficiente del producto!\n')
                    else:
                        productos[codigo]['Cantidad'] -= cantidad
                        print('Operación exitosa\n')
                else:
                    print('Producto no existente\n')

            elif opc == 3:
                print('\t\tProducto a eliminar\n')
                codigo = input('Código: ')
                if codigo in productos.keys():
                    productos.pop(codigo)
                    print('Producto eliminado!\n')
                else:
                    print('Producto no encontrado\n')
            elif opc == 4:
                print('\t\tProducto a buscar\n')
                codigo = input('Código: ')
                if codigo in productos.keys():
                    print()
                    print(productos[codigo])
                    print()
                else:
                    print('Producto no encontrado\n')
            elif opc == 5:
                if len(productos) == 0:
                    print('No hay existencias')
                else:
                    print('\t\tMercadearía en la tienda\n')
                    for i in productos.keys():
                        print(productos[i],end='\n')
                print()
            elif opc == 6:
                break
            else:
                print('Opción fuera de rango\n')

    elif opc == 2:
        break
    else:
        print('Opción fuera rango\n')