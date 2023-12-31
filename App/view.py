﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control=controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    temblores=controller.load_data(control)
    return temblores 


def print_data(lista,tamano):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    columna=[["code","time","lat","long","mag","sig","nst","gap","title","depth","felt","cdi","mmi","tsunami"]]
    for i in range(1,6):
        temblor=lt.getElement(lista,i)
        fila=[str(temblor["code"]),temblor["time"],str(temblor["lat"]),str(temblor["long"]),str(temblor["mag"]),temblor["sig"], str(temblor["nst"]), temblor["gap"], temblor["title"], temblor["depth"], str(temblor["felt"]), temblor["cdi"], temblor["mmi"], temblor["tsunami"]]
        for j in range(len(fila)):
            if fila[j]=="":
                fila[j]="Unknown"
        serie= pd.Series(fila).str.wrap(15)
        columna.append(serie)
    for i in range(tamano-4,tamano+1):
        temblor=lt.getElement(lista,i)
        fila=[str(temblor["code"]),temblor["time"],str(temblor["lat"]),str(temblor["long"]),str(temblor["mag"]),temblor["sig"], str(temblor["nst"]), temblor["gap"], temblor["title"], temblor["depth"], str(temblor["felt"]), temblor["cdi"], temblor["mmi"], temblor["tsunami"]]
        for j in range(len(fila)):
            if fila[j]=="":
                fila[j]="Unknown"
        serie= pd.Series(fila).str.wrap(15)
        columna.append(serie)
    print(tabulate(columna,tablefmt="grid"))

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    final = lt.newList("ARRAY_LIST")
    fecha_ini = input("Ingrese la fecha donde quiere inciar la busqueda: \n")
    fecha_fin = input("Ingrede la fecha donde quiere finalizar la busqueda: \n")
    size, data, time = controller.req_1(control, fecha_ini, fecha_fin)
    columna=[["code","time","lat","long","mag","sig","nst","gap","title","depth","felt","cdi","mmi","tsunami"]]
    if size>6:
        for i in range(0,6):
            if i<3:
                lt.addLast(final, data["elements"][i])
            else: 
                x = i-3
                lt.addLast(final,data["elements"][x])
    else:
        final = data
        
    for x in final["elements"]:
        registro = []
        for v in x["value"].values():
            v = str(v)
            if v == "":
                v = "Unknown"
            registro.append(v)    
        serie = pd.Series(registro).str.wrap(15)
        columna.append(serie)
        
        
    print("="*34)
    print(f"la fución se demoro: {time}")
    print("La cantidadd de terremotos encontrados es: " + str(size))
    print(tabulate(columna, tablefmt="grid"))
        
        
    


