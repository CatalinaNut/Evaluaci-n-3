import globales
import math
import os
def Producto_valor_más_alto():
    os.system("cls")
    todas_las_ventas = globales.leer_archivo_json('ventas.json')
    ventas_ordenadas = sorted(todas_las_ventas, key=lambda x:x ['total_ventas'], reverse=True)
    print("|Nombre |Valor | Iva")
    for venta in ventas_ordenadas[:3]:
        print(f"{venta['nombre']} \t\t | {venta['total_ventas']}")
        
    input(">> ")


def Producto_valor_IVA_más_bajo():
    os.system("cls")
    todas_las_ventas = globales.leer_archivo_json('ventas.json')
    ventas_ordenadas = sorted(todas_las_ventas, key=lambda x:x ['total_ventas'], reverse=False)
    print("|Nombre |Valor | Iva")
    for venta in ventas_ordenadas[:3]:
        print(f"{venta['nombre']} \t\t | {venta['total_ventas']}")
        
    input(">> ")
    


def Promedio_valor_de_productos():
    os.system("cls")
    todas_las_ventas = globales.leer_archivo_json('ventas.json')
    suma_ventas = 0
    cantidad_ventas = 0
    
    for venta in todas_las_ventas:
        suma_ventas+= venta['total_ventas']
        cantidad_ventas +=1
    
    promedio_ventas = suma_ventas/cantidad_ventas

    input(f"el promedio de ventas es ${int(promedio_ventas)} >>")

def Media_geométrica_valor_productos():
    todas_las_ventas = globales.leer_archivo_json('ventas.json')

    suma_ventas = 0
    cantidad_ventas = 0


    for venta in todas_las_ventas:    
        suma_ventas +=math.log(venta['total_ventas']) 
        cantidad_venta += 1 
        
    media_geometrica = math.exp(suma_ventas/cantidad_ventas)

    input(f"La media geometrica de ventas es ${int(media_geometrica)} >> ")
    
