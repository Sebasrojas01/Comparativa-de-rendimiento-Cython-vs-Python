from distutils.core import setup
import multiplicacion_matreces_CY
import multiplicacion_matreces_PY
import time
import numpy as np

#Creación archivo csv

formato_datos = "{:.5f},{:.5f},\n"

np.random.seed(237)

A = np.random.randint(20,90,size = (200,200))
B = np.random.randint(13,100,size = (200,200))


for i in range(20):

#Toma de tiempos para Python
    init_time=time.time()
    multiplicacion_matreces_PY.multiplicacion_matrices(A,B)
    end_time=time.time()

    time_python = end_time - init_time

#Toma de tiempos para Cython
    init_time=time.time()
    multiplicacion_matreces_CY.multiplicacion_matrices(A,B)
    end_time=time.time()

    time_cython = end_time - init_time

    with open("Multiplicacion_Matrices.csv", "a") as archivo:
        archivo.write(formato_datos.format(time_python, time_cython))

archivo.close()

print("Tiempo de ejecucion Python: {}s\n".format(time_python))
print("Tiempo de ejcucion Cython: {}s\n".format(time_cython))

print("Cython es {} veces más rápido que Python ".format(round(time_python/time_cython, 2)))
