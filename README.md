# zinobe-challenge
Python/Pandas, Python/request test

|  Region | City Name |  Languaje | Time  |
|---|---|---|---|
|  Africa | Angola  |  AF4F4762F9BD3F0F4A10CAF5B6E63DC4CE543724 | 0.23 ms  |
|   |   |   |   |
|   |   |   |   |

Desarrolle una aplicacion en python que genere la tabla anterior teniendo las siguientes consideraciones:

1. De https://rapidapi.com/apilayernet/api/rest-countries-v1, obtenga todas las
	 regiones existentes.
2. De https://restcountries.eu/ Obtenga un pais por region apartir de la region
	 optenida del punto 1.
3. De https://restcountries.eu/ obtenga el nombre del idioma que habla el pais
	 y encriptelo con SHA1
4. En la columna Time ponga el tiempo que tardo en armar la fila (debe ser
	 automatico)
5. La tabla debe ser creada en un DataFrame con la libreria PANDAS
6. Con funciones de la libreria pandas muestre el tiempo total, el tiempo
	 promedio, el tiempo minimo y el maximo que tardo en procesar toda las filas
	 de la tabla.
7. Guarde el resultado en sqlite.
8. Genere un Json de la tabla creada y guardelo como data.json
9. La prueba debe ser entregada en un repositorio git.


**Es un plus si:**
* No usa famework
* Entrega Test Unitarios
* Presenta un diseño de su solucion.


**¿Cómo voy a hacer?**


1. Voy a obtener todos los países con el siguiente filtro:
	 https://restcountries.com/v2/continent/europe?fields=region,name,capital,languages

	 Así tengo todos los países con los siguientes campos,
	 región
	 nombre
	 capital
	 lenguajes

2. Agarrar la información que necesito de cada país, es decir del lenguaje,
	 sólo voy a agarrar el nombre del languaje

	 languages:
	 	iso... : "ca"
	 	iso... : "ca"
	 	name : "Catalan"
	 	nativeName : "català"

3. Con la información hago una dataframe en Pandas.

4. Luego saco cada una de las regiones, quito los duplicados y con esa lista de
	 regiones hago los filtros necesarios.

5. Hago otro dataframe con la información que se pide en la tarea.

6. Guardo la tabla en SQLite

7. Guardo el dataframe como un Json (recordar que el nombre debe de ser
	 data.json)

8. Hacer pruebas de las funciones que se van realizando.
