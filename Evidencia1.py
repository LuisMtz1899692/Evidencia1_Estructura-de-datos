from collections import namedtuple
from datetime import datetime
datos_registro = {}
salir=True
nuevo_produc= True
ventas= namedtuple("ventas", ("dia_venta","des_prod","Cant_produ", "Precio_product"))

while salir:
    print("******Menu********")
    print("[1] Registrar una venta")
    print("[2] Consultar una venta")
    print("[3] Salir")
    print("******************")
    resp_menu = input("¿Que desea realizar: ")
    
    if resp_menu == "1":
        print("Bienvenido al menu Registrar venta")
        dia_venta= datetime.now()
        print(dia_venta)
        Folio_Vet= input("Ingrese el Folio de la venta: ")
        if not Folio_Vet in datos_registro.keys():
            while nuevo_produc:
                des_prod=input("Ingrese La Descripcion del Producto: ")
                Cant_produ=int(input("Ingrese La Cantidad Del produtos: "))
                Precio_product=int(input("Ingrese el Precio del producto: "))
                venta_registrada = ventas(dia_venta, des_prod, Cant_produ, Precio_product)
                datos_registro[Folio_Vet] = venta_registrada
                res_producto = input("Desea Agregar un nuevo producto[S/N]")
                if res_producto == "S":
                    print("Agregue el siguiente producto: ")
                elif res_producto=="N":
                    nuevo_produc= False
                    print("saliendo del menu registro")
        else:
            print("la clave registrada ya existe, intente de nuevo")
    elif resp_menu == "2":
        print("Bienvenido al menu Consultar venta")
        consulta=input("Ingrese el folio a buscar: ")
        if consulta in datos_registro.keys():
            print(f"Los Fecha registrada para esa venta es: {datos_registro[Folio_Vet].dia_venta}")
            print(f"Los productos Registrados son: {datos_registro[Folio_Vet].des_prod}")
            print(f"La Cantidad de productos es: {datos_registro[Folio_Vet].Cant_produ}")
            print(f"El precio del productos es: {datos_registro[Folio_Vet].Precio_product}")
        else:
            print("El Folio ingrado no se encuentra en el sistema")
            print("Intente de nuevo")
    elif resp_menu == "3":
        print("Usted esta saliendo del programa...")
        salir=False
    else:
        print("La opcion ingresada no esta disponible")
        print("Intente de nuevo")