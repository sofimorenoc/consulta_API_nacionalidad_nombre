# consulta\_API\_nacionalidad\_nombre



Implementación de Pandas para lectura del dataset:
Para leer un dataset con Pandas, se agregaría al principio del archivo:

import pandas as pd

Y despues una función para cargar los datos desde un archivo CSV:

def cargar_dataset(ruta_archivo):
   datos = pd.read_csv(ruta_archivo)
   return datos

Esto devuelve una tabla con todos los datos listos para usar.

Las funciones a modificar son:
Si los nombres se obtuvieran desde un dataset en lugar de ingresarse manualmente, las funciones que habría que modificar son:

* validar_texto(texto): ahora solo valida que el texto ingresado sea solo letras. Habría que adaptarla para recorrer cada nombre del dataset en lugar de recibir uno solo.

* consultar_nacionalidad(nombre): habría que llamarla dentro de un bucle, una vez por cada nombre presente en el dataset, en lugar de consultarla una sola vez.

Las funciones `obtener_pais_mas_probable` y `formatear_probabilidad` no necesitarían cambios, ya que solo procesan los datos que reciben sin importar su origen.



Carmin, Male y Sofi

