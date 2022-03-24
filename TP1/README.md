# SIA - Trabajo Práctico 1
- Patrick Dey
- Matias Lombardi
- Santos Rosati

## Rompecabezas de 8 números

Se tiene una grilla de 3 x 3, donde hay 8 piezas, numeradas del 1 al 8, en una cierta configuración inicial. A partir de eso, desplazando las piezas, se desea llegar a la configuración final con la forma
| 1 | 2 | 3 |
|---|---|---|
| 4 | 5 | 6 |
| 7 | 8 |   |

Cabe destacar que algunas configuraciones iniciales no tienen solución
## Dependencias
Instalar las dependencias necesarias mediante el siguiente comando
	 
	 pip install -r dependencies.txt
	
## Ejecución
1) Descargar el repositorio https://github.com/srosati/SIA.git en la carpeta deseada
2) Asegurarse de tener instalado la version 3.9.* de python
3) Tener en cuenta que los comandos python y pip tienen su equivalente en mac como python3 y pip3
4) Crear un archivo de configuración (El repositorio provee algunas configuraciones de ejemplo)
5) Ejecutar el siguiente comando para iniciar el programa	

		python main.py [config file]
6) De tener solución el tablero, el programa generara un archivo "solution.txt" con la misma
## Archivos de configuración
Un archivo en formato .json con los siguientes parametros:
- **algo**: Selecciona el algoritmo (Obligatorio)
	- BPA
	- BPP
	- BPPV
	- LOCAL
	- GLOBAL
	- A*
- **initial_state**: Configuración del tablero. (Por default se _randomiza_)
	- Es un string enumerado del 0 al 8 sin espacios
- **heu**: Selecciona la heuristica para los algoritmos informados (El default es EUC)
	- EUC: Suma de distancias euclidia
	- OOP: Cantidad de piezas fuera de lugar
	- MAN: Suma de distancias Manhattan con penalización por piezas invertidas
- **limit**: Valor numerico positivo para establecer el limite inicial del algoritmo BPPV (El default 20)

Ejemplos: 
- Configuración sin solución 
```json
{ 
  "algo": "GLOBAL",
  "initial_state": "812043765" 
}
```
- Configuración con solución 
```json
{ 
  "algo": "BPPV",
  "initial_state": "056832147",
  "limit": 12
}
```
- Configuración con la solución de mayor costo
```json
{ 
  "algo": "A*",
  "initial_state": "867254301",
  "heu":"MAN"
}
```
