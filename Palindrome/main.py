from distutils.core import setup
import Palindrome_CY
import Palindrome_PY
import time

#Creación archivo csv

formato_datos = "{:.9f},{:.9f},{:.9f}\n"
S = "lacomputacionparalelaesunatecnicadeprogramacionenlaquemuchasinstruccionesseejecutansimultaneamentesebasaenelprincipiodequelosproblemasgrandessepuedendividirenpartesmaspequenasquepuedenresolversedeformaconcurrente"

for i in range(20):

#Toma de tiempos para Python
    init_time=time.time()
    Palindrome_PY.maxNumPalindrome(S)
    end_time=time.time()

    time_python = end_time - init_time

#Toma de tiempos para Cython
    init_time=time.time()
    Palindrome_CY.maxNumPalindrome(S)
    end_time=time.time()

    time_cython = end_time - init_time

    mejora = time_python/time_cython

    with open("Palindrome.csv", "a") as archivo:
        archivo.write(formato_datos.format(time_python, time_cython, mejora))

archivo.close()

print("Tiempo de ejecucion Python: {}s\n".format(time_python))
print("Tiempo de ejcucion Cython: {}s\n".format(time_cython))

print("Cython es {} veces más rápido que Python ".format(round(time_python/time_cython, 2)))