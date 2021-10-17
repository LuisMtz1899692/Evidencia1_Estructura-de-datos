from collections import namedtuple
from datetime import datetime

diccionario = dict()
lista_de_listas = list()

while True:
    print("******Menu********")
    print("[1] Registrar una venta")
    print("[2] Consultar una venta")
    print("[3] Salir")
    print("******************")
    opcion = input("Elige una opcion :")
    print()

    if opcion == "1":
        folio = input("Folio de la nueva venta: ")
        while True:
            ventas = namedtuple("ventas", ("fecha","producto","cantidad", "precio", "iva", "total"))
            fecha = datetime.now()
            producto = input("Producto: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            iva = precio + (precio * 0.16)
            total = iva * cantidad
            eleccion = input("Desea Agregar un nuevo producto[S/N]")
            print()
            venta_registrada = ventas(fecha, producto, cantidad, precio, iva, total)
            lista_de_listas.append(venta_registrada)
            if eleccion == "S":
                print("Agregue El Siguiente Producto")
                pass
            else:
                break
        diccionario[folio] = lista_de_listas
        lista_de_listas = list()

    if opcion == "2":
        consulta = input("Ingrese el Folio a consultar: ")
        campos = ("fecha","producto","cantidad", "precio", "iva", "total")
        nombres = list()
        for x in diccionario.keys():
            if consulta == x:
                """print(f"La Fecha registrada para esa venta es: {diccionario[consulta]}")"""
                for tupla in diccionario.values():
                    for dato in tupla:
                        print(dato)
    if opcion == "3":
        print("Usted esta saliendo del programa")
        break
    
