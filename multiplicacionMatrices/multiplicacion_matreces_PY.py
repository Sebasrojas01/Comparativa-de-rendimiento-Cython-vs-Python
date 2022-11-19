def multiplicacion_matrices(a, b):
    filas_Ma = len(a)
    filas_Mb = len(b)
    columnas_Ma = len(a[0])
    columnas_Mb = len(b[0])

    resultado = []
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