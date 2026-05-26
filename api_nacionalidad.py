#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sofi
"""
import requests

API_KEY = "TU_API_KEY"

def validar_texto(texto):

    if not texto.isalpha():
        raise ValueError("Solo se permiten letras")

    return texto.capitalize()


def consultar_nacionalidad(nombre):

    url = "https://api.nationalize.io"

    params = {"name": nombre,"apikey": API_KEY}

    respuesta = requests.get(url, params=params)

    if respuesta.status_code != 200:
        raise Exception("Error al consultar API")

    return respuesta.json()


def obtener_pais_mas_probable(datos):

    paises = datos["country"]

    if len(paises) == 0:
        return None

    return max(paises, key=lambda x: x["probability"])


def formatear_probabilidad(probabilidad):

    return f"{probabilidad * 100:.1f}%"
