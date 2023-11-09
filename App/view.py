"""
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
    size, data = controller.req_1(control, fecha_ini, fecha_fin)
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
    print("La cantidadd de terremotos encontrados es: " + str(size))
    print(tabulate(columna, tablefmt="grid"))
        
        
    


def print_req_2(temblores):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    lista=[1,2,3,lt.size(temblores)-2,lt.size(temblores)-1,lt.size(temblores)]   
    columna_2=[["mag","events","details"]]

    if lt.size(temblores)<=6:
        for magnitud  in lt.iterator(temblores):
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
        for i in range(1,4):
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
        
        for i in range(tamano_temblores-2,tamano_temblores+1):
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
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    sig = input("Ingrese la significancia minima de la busqueda: ")
    gap = input("Ingrese la distancia azimutal maxima de la busqueda:  ")
    final = lt.newList("ARRAY_LIST")
    size, data = controller.req_4(control, sig, gap)
    
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
    print("La cantidadd de terremotos encontrados es: " + str(size))
    print(tabulate(columna, tablefmt="grid"))


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


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
            print_req_5(control)

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
