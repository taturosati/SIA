# SIA - Trabajo Práctico 3

-   Patrick Dey
-   Matias Lombardi
-   Santos Rosati

## **Redes Neuronales**

### **Ejercicio 1**

Mediante el uso de un perceptron simple se desea aprender a separar linealmente las funciones logicas AND y XOR dados un conjunto de datos de entrada y su correspondientes salidas

El perceptron simple unicamente puede aprender problemas que son linealmente separables por lo que la funcion logica AND es aprendida de forma correcta mientras que la función lógica XOR no es posible

### **Ejercicio 2**

Dado un conjunto de entrada y de salida se desea separarlos de manera tanto lineal y no lineal. Para ello se utiliza un perseptron simple con función de activación lineal y no lineal (para el no lineal se estara utilizando la funcion g(x) = tanh(ßh).

Para poder evaluar si la red realmente esta aprendiendo el problema especificado se decidio un metodo de metrica en el cual se cuenta la cantidad de aciertos una vez entrenada la red.

En sintesis, la red entrena con un conjunto de datos y luego de que el error se redujo lo suficiente, se la expone a los mismos datos de entrada y se evalua la capacidad que tiene de predecir la salida.

Asi mismo, para evaluar la capacidad de generalización de la red, los datos se dividen en k partes. Se entrena la red con k-1 partes y luego se predice con la parte restante. Luego, contamos la cantidad de aciertos sobre el total

### **Ejercicio 3**

Para este ejercicio se trataran de resolver diversos problemas utilzando una red neuronal multicapa

### Item a

Mediante el uso de una red neuronal de 2 capas, la capa oculta con 2 neuronas y la de salida con una unica neurona se buscara poder resolver el problema del ejercicio 1 en el que queremos separar y aprender la funcion logica XOR

### Item b

Se le presenta a la red multicapa un conjunto imagenes de 5x7 pixeles en las cuales se representan numeros del 0 al 9. En base a esto, la idea es que la red aprenda a discernir si el numero presentado es par o impar.

En cuanto a la capacidad de generalización, utilzando el mismo sistema de evaluacion que en el ejercicio 2, pudimos observar que la red no tiene capacidad para generalizar. Esto se debe posiblemente a 2 cosas. Primero, puede deberse a que la cantidad de pixeles utilzados son muy pocos por lo que un cambio en un pixel puede variar completamente la predicción de la red. Segundo, entendemos que no hay una relacion entre la forma de representar un numero con su paridad

### Item c

Parecido al item b, se presenta a la red multicapa el mismo conjunto de imagenes pero la diferencia es el objetivo. En este item, se busca que la red sepa diferenciar el numero que se le presento. Luego, una vez que la capa haya entrenado, al mismo conjunto de datos se les agrega ruido para probar que si la red puede seguir diferenciando los numeros de entrada

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

-   **beta**: Selecciona valor de ß
-   **eta**: Selecciona el valor de eta
-   **excer**: Selecciona el ejercicio a ejecutar
    -   Valores posibles: 1, 2, 3
-   **item**: Selecciona el item del ejercicio elegido a ejecutar
    -   Valores posibles: a, b, c (según el ejercicio)
-   **validation**: Utiliza validacion cruzada en el ejercicio 2.b
-   **k**: Selecciona la cantidad de partes a utilizar en el calculo de validación cruzada
-   **limit**: Selecciona el limite de iteraciones
-   **error_bound**: Selecciona el margen de error para la red multicapa

Ejemplos:

-   Ejecuta el ejercicio 1, item a con los parametros correspondientes

```json
{
	"excer": 1,
	"item": "a",
	"beta": 0.8,
	"eta": 0.1,
	"limit": 10000
}
```

-   Ejecuta el ejercicio 2, item b con los parametros correspondientes

```json
{
	"excer": 2,
	"item": "b",
	"beta": 0.6,
	"validation": true,
	"eta": 0.4,
	"limit": 7500
}
```

-   Ejecuta el ejercicio 3, item c con los parametros correspondientes

```json
{
	"excer": 3,
	"item": "c",
	"beta": 0.8,
	"eta": 0.1,
	"error_bound": 0.001
}
```
