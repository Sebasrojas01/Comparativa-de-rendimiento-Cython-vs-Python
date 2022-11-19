#cython: language_level=3
cimport cython

def multiplicacion_matrices(a, b):

    cdef filas_Ma = len(a)
    cdef filas_Mb = len(b)
    cdef columnas_Ma = len(a[0])
    cdef columnas_Mb = len(b[0])
    cdef int i = 0
    cdef resultado = []
    for i in range(filas_Mb):
        resultado.append([])
        for j in range(columnas_Mb):
            resultado[i].append(None)
    
    for c in range(columnas_Mb):
        for i in range(filas_Ma):
            suma = 0
            for j in range(columnas_Ma):
                suma += a[i][j]*b[j][c]
            resultado[i][c] = suma
    return resultado