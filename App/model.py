"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
import datetime as dt
from datetime import datetime as d
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    temblores = lt.newList(datastructure="ARRAY_LIST")
    magnitud=om.newMap(omaptype="RBT")
    data_structs = {"temblores": temblores,"magnitud":magnitud
               
                    }
    return data_structs
    


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    lista = data_structs['temblores']
    lt.addLast(lista,data)

    mapa_magnitud=data_structs["magnitud"]
    magnitud=float(data["mag"])
    if om.contains(mapa_magnitud,magnitud):
        mapentry=om.get(mapa_magnitud,magnitud)
        magnitud_search=me.getValue(mapentry)
        lt.addLast(magnitud_search,data)
    else:
        magnitud_search=lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(magnitud_search,data)
        om.put(mapa_magnitud,magnitud,magnitud_search)
    return data_structs


# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    return lt.size(data_structs)

def make_datetime(string):
    temp = string.split("T")
    temp[0] = temp[0].split("-")
    temp[1] = temp[1].split(":")
    x = temp[1][2].split(".")
    temp.append(x)
    size = len(temp[2][1]) - 1
    rta = dt.datetime(year=int(temp[0][0]), month=int(temp[0][1]), day=int(temp[0][2]), hour=int(temp[1][0]), minute=int(temp[1][1]), second=int(temp[2][0]), microsecond=int(temp[2][1][0:size]))
    return rta
    
def req_1(data_structs, ini_date, fin_date):
    """
    Descripción: Una lista que retorna una lista los terremotos
                 que sucedierón en un rango de fechas
    Args: 
         - data_structs: variable donde están cargados los datos
         - ini_date: fecha en la cual inicia la busqueda
         - fin_date: fecha en la cual finaliza la busqueda
    Return: Lista de los terremotos que sucedieron en el rango
    """
    # TODO: Realizar el requerimiento 1

    #Primero hacemos un árbol RBT de los datos de los terremotos
    #Usamos las fechas como las llaves, pasandolas por la función 
    #datetime de la librería datetime
    lista = lt.newList("ARRAY_LIST")
    map = om.newMap(omaptype="RBT")
    
    for item in (data_structs["temblores"]["elements"]):
        om.put(map, (item["time"]), item)

    #Una vez tenemos el árbol conseguimos una lista de todas las llaves
    #Iteramos sobre la lista comparando las fechas
    #Si una fecha cae dentro del rango, integramamos la información
    #de su registro
    keys = om.keySet(map)
    ini_dt = make_datetime(ini_date)
    fin_dt = make_datetime(fin_date)

    for j in lt.iterator(keys):
        key = make_datetime(str(j))
        if ini_dt <= key <= fin_dt:
            x = om.get(map, j)
            lt.addLast(lista, x)

    return lt.size(lista), lista




def req_2(data_structs,lower_mag,upper_mag):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    arbol=data_structs["magnitud"]
    temblores_filtrados=om.values(arbol,lower_mag,upper_mag)
    contador=0
    for temblores_mag in lt.iterator(temblores_filtrados):
        merg.sort(temblores_mag,cmp_temblores_by_fecha)
        contador+=lt.size(temblores_mag)
    return temblores_filtrados,contador


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista

    pass

def cmp_temblores_by_fecha(resultado1,resultado2):
    date_1=d.strptime(resultado1["time"], "%Y-%m-%dT%H:%M:%S.%fZ")
    date_2=d.strptime(resultado2["time"], "%Y-%m-%dT%H:%M:%S.%fZ")
    if date_1<=date_2:
        return False
    elif date_1>date_2:
        return True

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