def print_req_2(temblores):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
   
    columna_2=[["mag","events","details"]]

    if lt.size(temblores)<=6:
        for i  in range(lt.size(temblores),0,-1):
            magnitud=lt.getElement(temblores,i)
            columna=[["time","lat","long","depth","sig","gap","nst","title","cdi","mmi","magType","type","code"]]
            if lt.size(magnitud)<=6:
                for temblor in lt.iterator(magnitud):
                    mag=temblor["mag"]
                    fila=[str(temblor["time"]),temblor["lat"],str(temblor["long"]),str(temblor["depth"]),str(temblor["sig"]),temblor["gap"], str(temblor["nst"]), temblor["title"], temblor["cdi"], temblor["mmi"], str(temblor["magType"]), temblor["type"], temblor["code"]]
                    serie= pd.Series(fila).str.wrap(15)
                    columna.append(serie)
            else:
                tamano_magnitud=lt.size(magnitud)
                for i in range(1,4):
                    temblor=lt.getElement(magnitud,i)
                    mag=temblor["mag"]
                    fila=[str(temblor["time"]),temblor["lat"],str(temblor["long"]),str(temblor["depth"]),str(temblor["sig"]),temblor["gap"], str(temblor["nst"]), temblor["title"], temblor["cdi"], temblor["mmi"], str(temblor["magType"]), temblor["type"], temblor["code"]]
                    serie= pd.Series(fila).str.wrap(15)
                    columna.append(serie)
                for i in range(tamano_magnitud-2,tamano_magnitud+1):
                    temblor=lt.getElement(magnitud,i)
                    mag=temblor["mag"]
                    fila=[str(temblor["time"]),temblor["lat"],str(temblor["long"]),str(temblor["depth"]),str(temblor["sig"]),temblor["gap"], str(temblor["nst"]), temblor["title"], temblor["cdi"], temblor["mmi"], str(temblor["magType"]), temblor["type"], temblor["code"]]
                    serie= pd.Series(fila).str.wrap(15)
                    columna.append(serie)

            tabla=tabulate(columna,tablefmt="grid")
            fila_2=[str(mag),str(lt.size(magnitud)),tabla]
            serie_2=pd.Series(fila_2)
            columna_2.append(serie_2)
    
    else:
        tamano_temblores=lt.size(temblores)
        
        for i in range(tamano_temblores,tamano_temblores-3,-1):
            magnitud=lt.getElement(temblores,i)
            columna=[["time","lat","long","depth","sig","gap","nst","title","cdi","mmi","magType","type","code"]]
            if lt.size(magnitud)<=6:
                for temblor in lt.iterator(magnitud):
                    mag=temblor["mag"]
                    fila=[str(temblor["time"]),temblor["lat"],str(temblor["long"]),str(temblor["depth"]),str(temblor["sig"]),temblor["gap"], str(temblor["nst"]), temblor["title"], temblor["cdi"], temblor["mmi"], str(temblor["magType"]), temblor["type"], temblor["code"]]
                    serie= pd.Series(fila).str.wrap(15)
                    columna.append(serie)
            else:
                tamano_magnitud=lt.size(magnitud)
                for i in range(1,4):
                    temblor=lt.getElement(magnitud,i)
                    mag=temblor["mag"]
                    fila=[str(temblor["time"]),temblor["lat"],str(temblor["long"]),str(temblor["depth"]),str(temblor["sig"]),temblor["gap"], str(temblor["nst"]), temblor["title"], temblor["cdi"], temblor["mmi"], str(temblor["magType"]), temblor["type"], temblor["code"]]
                    serie= pd.Series(fila).str.wrap(15)
                    columna.append(serie)
                for i in range(tamano_magnitud-2,tamano_magnitud+1):
                    temblor=lt.getElement(magnitud,i)
                    mag=temblor["mag"]
                    fila=[str(temblor["time"]),temblor["lat"],str(temblor["long"]),str(temblor["depth"]),str(temblor["sig"]),temblor["gap"], str(temblor["nst"]), temblor["title"], temblor["cdi"], temblor["mmi"], str(temblor["magType"]), temblor["type"], temblor["code"]]
                    serie= pd.Series(fila).str.wrap(15)
                    columna.append(serie)

            tabla=tabulate(columna,tablefmt="grid")
            fila_2=[str(mag),str(lt.size(magnitud)),tabla]
            serie_2=pd.Series(fila_2)
            columna_2.append(serie_2)

        for i in range(3,0,-1):
            magnitud=lt.getElement(temblores,i)
            columna=[["time","lat","long","depth","sig","gap","nst","title","cdi","mmi","magType","type","code"]]
            if lt.size(magnitud)<=6:
                for temblor in lt.iterator(magnitud):
                    mag=temblor["mag"]
                    fila=[str(temblor["time"]),temblor["lat"],str(temblor["long"]),str(temblor["depth"]),str(temblor["sig"]),temblor["gap"], str(temblor["nst"]), temblor["title"], temblor["cdi"], temblor["mmi"], str(temblor["magType"]), temblor["type"], temblor["code"]]
                    serie= pd.Series(fila).str.wrap(15)
                    columna.append(serie)
            else:
                tamano_magnitud=lt.size(magnitud)
                for i in range(1,4):
                    temblor=lt.getElement(magnitud,i)
                    mag=temblor["mag"]
                    fila=[str(temblor["time"]),temblor["lat"],str(temblor["long"]),str(temblor["depth"]),str(temblor["sig"]),temblor["gap"], str(temblor["nst"]), temblor["title"], temblor["cdi"], temblor["mmi"], str(temblor["magType"]), temblor["type"], temblor["code"]]
                    serie= pd.Series(fila).str.wrap(15)
                    columna.append(serie)
                for i in range(tamano_magnitud-2,tamano_magnitud+1):
                    temblor=lt.getElement(magnitud,i)
                    mag=temblor["mag"]
                    fila=[str(temblor["time"]),temblor["lat"],str(temblor["long"]),str(temblor["depth"]),str(temblor["sig"]),temblor["gap"], str(temblor["nst"]), temblor["title"], temblor["cdi"], temblor["mmi"], str(temblor["magType"]), temblor["type"], temblor["code"]]
                    serie= pd.Series(fila).str.wrap(15)
                    columna.append(serie)

            tabla=tabulate(columna,tablefmt="grid")
            fila_2=[str(mag),str(lt.size(magnitud)),tabla]
            serie_2=pd.Series(fila_2)
            columna_2.append(serie_2)

    print(tabulate(columna_2,tablefmt="grid"))

    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    min_magnitude=float(input("Ingrese la magnitud minima: "))
    max_depth=float(input("Ingrese la profundidad maxima: "))
    lista_p3_u3,lista,tiempo = controller.req_3(control, min_magnitude, max_depth)
    print("------REQ 3 RESULTS------")
    print("Total events diferent magnitudes: " + str(lt.size(lista)))
    print(f"Selecting {lt.size(lista)}...")
    if lt.size(lista) > 6:
        print("Results struct has more than 6 records...\n")
    else:
        print("Results struct has less than 6 records...\n")
    print("Tiempo de ejecución: "+str(tiempo))
    print(tabulate(lista_p3_u3['elements'], headers="keys", tablefmt='fancy_grid'))

