import os
import globales 
import ventas
import Estadisticas

os.system("cls")

def menu_estadisticas():
    while True:
        os.system("cls")
        print("==MENU ESTADISTICAS==")
        print("1. Producto con valor más alto.")
        print("2. Producto con valor del IVA más bajo.")
        print("3. Promedio del valor de los productos.")
        print("4. Media geométrica del valor de los productos.")

        opcion = globales.seleccionar_opciones(5)

        if opcion == 1:
            Estadisticas.Producto_valor_más_alto()
        elif opcion == 2:
            Estadisticas.Producto_valor_IVA_más_bajo()
        elif opcion == 3:
            Estadisticas.Promedio_valor_de_productos()
        elif opcion == 4:
            Estadisticas.Media_geométrica_valor_productos
        elif opcion == 5:
            return
def menu_general():
    while True:
        os.system("cls")