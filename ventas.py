import os
import random
import globales
import random

def leer_archivo_json(dir):
    try:
        with open(dir, 'r') as archivo: # leemos el archivo
            return json.load(archivo) # retornamos lo que quenga el archivo
    except:
        return []

def guardar_archivo_json(dir, data):
    try:
        with open(dir, 'w') as archivo: # leemos el archivo
            json.dump(data, archivo, indent=4)
    except:
        return []
def crear_venta():
    todas_las_ventas = globales.leer_archivo_json('ventas.json')
    
    for i in range(10):
        nombre = nombre(productos.json)
        ventas=random.choice(todas_las_ventas)
        valor=int.random.randint(2,10)*1000
        iva=valor*19
    nueva_venta = { 
        "nombre": nombre ,
        "valor":valor,
        "iva": iva
}

    todas_las_ventas.append(nueva_venta)
    globales.guardar_archivo_json('ventas.json',todas_las_ventas)

    input("ventas Cargadas")

