# zinobe-challenge
Python/Pandas, Python/request test

|  Region | Country |  Languaje | Time  |
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


**¿Cómo se hizo?**


1. Voy a obtener todos los países con el siguiente filtro:
	 https://restcountries.com/v2/continent/europe?fields=region,name,capital,languages

	 Así tengo todos los países con los siguientes campos,
	 región
	 nombre
	 capital
	 lenguajes

2. Agarrar la información que necesito de cada país, es decir del lenguaje,
	 sólo voy a agarrar el nombre del languaje, y para los países que tenga más
	 de un lenguaje se hace una lista de lenguajes.

	 languages:
	 	iso... : "ca"
	 	iso... : "ca"
	 	name : "Catalan"
	 	nativeName : "català"

3.	Se hace una función la cuál será una propiedad de clase que se encargue de
		hashear esa lista de lenguajes en un sólo string que se codificará, es
		decir:

		---> si tiene varios lenguajes
		[español, inglés, alemán] => españolinglésalemán => hash SHA1

4. Reemplazo la información de lenguage con el resultado del método del hash en
	 en el objeto.

5. Hago los objetos y los convierto en una lista en el main.py para volverlos
	 un insumo para la Pandas y la creación de los diferentes dataframes.

6. Con la información hago una dataframe en Pandas.

4. Luego saco cada una de los valores únicos de las regiones,

5. Con esa lista de regiones hago aplico un filtro para obtener un dataframe
	 por región y de cada uno de estos dataframes saco una muestra de un elemento
	 y con cada uno de esos elementos, hago un nuevo dataframe que tiene
	 efectivamente un elemento de cada región elegido de manera aleatoria.

6. Guardo la tabla en SQLite (Sólo se puede guardar una tabla por vez, pq desde
	 la función que estoy utilizando no puedo reescribir la información de la
	 tabla).

7. Guardo el dataframe como un Json (recordar que el nombre debe de ser
	 data.json)

8. Como paso final, hago las pruebas unitarias de la clase generadora de
	 objetos Country, con el fin de eliminar las fuentes de error desde la fuente,
	 ya que como todas las funciones y flujos de trabajo se hacen al rededor de
	 esa, es la clase es la más crítica de corroborar que esta bien.

	 En las pruebas unitarias se testean las siguientes cosas:
	 - Constructor de valores iniciales.
	 - Constructor con valores incompletos.
	 - Constructor con valores vacíos.
	 - Constructor sin valores.
	 - Tipos del objeto entrante al constructor y los tipos de cada uno de los atributos
