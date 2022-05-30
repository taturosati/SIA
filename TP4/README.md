# SIA - Trabajo Práctico 3

-   Patrick Dey
-   Matias Lombardi
-   Santos Rosati

## **Métodos de Aprendizaje No Supervisado**

### **Ejercicio 1**

Se utiliza una red de Kohonen (self-organizing maps) y la regla de Oja para agrupar países en base a distintas características y para generar un índiceque permita ordenarlos

### **Ejercicio 2**

Se utiliza una Red de Hopefield para almacenar e identificar 4 patrones de letras con ruido. Ademas de identificar un estado espurio mediante un patron ruidoso.

## Dependencias

Instalar las dependencias necesarias mediante el siguiente comando
pip install -r dependencies.txt

## Ejecución

1.  Descargar el repositorio https://github.com/srosati/SIA.git en la carpeta deseada
2.  Asegurarse de tener instalado la version 3.9.\* de python
3.  Tener en cuenta que los comandos python y pip tienen su equivalente en mac como python3 y pip3
4.  Crear un archivo de configuración (El repositorio provee algunas configuraciones de ejemplo)

5.  Ejecutar el siguiente comando para iniciar el programa

        python main.py [config file]

## Archivo de configuración

Un archivo en formato .json con los siguientes parametros (cabe destacar que todos cuentan con un valor default):

-   **excercise**: Selecciona el ejercicio a ejecutar
    -   Valores posibles: 1, 2
-   **item**: Selecciona el item del ejercicio elegido a ejecutar
    -   Valores posibles: a, b (según el ejercicio)
-   **eta**: Valor del eta
-   **limit**: Selecciona el limite de iteraciones
-   **grid_k**: Selecciona el tamaño de la grilla de salida (k x k) en kohonnen
-   **spurius_noise**: Selecciona la probabilidad de agregar ruido para el estado espurio
-   **noise**: Selecciona la probabilidad de agregar ruido
-   **radius**: Selecciona el radio a utilizar

Ejemplos:

-   Ejecuta el ejercicio 1, item a con los parametros correspondientes

```json
{
	"exercise": 1,
	"item": "a",
	"eta": 0.1,
	"grid_k": 4,
	"radius": 2
}
```

-   Ejecuta el ejercicio 1, item b con los parametros correspondientes

```json
{
	"exercise": 1,
	"item": "b",
	"eta": 0.0001,
	"limit": 500000
}
```

-   Ejecuta el ejercicio 2

```json
{
	"exercise": 2,
	"spurius_noise": 0.3,
	"noise": 0.1
}
```
