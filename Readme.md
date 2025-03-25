# Graficador de Hoja Milimetrada y Log-Log

Este proyecto fue desarrollado para automatizar la creación de gráficos en la clase de Física Mecánica. La herramienta permite generar gráficos de puntos sobre una hoja milimetrada o gráficos log-log a partir de datos proporcionados en archivos de texto.

## Descripción

La herramienta incluye dos scripts:

- **Milimetrada.py**: Genera gráficos sobre una hoja milimetrada, basándose en los datos de entrada que representan coordenadas y otros factores relacionados con la escala.
- **Log-Log.py**: Genera gráficos en escala logarítmica en ambos ejes (X y Y), para analizar relaciones que siguen una ley de potencia.

## ¿Cómo usarla?

### 1. Preparación del archivo de entrada

Antes de ejecutar cualquiera de los scripts, debes preparar el archivo de datos (ya sea `mil.txt` o `log.txt`) en el formato adecuado. Los pasos para preparar el archivo son los siguientes:

1. **Estructura del archivo**: El archivo de entrada debe seguir un formato específico con los encabezados definidos. **NO CAMBIES los encabezados**. Solo debes modificar los valores de los datos.

    **Ejemplo de archivo mil.txt**:

    ```
        Titulo de la grafica
        $V \text{ vs } T^2$
        Eje_x(Unidades),Eje_y(Unidades)
        $T^2 (s^2$),$V \left(\frac{m}{s}\right)$
        Variables Ecuacione Empirica Formato(Variable Dependiente, Variable Independiente)
        V,T^2
        Medida Eje_x,Medida Eje_y
        23,18
        Factor de escala Eje_x, Factor de escala Eje_y
        0.46,10.6
        Puntos Tomados para la toma de puntos debes seguir el siguiente formato: 
        Si tiene que sacar promedio debera poner primero todos los datos de la observacion en "x" separados 
        por coma y luego en el eje "y" asi sucesivamente para todas las observaciones.
        1x1,1x2,1x3....1xn
        1y1,1y2,1y3,...1yn
        2x1,2x2,2x3,...2xn
        2y1,2y2,2y3,...2yn
        nx1,nx2,nx3,...nxn
        nx1,nx2,nx3,...nxn
    ```

    
2. **Asegúrate de seguir el formato correcto** para los datos. Los valores deben estar separados por comas, y cada par de valores debe estar en una nueva línea.

### 2. Ejecución del script

Una vez que hayas preparado el archivo de datos correctamente, puedes proceder con la ejecución del script:

- **Para generar el gráfico en una hoja milimetrada**:
    1. Asegúrate de que el archivo de datos esté nombrado como `mil.txt`.
    2. Ejecuta el script `Milimetrada.py`.

- **Para generar el gráfico log-log**:
    1. Asegúrate de que el archivo de datos esté nombrado como `log.txt`.
    2. Ejecuta el script `Log-Log.py`.

#### Instrucciones para ejecutar los scripts:

1. Abre una terminal o consola.
2. Navega hasta la carpeta donde se encuentra el archivo `.py`.
3. Ejecuta el siguiente comando:

    ```bash
    python Milimetrada.py
    ```

    O para el gráfico log-log:

    ```bash
    python Log-Log.py
    ```

### 3. Personalización

Los usuarios pueden personalizar los gráficos ajustando los parámetros en los archivos de datos, como:

- **Escala de los ejes**: Ajusta los factores de escala para representar los datos en diferentes unidades.
- **Número de puntos**: Modifica el número de puntos a graficar.
- **Título y etiquetas de los ejes**: Personaliza el título del gráfico y las etiquetas de los ejes X e Y.

### 4. ¿Qué hace el código?

El código procesa los datos de entrada de los archivos `.txt` y realiza los siguientes pasos:

1. Lee los datos del archivo de entrada.
2. Calcula las coordenadas de los puntos en función de los factores de escala.
3. Dibuja el gráfico en una hoja milimetrada o en escala logarítmica.
4. Muestra el gráfico con las etiquetas y el título correspondientes.

## Requisitos

Para ejecutar este proyecto, asegúrate de tener las siguientes dependencias instaladas:

- **Python 3.x** (preferentemente la última versión)
- **Bibliotecas**:
    - `numpy`
    - `matplotlib`

Puedes instalar las dependencias necesarias utilizando `pip`:

```bash
pip install numpy matplotlib