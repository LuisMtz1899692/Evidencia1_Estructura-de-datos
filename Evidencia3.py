import sys
import os
import sqlite3
from sqlite3 import Error
import datetime

venta=True
Ag_Produ=True
ciclo=True
folio_venta=True
try:
    with sqlite3.connect("VentasCosmeticos.db")as conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS folio_venta(Folio INTEGER PRIMARY KEY,Fecha TEXTO NOT NULL);")
        c.execute("CREATE TABLE IF NOT EXISTS Ventas(Producto TEXT NOT NULL, Cantidad INTEGER NOT NULL, Precio REAL NOT NULL, Total_sin_IVA REAL NOT NULL, IVA REAL NOT NULL, Total_con_IVA REAL NOT NULL,Folioventa INTEGER NOT NULL,FOREIGN KEY(Folioventa) REFERENCES Folioventa(Folio));")
        print("La tabla se creo exitosamente")
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
            while True:
                folio = int(input('Folio de la nueva venta: '))
                with sqlite3.connect("VentasCosmeticos.db") as conn:
                    c = conn.cursor()
                    val_folio = {"folio": folio}
                    c.execute("SELECT * FROM folio_venta WHERE Folio = :folio", val_folio)
                    fetfol = c.fetchall()
                    if fetfol:
                        print("El folio ya existe. Ingrese uno nuevamente")
                    else:
                        break  
            while folio_venta:
                fecha = datetime.date.today()
                print(fecha)
                c.execute("INSERT INTO folio_venta(Folio,Fecha)VALUES(?,?)",(folio,fecha))
                print("Folio agregado exitosamente")
                conn.commit()
                while Ag_Produ:
                    producto = input("Producto: ")
                    precio = float(input("Precio: "))
                    cantidad = int(input("Cantidad: "))
                    total=precio * cantidad
                    iva = precio * 0.16
                    total_iva = (total)+(iva)
                    c.execute("INSERT INTO Ventas(Producto,Cantidad,Precio,Total_sin_IVA,IVA,Total_con_IVA,Folioventa)VALUES(?,?,?,?,?,?,?)", (producto,cantidad,precio,total,iva,total_iva,folio))
                    print("La Venta Se Agrego a la BD")
                    conn.commit()
                    eleccion = input("Desea Agregar un nuevo producto[S/N]: ")
                    print()
                    if eleccion == "S":
                        print("Agregue El Siguiente Producto")
                        pass
                    elif eleccion == "N":
                        print("Usted esta saliendo del menu registro")
                        print(f"El Total a pagar es de: ${total}")
                        print(f"IVA ${iva}")
                        print(f"El total con iva es de ${total_iva}")
                        Ag_Produ=False
                        folio_venta=False
                    else:
                        print("La Opcion ingresada no existe intente de nuevo")

        elif opcion =="2":
            folio_clave = int(input("Ingrese el Folio a consultar:"))
            print("Las Ventas Registradas con ese folio son...")
            valores={"folio":folio_clave}
            c.execute('''SELECT folio_venta.Folio,folio_venta.Fecha,Ventas.Producto,Ventas.Cantidad,Ventas.Precio,Ventas.Total_sin_IVA,Ventas.IVA,Ventas.Total_con_IVA,Ventas.Folioventa 
                FROM folio_venta 
                INNER JOIN Ventas ON Ventas.Folioventa = folio_venta.Folio WHERE Folio = :folio''',valores)
            registro= c.fetchall()
            if registro:
                print("Folio\t\tFecha\t\tProducto\t\tCantidad\t\tPrecio\t\tTotal_sin_IVA\t\tIVA\t\tTotal_con_IVA\t\tFolioventa")
                for Folio,Fecha,Producto,Cantidad,Precio,Total_sin_IVA,iva,Total_con_IVA,Folioventa in registro:
                    print(f"{Folio}\t\t{Fecha}\t{Producto}\t\t{Cantidad}\t\t{Precio}\t{Total_sin_IVA}\t\t{iva}\t{Total_con_IVA}\t\t{Folioventa}")
            else:
                print(f"No Se encontro un proyecto asociado con la clave {folio_clave}")
        elif opcion =="3":
            fecha_capturada = input("Ingrese La Fecha (dd-mm-aaaa): \n")
            fecha_procesada = datetime.datetime.strptime(fecha_capturada, "%d-%m-%Y").date()
            print("Las Ventas Registradas con esa fecha...")

            valores={"folio":fecha_procesada}
            c.execute('''SELECT folio_venta.Folio,folio_venta.Fecha,Ventas.Producto,Ventas.Cantidad,Ventas.Precio,Ventas.Total_sin_IVA,Ventas.IVA,Ventas.Total_con_IVA,Ventas.Folioventa 
                FROM folio_venta 
                INNER JOIN Ventas ON Ventas.Folioventa = folio_venta.Folio WHERE Fecha = :folio''',valores)
            registro= c.fetchall()
            if registro:
                print("Folio\t\tFecha\t\tProducto\t\tCantidad\t\tPrecio\t\tTotal_sin_IVA\t\tIVA\t\tTotal_con_IVA\t\tFolioventa")
                for Folio,Fecha,Producto,Cantidad,Precio,Total_sin_IVA,iva,Total_con_IVA,Folioventa in registro:
                    print(f"{Folio}\t\t{Fecha}\t{Producto}\t\t{Cantidad}\t\t{Precio}\t{Total_sin_IVA}\t\t{iva}\t{Total_con_IVA}\t\t{Folioventa}")
            else:
                print(f"No Se encontro la fecha : {fecha_capturada} en el registro")

        elif opcion == "4":
            print("Usted esta saliendo del programa")
            ciclo=False
        else:
            print("La opcion Ingresada No es Valida")
            print("Porfavor Intente de Nuevo....")
except Error as e:
    print(e)
except Exception:
    print(f"Se Podujo el siguente error: {sys.exc_info()[0]}")
finally:
    if conn:
        conn.close()