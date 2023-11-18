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
import math
from tabulate import tabulate
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
    profundidad=om.newMap(omaptype="RBT")
    data_structs = {"temblores": temblores,"magnitud":magnitud,"profundidad":profundidad
               
                    }
    return data_structs
    


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    lista = data_structs['temblores']
    if data["nst"]=="":
        data["nst"]= 1
    if int(data["tsunami"])==0:
        data["tsunami"]="False"
    if data["cdi"]=="":
        data["cdi"]="Unavailable"
    if data["mmi"]=="":
        data["mmi"]="Unavailable"
    if data["gap"]=="":
        data["gap"]=0.0
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
    
    mapa_profundidad=data_structs["profundidad"]
    profundidad=float(data["depth"])
    if om.contains(mapa_profundidad,profundidad):
        mapentry=om.get(mapa_profundidad,profundidad)
        profundidad_search=me.getValue(mapentry)
        lt.addLast(profundidad_search,data)
    else:
        profundidad_search=lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(profundidad_search,data)
        om.put(mapa_profundidad,profundidad,profundidad_search)
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
    
def cmpfunction_int(anio1, anio2):
    anio1 = int(anio1)
    anio2 = int(anio2)
    
    if anio1 > anio2:
        return 1
    elif anio1 == anio2:
        return 0
    else: 
        return -1
    
    
def cmpfunction_str(str1, str2):
    str1 = str(str1)
    str2 = str(str2)
    
    if str1 > str2:
        return 1
    elif str1 == str2:
        return 0 
    else:
        return -1
    
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


def req_3(analyzer,min_magnitude,max_depth):
    eventos_filtrados = lt.newList('ARRAY_LIST')
    
    for evento in lt.iterator(analyzer['temblores']):
        
        if (float(evento['mag']) >= min_magnitude and float(evento['depth']) <= max_depth):
            
            lt.addLast(eventos_filtrados,evento)
            
    eventos_filtrados= merg.sort(eventos_filtrados, compare)
    
    eventos_resultado = lt.subList(eventos_filtrados, 1, 10)
    
    lista_p3_u3 = lt.newList("ARRAY_LIST")
    
    if lt.size(eventos_resultado) < 6:
        
        return eventos_resultado
    
    else:
        
        for i in range(3):
            
            lt.addFirst(lista_p3_u3, eventos_resultado["elements"][i])
            
        tamaño = lt.size(eventos_resultado)
        
        for i in range(tamaño - 3, tamaño):
            
            lt.addFirst(lista_p3_u3, eventos_resultado["elements"][i])
            
    return lista_p3_u3,eventos_resultado
    
