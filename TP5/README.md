# SIA - Trabajo Práctico 3

-   Patrick Dey
-   Matias Lombardi
-   Santos Rosati

## **Métodos de Aprendizaje No Supervisado**

### **Ejercicio 1a**

Utilizando un Autoencoder Generativo se busca que a partir de un conjunto de datos (en este caso bitmaps de fonts) generar nuevas letras a partir de lo que se aprende en la zona latente

### **Ejercicio 1b**

Utilizando un Autoencoder de Denoising (DAE) se busca, luego de entrenar a la red con un conjunto de datos con ruido, que al presentarle una font con ruido, esta pueda quitarselo

### **Ejercicio 2**

Utilizando un Autoencoder Variacional se busca generar una nuevo set de datos y determinar si pertenece al conjunto de datos original. Pare este ejercicio utilizamos como set de datos un conjunto imagenes de Pokemones en blanco y negro.

## Dependencias

Instalar las dependencias necesarias mediante el siguiente comando
pip install -r dependencies.txt

## Ejecución

1.  Descargar el repositorio https://github.com/srosati/SIA.git en la carpeta deseada
2.  Asegurarse de tener instalado la version 3.9.\* de python
3.  Tener en cuenta que los comandos python y pip tienen su equivalente en mac como python3 y pip3
4.  Crear un archivo de configuración (El repositorio provee algunas configuraciones de ejemplo)

5.  Ejecutar los siguiente comandso para iniciar los distintos programas

        - python exercise_1a.py
        - python exercise_1b.py
        - python exercise_2.py
