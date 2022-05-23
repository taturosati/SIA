# SIA - Ejercicio Obligatorio 2

-   Patrick Dey
-   Matias Lombardi
-   Santos Rosati

## Componentes principales

Dado un conjunto de datos que representan los paises europeos, se desea calcular las componentes principales.
Las variables son:
- Country
- Area
- GDP
- Inflation
- Life.expect
- Military
- Pop.growth
- Unemployment

## Dependencias

Instalar las dependencias necesarias mediante el siguiente comando
pip install -r dependencies.txt

## Ejecución

1.  Descargar el repositorio https://github.com/srosati/SIA.git en la carpeta deseada
2.  Asegurarse de tener instalado la version 3.9.\* de python
3.  Tener en cuenta que los comandos python y pip tienen su equivalente en mac como python3 y pip3
4.  Asegurarse de tener el archivo 'europe.csv' en el mismo directorio
5.  Ejecutar el siguiente comando para iniciar el programa

        python main.py

    Este devolvera el las componentes principales y los graficos correspondientes

## Resultados

-   Componentes principales

    ```
        PC1  0.124874 -0.500506   0.406518    -0.482873  0.188112   -0.475704      0.271656
        PC2 -0.172872 -0.130140  -0.369657     0.265248  0.658267    0.082622      0.553204
        PC3  0.898297  0.083956   0.198195     0.246082  0.243679    0.163697      0.000500
        PC4  0.044850 -0.084255   0.164686     0.026771 -0.562375    0.392463      0.701968
        PC5 -0.324017  0.390632   0.689501    -0.101787  0.368148    0.347868      0.010159
    ```

-   Variabilidad de las cargas
    ```
        0.46102367  0.16958906  0.15188436    0.11005085    0.06540695  0.02409627  0.01794884
    ```
