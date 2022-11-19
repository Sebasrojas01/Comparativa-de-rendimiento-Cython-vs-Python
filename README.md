<p align = center  
<br>
<img src="https://res-5.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco/v1455514364/pim02bzqvgz0hibsra41.png" align="center"><br><FONT FACE="times new roman" SIZE=5>
<b>Tercer Parcial: Computación Paralela y Distribuida - Comparativa de rendimiento Cython vs Python</b>
<br>
<i><b>Autor:</b></i> Juan Sebastián Rojas Acevedo - 8º semestre
<br>
<i><b>Fecha: </b>20/11/2022
<br>
<b>Ciencias de la computación e Inteligencia Artificial - Universidad Sergio Arboleda</b></i>
<br>
</FONT>


# Python y Cython ¿Qué son?

* Python es un lenguaje de programación muy utilizado hoy en día, entre otras razones por que es cómodo para programar a alto nivel, además cuenta con muchas librerías y es un código fácilmente mantenible. A pesar de todas estas ventajas, cabe destacar que es notoriamente lento, por lo que es conveniente conocer algunas herramientas que permitan acelerar el código Python.

  Para esto se crea Cython, este es un lenguaje que se escribe de forma muy similar a Python, pero permite la utilización de librerías y variables de tipo C. Por tanto, se puede conseguir la velocidad de C manteniendo la simplicidad de sintaxis proporcionada por Python. Además, una de sus grandes versatilidades es que se pueden mezclar definiciones explícitas de variables C con variables de Python, como pueden ser los diccionarios.

* Sin embargo, programar en Cython también comporta una serie de inconvenientes, como la necesidad de compilar el código por separado antes de ejecutar el programa. También está el hecho de que comparado con lenguajes como C o Fortran, no tiene un soporte tan bueno para la paralelización de memoria.

# Objetivo: Comparativa  de rendimiento Cython vs Python

* Durante el desarrollo del ejercicio se seleccionan dos Algoritmos (Multiplicación de Matrices y el Palindrome de 3 Longitudes) con el fin de comparar los tiempos de rendimiento que se gastan a la hora de ser ejecutados con Python y con Cython y comprobar que Cython tiene un mejor rendimiento acomparación de Python.  

* También hay que tener en cuenta el sistema operativo en el que se realizan las pruebas, para este paso es recomendable y sumamente eficiente emplear un Software ligero, como Ubuntu, debido a que este sistema operativo tiene un kernel de Linux basado en Debian, teniendo en cuenta su uso sencillo y el completo dominio que le brinda a su empleador; además de la cantidad de subprocesos innecesarios que tiene en segundo plano, es inferior en comparación con otros sistemas operativos, esto permite que las pruebas realizadas como la multiplicación para la toma de rendimiento tenga un mayor porcentaje de éxito y fiabilidad.

# Construcción
1. Para la elaboración de este Algoritmo se opto por la multiplicación de Matrices Clasica para poder evidenciar mejor los tiempos empleados por cada Lenguaje, teniendo un Archivo principal llamado ***main.py*** donde se llamaran a cada una las funciones de cada lenguaje para ejecutar el algoritmo y las funciones de tiempo para contabilizar el tiempo empleado por cada uno, tiempo incial y tiempo final, además con esgte archivo se quieren guardar lo tiempo que se ejecuten por cada repetición en un **.csv** para trabajar con esos datos si así se desea.  

2. Se debe crear un archivo con el algoritmo que se desea trabajar para cada uno de los lenguajes, en este caso al trabjar con Python y Cython se crea un **.py** y un **.pyx**, recordando que el ALgoritmo se escoge primo para Python y una vez se tiene listo y define en Cython acoplandolo con lo necesario para que se ejecute con las reglas que este lenguaje maneja.

3. Es necesario crear un Setup con el nombre del archivo **.pyx** para generar el archivo **.c** y el **.so** para poder ejecutar posteriormente el programa.

4. Para la elaboración de este proyecto se crea un **Makefile** con el fin de correr el setup (**make all**) y borrar (**clean**)los archivos generados por este cuando se realizan cambios en el codigo así como el **.csv** 

</p>