def compare(lt1, lt2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    if lt1['time'] > lt2['time']:
        return True
    else:
        return False
 
def cmp_4(sig1, sig2):
    sig1 = int(sig1)
    sig2 = int(sig2)

    if sig1>sig2:
        return 1
    elif sig2>sig1:
        return -1
    else:
        return 0
    
def CmpSortR4(item1, item2):
    
    sig1 = int(item1)
    sig2 = int(item2)

    if sig1>sig2:
        return True
    else:
        return False
    
    

def req_4(data_structs, sig, gap):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    #creamos el mapa que usaremos para el req 4
    #usamos el valor "sig" como llave
    
    mapa = om.newMap(omaptype="RBT", cmpfunction=cmp_4)
    #hacemos la lista donde guardaremos todos los temblores que caen en el rango
    lista = lt.newList("ARRAY_LIST")
    #convertimos el valor de gap en float para poder compararlo mas adelante
    gap = float(gap)
    #añadimos los datos al arbol
    for item in data_structs["temblores"]["elements"]:
        om.put(mapa, item["sig"], item)
    #conseguimos la llave mas grande en el arbol
    max_key = om.maxKey(mapa)
    #usando la llave que conseguimos antes y el minimo que nos da el usuario encontramos todas las llaves entre ellas
    keys = om.keys(mapa, sig, max_key)
    keys = merg.sort(keys, CmpSortR4)
    #Hacemos un bloque de for donde revisamos si el gap es menor de el dado por el usuario
    for key in lt.iterator(keys):
        item = om.get(mapa, key)
        if item['value']['gap'] == '' or item["value"]["gap"] =="Unkown":
            item['value']['gap']  = 'Unknown'
        elif float(item["value"]["gap"])< gap:
            lt.addLast(lista, item["value"])
    #retornamos el tamaño (para la cantidad de terremotos) y la lista de datos que extraimos 
    return lista
        


def req_5(data_structs,profundidad_minima,numero_minimo_estaciones):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    arbol=data_structs["profundidad"]
    maximo=om.maxKey(arbol)
    temblores_profundidad=om.values(arbol,profundidad_minima,maximo)
    temblores_profundidad_nst=lt.newList("ARRAY_LIST")
    fechas=lt.newList("ARRAY_LIST")
    for profundidad in lt.iterator(temblores_profundidad):
        for temblor in lt.iterator(profundidad):
            if temblor["nst"]!="":
                if float(temblor["nst"])>=numero_minimo_estaciones:
                    lt.addLast(temblores_profundidad_nst,temblor)
                    if lt.isPresent(fechas,temblor["time"])==False:
                        lt.addLast(fechas,temblor["time"])
    sorted_list=merg.sort(temblores_profundidad_nst,cmp_temblores_by_fecha_and_magnitud)
    if lt.size(sorted_list)>20:
        top_20=lt.subList(sorted_list,1,numelem=20)
    else:
        top_20=sorted_list
    return top_20,lt.size(fechas),lt.size(sorted_list)
    


def req_6(catalog, startDate, endDate, focusLatitude, focusLongitude, radio, numberOfImportantEvents):
    """
    Función que soluciona el requerimiento 6
    
    # TODO: Realizar el requerimiento 6
    """
    datesIndex = catalog['datesIndex']
    radio_tierra = 6371
    startDate = d.strptime(startDate, "%Y-%m-%dT%H:%M:%S.%fZ")
    endDate = d.strptime(endDate, "%Y-%m-%dT%H:%M:%S.%fZ")
    lon2 = focusLongitude
    lat2 = focusLatitude
    eventsList = om.values(datesIndex, startDate.strftime("%Y-%m-%d %H:%M:%S"), endDate.strftime("%Y-%m-%d %H:%M:%S"))
    eventsWithinRadious = lt.newList("ARRAY_LIST")
    for list in lt.iterator(eventsList):
        for event in lt.iterator(list):
            
            lon1 = float(event["long"])
            lat1 = float(event["lat"])
            
            lat1_rad = math.radians(lat1)
            lon1_rad = math.radians(lon1)
            lat2_rad = math.radians(lat2)
            lon2_rad = math.radians(lon2)
            
            dlat = lat2_rad - lat1_rad
            dlon = lon2_rad - lon1_rad
            
            a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            
            distancia = radio_tierra * c
            
            if distancia < radio:
                time = d.strptime(event['time'], "%Y-%m-%dT%H:%M:%S.%fZ")
                info = {'time': time.strftime("%Y-%m-%dT%H:%M"),
                        'mag': "%.3f" % float(event['mag']),
                        'lat': "%.3f" % float(event['lat']),
                        'long': "%.3f" % float(event['long']),
                        'depth': "%.3f" % float(event['depth']),
                        'sig': int(event['sig']),
                        'gap': 0.0 if event['gap'] == "" else float(event['gap']),
                        'distance': float(round(distancia, 2)),
                        'nst': 1 if event['nst'] == "" else float(event['nst']),
                        'title': event['title'],
                        'cdi': 'Unavailable' if event['cdi'] == "" else float(event['cdi']),
                        'mmi': 'Unavailable' if event['mmi'] == "" else float(event['mmi']),
                        'magType': event['magType'],
                        'type': event['type'],
                        'code': event['code']
                        }
                lt.addLast(eventsWithinRadious, info)
                
                
    numberOfEvents = lt.size(eventsWithinRadious)             
    maxSig = 0
    maxEvent = None
    i = 0
    for event in lt.iterator(eventsWithinRadious):
        i += 1
        if float(event["sig"]) > maxSig:
            maxSig = float(event["sig"])
            maxEvent = event
            posMaxSig = i
            
    maxEventReturn = lt.newList("ARRAY_LIST")
    lt.addLast(maxEventReturn, maxEvent)         
    
    if (posMaxSig + numberOfImportantEvents) < lt.size(eventsWithinRadious):
        eventsAfter = lt.subList(eventsWithinRadious, posMaxSig, numberOfImportantEvents + 1)
    else:
        eventsAfter = lt.subList(eventsWithinRadious, posMaxSig, (lt.size(eventsWithinRadious) - posMaxSig) + 1)
    
    if (posMaxSig - numberOfImportantEvents) > 1:
        eventsBefore = lt.subList(eventsWithinRadious, posMaxSig - numberOfImportantEvents, numberOfImportantEvents)
    else:
        eventsBefore = lt.subList(eventsWithinRadious, 1, posMaxSig - 1)
        
    postN = lt.size(eventsBefore)
    preN = lt.size(eventsAfter) - 1
    code = maxEvent['code']
    
    eventsFoundIndex = om.newMap('RBT')    
    
    for event in lt.iterator(eventsBefore):
        entry = om.get(eventsFoundIndex, event['time'])
        if entry == None:
            list = lt.newList("ARRAY_LIST") 
        else:
            list = me.getValue(entry)
        info = {'mag': event['mag'],
                'lat': event['lat'],
                'long': event['long'],
                'depth': event['depth'],
                'sig': event['sig'],
                'gap': event['gap'],
                'distance': event['distance'],
                'nst': event['nst'],
                'title': event['title'],
                'cdi': event['cdi'],
                'mmi': event['mmi'],
                'magType': event['magType'],
                'type': event['type'],
                'code': event['code']
                }
        lt.addLast(list, info)
        om.put(eventsFoundIndex, event['time'], list)
        
    for event in lt.iterator(eventsAfter):
        entry = om.get(eventsFoundIndex, event['time'])
        if entry == None:
            list = lt.newList("ARRAY_LIST") 
        else:
            list = me.getValue(entry)
        info = {'mag': event['mag'],
                'lat': event['lat'],
                'long': event['long'],
                'depth': event['depth'],
                'sig': event['sig'],
                'gap': event['gap'],
                'distance': event['distance'],
                'nst': event['nst'],
                'title': event['title'],
                'cdi': event['cdi'],
                'mmi': event['mmi'],
                'magType': event['magType'],
                'type': event['type'],
                'code': event['code']
                }
        lt.addLast(list, info)
        om.put(eventsFoundIndex, event['time'], list)
        
    datesList = om.keySet(eventsFoundIndex)
    totalDates = lt.size(datesList)
    totalEventsBetweenDates = 0
    
    eventsFound = lt.newList("ARRAY_LIST")
    
    for date in lt.iterator(datesList):
        entry = om.get(eventsFoundIndex, date)
        details = me.getValue(entry)
        totalEventsBetweenDates += lt.size(eventsFound)
        info = {'time': date,
                'events': lt.size(details),
                'details': tabulate(lt.iterator(details), headers="keys", tablefmt="grid", numalign= "left")}
        lt.addLast(eventsFound, info)
        
    return maxEventReturn, eventsFound, numberOfEvents, totalDates, totalEventsBetweenDates, code,postN, preN



def req_7(data_structs, anio, title, prop):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    #Primero hacemos el arbol
    #Para esta función queremos un arbol con llaves de cada año que contiene arboles orfganizados por la propiedad dada
    mapa = om.newMap(omaptype="RBT", cmpfunction=cmpfunction_int)
    rta = lt.newList("ARRAY_LIST")
    for i in lt.iterator(data_structs["temblores"]):
        year = i["time"][:4]
        if om.contains(mapa, year):
            item = om.get(mapa, year)
            lt.addLast(item["value"], i)
        else:
            leaf = lt.newList("ARRAY_LIST")
            lt.addLast(leaf, i)
            om.put(mapa, year, leaf)
            
    p = om.get(mapa, anio)
    for x in lt.iterator(p["value"]):
        if title in x["title"]:
            lt.addLast(rta, x)
    if prop in [ "mag", ""]:
        cmpfunction = cmp_temblores_mag
    elif prop == "depth":
        cmpfunction = cmp_temblores_depth
    else:
        cmpfunction = cmp_temblores_sig
    final = merg.sort(rta, sort_crit=cmpfunction)
    return final
            
    
                    

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
    
def cmp_temblores_mag(item1, item2):
    
    item1 = float(item1["mag"])
    item2 = float(item2["mag"])
    
    if item1>item2:
        return False
    else:
        return True
    

def cmp_temblores_depth(item1, item2):
    
    item1 = float(item1["depth"])
    item2 = float(item2["depth"])
    
    if item1>item2:
        return False
    else:
        return True

def cmp_temblores_sig(item1, item2):
    
    item1 = int(item1["sig"])
    item2 = int(item2["sig"])
    
    if item1>item2:
        return False
    else:
        return True
 
def cmp_temblores_by_fecha_and_magnitud(resultado1,resultado2):
    date_1=d.strptime(resultado1["time"], "%Y-%m-%dT%H:%M:%S.%fZ")
    date_2=d.strptime(resultado2["time"], "%Y-%m-%dT%H:%M:%S.%fZ")
    if date_1<date_2:
        return False
    elif date_1>date_2:
        return True
    elif date_1==date_2:
        if resultado1["mag"]<=resultado2["mag"]:
            return False
        else:
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