def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    sig = input("Ingrese la significancia minima de la busqueda: ")
    gap = input("Ingrese la distancia azimutal maxima de la busqueda:  ")
    final = lt.newList("ARRAY_LIST")
    data, time = controller.req_4(control, sig, gap)
    
    size = lt.size(data)
    columna=[["mag","place","time","updated", "tz", "felt", "cdi", "mmi", "alert", "status", "tsunami", "sig", "net", "code", "ids", "sources", "types", "nst", "dmin", "rms", "gap", "magType", "type", "title", "long", "lat", "depth"]]
    if size>6:
        for i in range(0,6):
            if i<3:
                lt.addLast(final, data["elements"][i])
            else: 
                x = 6-i
                lt.addLast(final,data["elements"][size-1-x])
    else:
        final = data
        
    for x in final["elements"]:
        registro = []
        for v in x.values():
            v = str(v)
            if v == "":
                v = "Unknown"
            registro.append(v)    
        serie = pd.Series(registro).str.wrap(15)
        columna.append(serie)
        
        
    print("="*34)
    print(f"La función se tardo: {time}")
    print("La cantidadd de terremotos encontrados es: " + str(size))
    print(tabulate(columna, tablefmt="grid"))


def print_req_5(temblores):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5  
    columna_2=[["time","events","details"]]

    if lt.size(temblores)<=6:
        for i in range(1,lt.size(temblores)):
           
            temblor=lt.getElement(temblores,i)
            time=temblor["time"]
            fila=[str(temblor["mag"]),temblor["lat"],str(temblor["long"]),str(temblor["depth"]),str(temblor["sig"]),temblor["gap"], str(temblor["nst"]), temblor["title"], temblor["cdi"], temblor["mmi"], str(temblor["magType"]), temblor["type"], temblor["code"]]
            serie= pd.Series(fila).str.wrap(15)
            if i ==1:
                contador=1
                columna=[["mag","lat","long","depth","sig","gap","nst","title","cdi","mmi","magType","type","code"]]
                columna.append(serie)
            else:
                temblor_anterior=lt.getElement(temblores,i-1)
                if temblor_anterior["time"]==temblor["time"]:
                    columna.append(serie)
                    contador+=1
                else:
                    tabla=tabulate(columna,tablefmt="grid")
                    fila_2=[str(temblor_anterior["time"]),str(contador),tabla]
                    serie_2=pd.Series(fila_2)
                    columna_2.append(serie_2)
                    columna=[["mag","lat","long","depth","sig","gap","nst","title","cdi","mmi","magType","type","code"]]
                    contador=1
                    columna.append(serie)
            if i == lt.size(temblores):
                tabla=tabulate(columna,tablefmt="grid")
                fila_2=[str(time),str(contador),tabla]
                serie_2=pd.Series(fila_2)
                columna_2.append(serie_2)


        
    
    else:
        tamano_temblores=lt.size(temblores)
        indices=[1,2,3,tamano_temblores-2,tamano_temblores-1,tamano_temblores]
        for i in range(len(indices)):
            temblor=lt.getElement(temblores,indices[i])
            time=temblor["time"]
            fila=[str(temblor["mag"]),temblor["lat"],str(temblor["long"]),str(temblor["depth"]),str(temblor["sig"]),temblor["gap"], str(temblor["nst"]), temblor["title"], temblor["cdi"], temblor["mmi"], str(temblor["magType"]), temblor["type"], temblor["code"]]
            serie= pd.Series(fila).str.wrap(15)
            if indices[i] ==1:
                contador=1
                columna=[["mag","lat","long","depth","sig","gap","nst","title","cdi","mmi","magType","type","code"]]
                columna.append(serie)
            else:
                temblor_anterior=lt.getElement(temblores,indices[i-1])
                if temblor_anterior["time"]==temblor["time"]:
                    columna.append(serie)
                    contador+=1
                else:
                    tabla=tabulate(columna,tablefmt="grid")
                    fila_2=[str(temblor_anterior["time"]),str(contador),tabla]
                    serie_2=pd.Series(fila_2)
                    columna_2.append(serie_2)
                    columna=[["mag","lat","long","depth","sig","gap","nst","title","cdi","mmi","magType","type","code"]]
                    contador=1
                    columna.append(serie)

            if indices[i] == tamano_temblores:
                tabla=tabulate(columna,tablefmt="grid")
                fila_2=[str(time),str(contador),tabla]
                serie_2=pd.Series(fila_2)
                columna_2.append(serie_2)


    print(tabulate(columna_2,tablefmt="grid"))


    
    
    


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    anio = input("Ingrese el año de interes: ")


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    anio = input("Ingrese el año de interes: ")
    title = input("Ingrese el titulo de la regíon en la que desea buscar: ")
    prop = input("Ingrese la propiedad que desea contar (sig: significancia, mag: magnitud, depth: profundidad): ")
    data, time = controller.req_7(control, anio, title, prop)
    num_bins = int(input("Elija la cantidad de bins que desea: "))
    
    size = lt.size(data)-1
    print(f"la función se demoro: {time}")
    print(f"La cantidad de datos es: {lt.size(data)}")
    print(f"El dato mas pequeño de {prop} es: {data['elements'][0][prop]}")
    print(f"El dato mas grande de {prop} es: {data['elements'][size][prop]}")
    
    p_list = lt.newList("ARRAY_LIST")
    
    for x in lt.iterator(data):
        lt.addLast(p_list, x[prop])
        
    fig, (ax1, ax2) = plt.subplots(2)
        
    hist = ax1.hist(p_list["elements"], bins = num_bins, color="purple", histtype="bar", rwidth=0.8, align="mid", edgecolor="black")
    ax1.set_title(f"Histogram of {prop} in {title} \n\n", fontweight="bold", fontsize=14)
    plt.ylabel("No. of events")
    plt.xlabel(f"{prop}")
    plt.grid(visible= True, axis = "y", linestyle = "-", alpha = 0.7)
    
    array = []
    for i in range(0,6):
        if i <3:
            item = data["elements"][i]
        else:
            k = 6-1
            item = data["elements"][size-k]
        row = [str(item["time"][:16]), str(item["lat"]), str(item["long"]), str(item["title"]), str(item["code"]), str(item["mag"])]
        array.append(row)
        
    
    
    headers = ["time", "lat", "long", "title", "code", "mag"]
    ax2.set_axis_off()
    
    table = ax2.table(cellText=array, 
                      cellLoc="center",
                      colLabels=headers,
                      colLoc="center", 
                      loc="bottom",
                      colWidths = [0.15, 0.15, 0.15, 0.3, 0.1, 0.1])
    table.scale(1,2)
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    plt.subplots_adjust(bottom=0.373, hspace=0)
    

    
    plt.show()
    
    
    
    
        
    
    
    
    


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
            print("earthquakes event size:",data)
            print("\n===============================")
            print("===EARTHQUAKES RECORD REPORT===")
            print("===============================\n")
            print("----EARTHQUAKES RESULTS----")
            print("Total Earthquakes: ",data)
            print_data(control["model"]["temblores"],data)


        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            lower_mag=float(input('Ingrese el limite inferior de la magnitud: '))
            upper_mag=float(input("Ingrese el limite superior de la magnitud: "))
            resultado,contador=controller.req_2(control,lower_mag,upper_mag)
            print("======Req No. 2 Results======")
            print("Total different magnitudes",lt.size(resultado))
            print("Total events btween magnitudes:",contador)
            print_req_2(resultado)
            

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            profundidad_minima=float(input("Ingrese la profundidad minima: "))
            num_min_estaciones=int(input("Ingrese el numero minimo de estaciones: "))
            top_20,fechas,tamano_sorted_list=controller.req_5(control,profundidad_minima,num_min_estaciones)
            print("=====Req  No 2 inputs====")
            print("Min depth",profundidad_minima)
            print("=====Req No.5 Results=====")
            print("Total different dates:",fechas)
            print("Total events between dates:",tamano_sorted_list)
            print("Selecting the first 20 results...:")
            print_req_5(top_20)
            #for temblor in lt.iterator(top_20):
                #print(temblor)
            


        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
