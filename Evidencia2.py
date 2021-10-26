import pandas as pd
from collections import namedtuple
import csv
import datetime

columnas_csv =("fecha","producto","cantidad", "precio", "iva", "total")
nombre_archivo = "Reporte_venta"
diccionario = {}
lista_de_listas = []
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
                fecha = datetime.date.today()
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
                    print(f"\nSe agregaron los datos:\n {venta_registrada} con el folio {folio} el dia {fecha}")
                    print("")
                    print("Usted esta saliendo del menu registro")
                    Ag_Produ=False
                else:
                    print("La Opcion ingresada no existe intente de nuevo")
        else:
            print("La Clave ingresada ya existe")
            print("Porfavor intente de nuevo...")
        diccionario[folio] = lista_de_listas

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
        fecha_actual = datetime.date.today()
        fecha_capturada = input("Ingrese La Fecha (dd/mm/aaaa): \n")
        fecha_procesada = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()
        if fecha_procesada == fecha_actual:
            print("Tu registro se generara")
            with open("Reporte_venta.csv","w",newline="") as archivo:
                registrador = csv.writer(archivo)
                registrador.writerow(columnas_csv)
                registrador.writerows(lista_de_listas)
        else:
            print("Tu registro se realizara el dia que indicaste")
    elif opcion == "4":
        print("Usted esta saliendo del programa")
        ciclo=False
    else:
        print("La opcion Ingresada No es Valida")
        print("Porfavor Intente de Nuevo....")