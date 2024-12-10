"""
Cree un archivo de texto llamado notas.txt y escriba 3 líneas con contenido.
Lea el archivo y muestre el contenido línea por línea.
Guarde un diccionario con al menos 3 claves en un archivo JSON.
Lea el archivo JSON y muestre el contenido.
Guarde una tabla de datos con al menos 3 filas en un archivo CSV.
Lea el archivo CSV y muestre cada fila.
"""

#Archivo texto
with open("notas.txt", "w") as archivo:
    archivo.write("Hola\n")
    archivo.write("que tal\n")
    archivo.write("Fin\n")
with open("notas.txt", "r") as archivo:
    lectura = archivo.read()
    print(lectura)

#Archivo JSON
import json
dicc = {"edad": 15, "año": 2025, "lugar": "Barna"}
with open("diccionario.json", "w") as archivo:
    json.dump(dicc, archivo)
with open("diccionario.json", "r") as archivo:
    lectura = json.load(archivo)
    print(lectura)

#Archivo CSV
import csv
datos_csv = [["edad", 15], ["año", 2025], ["lugar", "Barna"]]
with open("excel.csv", "w", newline="") as archivo:
    escri = csv.writer(archivo)
    escri.writerows(datos_csv)
with open("excel.csv", "r") as archivo:
    lectura = csv.reader(archivo)
    print ("\nContenido del archivo:")
    for i in lectura:
        print(i)