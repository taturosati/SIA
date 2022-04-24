# SIA - Ejercicio Obligatorio 1

-   Patrick Dey
-   Matias Lombardi
-   Santos Rosati

## Método de Optimización NO lineal

Dadas 3 mediciones realizadas sobre un reactivo se desea aproximar los valores de salida para otras posibles mediciones, por una función $F(W,w,w_{0},\xi )$, donde W es un vector de tres coordenadas de números reales, w es una matriz de dimensión 2 × 3 de números reales, y $w_{0}$ = ($w_{01}$, $w_{02}$) también de números reales.

Esto se realizara buscando la minimización de la función de error $E(W,w,w_{0})$ mediante los metodos de optimización por **Gradiente Descendiente**, **Gradientes Conjugadas** y por el método de **Adam**

-   $$F(W,w,w_{0},\xi ) = g(\sum_{j=1}^{2}W_{j} \cdot g(\sum_{k=1}^{2}w_{jk}\cdot\xi_{k}-w_{0j})-W_{0})$$

-   $$E(W,w,w_{0}) = \sum_{\mu = 1}^{3}(\zeta ^{\mu }-F(W,w,\xi ^{\mu }))^{2}$$

-   $$g(x)=\frac{e^{x}}{1+e^{x}}$$

## Dependencias

Instalar las dependencias necesarias mediante el siguiente comando
pip install -r dependencies.txt

## Ejecución

1.  Descargar el repositorio https://github.com/srosati/SIA.git en la carpeta deseada
2.  Asegurarse de tener instalado la version 3.9.\* de python
3.  Tener en cuenta que los comandos python y pip tienen su equivalente en mac como python3 y pip3
4.  Crear un archivo de configuración (El repositorio provee algunas configuraciones de ejemplo)
5.  Ejecutar el siguiente comando para iniciar el programa

        python main.py

    Este devolvera el resultado optimo del problema para 3 metodos distintos: Gradiente Descendente, Conjugación de Gradientes y Metodo ADAM

## Resultados óptimos

-   Gradiente Descendiente
    ```
      Time: 0.01194310188293457
      Optimal solution
      - W: [-0.19007274310072553, 0.1117282524008133, 0.1117282524008133]
      - w: [
            [-0.041724368751473895, -0.002122577491924571, 0.03554511946626415]
            [-0.041724368751473895, -0.002122577491924571, 0.03554511946626415]
        ]
      - w0: [-0.002347013275248777, -0.002347013275248777]
      - Error: 0.6801816128501843
    ```
-   Gradientes Conjugadas
    ```
      Time: 0.011232852935791016
      Optimal solution
      - W: [6.149791395356611, 7.121820079774245, 7.121820079774245]
      - w: [
            [-2.7609105156760476, 0.5392961974570846, 2.3459389823907757]
            [-2.7609105156760476, 0.5392961974570846, 2.3459389823907757]
        ]
      - w0: [0.0628373991505721, 0.0628373991505721]
      - Error: 4.720716971989189e-06
    ```
-   Adam

    ```
      Time: 1.1997499465942383
      Optimal solution
      - W: [8.099628786659245, 8.485636669543878, 8.485636669543878]
      - w: [
            [-2.305111762883408, -0.6197283706152314, 2.177430953427529]
            [-2.305111762883408, -0.6197283706152314, 2.177430953427529]
          ]
      - w0: [0.7623970110244708, 0.7623970110244708]
      - Error: 1.3151231815667763e-07
    ```
