#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sofi
"""
#importo una libreria que me permite conectarme con internet y hacer consultas a APIs
import requests

#uso la api key para saber quien consulta, contar solicitudes.. es como una contraseña
API_KEY = "TU_API_KEY"

#creo una función para validar el texto, chequea si son todas letras
def validar_texto(texto):
    #lanza error si se escriben numeros
    if not texto.isalpha():
        raise ValueError("Solo se permiten letras")
    #devuelve el nombre de manera prolija: primer letra mayuscula, el resto minuscula
    return texto.capitalize()

#Creo una función que recibe un nombre, consulta en internet y devuelve datos
def consultar_nacionalidad(nombre):

    #dirección de la API
    url = "https://api.nationalize.io"
    #armo el pedido
    params = {"name": nombre,"apikey": API_KEY}
    #pido información
    respuesta = requests.get(url, params=params)
    #Las APIs responden con códigos asi que hago que salte error si no es 200
    if respuesta.status_code != 200:
        raise Exception("Error al consultar API")
    
    #convierte la respuesta JSON en un diccionario de Python
    return respuesta.json()

#esta funcion analiza los datos devueltos por la API
def obtener_pais_mas_probable(datos):
    #agarro solo la lista de paises
    paises = datos["country"]
    #creo una variable para guardar la prob mas alta encontrada
    mayor_probabilidad = 0
    #aca voy a guardar el codigo del pais ganador
    pais_mas_probable = ""

    #recorro la lista de pais por pais
    for pais in paises:
        #comparo probabilidades
        if pais["probability"] > mayor_probabilidad:
            #guardo la nueva prob mayor
            mayor_probabilidad = pais["probability"]
            #guardo el pais correspondiente
            pais_mas_probable = pais["country_id"]
    
    # Devuelvo el país más probable
    return pais_mas_probable

def formatear_probabilidad(probabilidad):
    #toma la probabilidad
    #la paso a porcentaje y la redondea
    #la convierte en texto y le agrega el simbolo %
    return str(round(probabilidad * 100, 1)) + "%"
