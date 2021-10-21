import pandas as pd
from collections import namedtuple
from datetime import datetime

diccionario = dict()
lista_de_listas = list()
Ag_Produ=True
ciclo=True

while ciclo:
    print("******Menu********")
    print("[1] Registrar una venta")
    print("[2] Consultar una venta")
    print("[3] Obtener Reportes de ventas")
    print("[4] Salir")
    print("******************")
    opcion = input("Elige una opcion :")
    print()

    if opcion == "1":
        folio = input("Folio de la nueva venta: ")
        if not folio in diccionario.keys():
            while Ag_Produ:
                ventas = namedtuple("ventas", ("fecha","producto","cantidad", "precio", "iva", "total"))
                fecha = datetime.now()
                print(fecha)
                producto = input("Producto: ")
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                iva = precio + (precio * 0.16)
                total = iva * cantidad
                eleccion = input("Desea Agregar un nuevo producto[S/N]: ")
                print()
                venta_registrada = ventas(fecha, producto, cantidad, precio, iva, total)
                lista_de_listas.append(venta_registrada)
                if eleccion == "S":
                    print("Agregue El Siguiente Producto")
                    pass
                elif eleccion == "N":
                    print("Usted esta saliendo del menu registro")
                    Ag_Produ=False
                else:
                    print("La Opcion ingresada no existe intente de nuevo")
        else:
            print("La Clave ingresada ya existe")
            print("Porfavor intente de nuevo...")
        diccionario[folio] = lista_de_listas
        lista_de_listas = list()

    elif opcion == "2":
        consulta = input("Ingrese el Folio a consultar: ")
        campos = ("fecha","producto","cantidad", "precio", "iva", "total")
        nombres = list()
        for x in diccionario.keys():
            if consulta == x:
                """print(f"La Fecha registrada para esa venta es: {diccionario[consulta]}")"""
                for tupla in diccionario.values():
                    for dato in tupla:
                        print(dato)
    elif opcion == "3":
        print("El Siguiente menu creara un reporte")
        
    elif opcion == "4":
        print("Usted esta saliendo del programa")
        ciclo=False
    else:
        print("La opcion Ingresada No es Valida")
        print("Porfavor Intente de Nuevo....")