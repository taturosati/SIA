# SIA - Trabajo Práctico 2

- Patrick Dey
- Matias Lombardi
- Santos Rosati

## Problema de la mochila

Dado un conjunto de n elementos, donde cada uno tiene asociado un peso y un beneficio, queremos maximizar la cantidad de beneficio que podemos poner dentro de una mochila que esta limitada por una capacidad maxima tanto de elementos como de peso. Esto se lograra mediante la optimización por Algoritmos Genéticos

## Dependencias

Instalar las dependencias necesarias mediante el siguiente comando
pip install -r dependencies.txt

## Ejecución

1.  Descargar el repositorio https://github.com/srosati/SIA.git en la carpeta deseada
2.  Asegurarse de tener instalado la version 3.9.\* de python
3.  Tener en cuenta que los comandos python y pip tienen su equivalente en mac como python3 y pip3
4.  Crear un archivo de configuración (El repositorio provee algunas configuraciones de ejemplo)
5.  Asegurarse de tener en el mismo directorio un archivo llamado data.txt donde la primer linea tiene 2 columnas separadas por un espacio _[capacidad maxima de la mochila] [peso maximo de la mochila]_ y las siguientes representan cada elemento con su beneficio y su peso de la forma _[beneficio] [peso]_

    Ejemplo:

    ```
    100 995
    94 485
    506 326
    416 248
    992 421
    649 322
    237 795
    ```

6.  Ejecutar el siguiente comando para iniciar el programa

        python main.py [config file]

## Archivos de configuración

Un archivo en formato .json con los siguientes parametros:

- **selection**: Config. del metodo de selección
  - direct
  - roulette
  - rank
  - boltzman
    - _k_
    - _t0_: Temperatura incial
    - _tf_: Temperatura final (<t0)
  - truncate
    - _trunc_: cantidad de elementos a truncar
  - tournament
    - _u_: valor numerico perteneciente a [0,5 ; 1]
- **cross**: Config. del metodo de cruza
  - simple
  - multiple
    - _multiple_cross_n_: cantidad de indices generados
  - uniform
- **p**: Probabilidad de mutar
- **gen**: Cantidad minima de generaciones a iterar

Ejemplos:

- Selección truncada con cruza uniforme

```json
{
  "selection": "truncate",
  "cross": "uniform",
  "p": 0.001,
  "trunc": 65
}
```

- Selección directa con cruza multiple

```json
{
  "selection": "direct",
  "cross": "multiple",
  "multiple_cross_n": 12,
  "p": 0.001
}
```

- Selección Boltzman con cruza uniforme

```json
{
  "selection": "boltzman",
  "t0": 10000,
  "tf": 8000,
  "k": 1,
  "cross": "uniform",
  "p": 0.001
}
```
