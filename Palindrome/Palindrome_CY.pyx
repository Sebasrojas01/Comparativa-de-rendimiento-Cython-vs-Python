#cython: language_level=3
cimport cython

#Programa que maximiza el recuento de subsecuencias palindrómicas de 3 longitudes con cada parte de índice de una sola subsecuencia
def maxNumPalindrome(S):
	#Índice de la S
	cdef int j = 0
	cdef int l 

	# Almacena la frecuencia de cada carácter
	freq = [0] * 26

	# Almacena el par de frecuencias que contienen los mismos caracteres
	cdef int freqPair = 0
	l = len(S)

	# Número de subsecuencias teniendo longitud 3
	cdef int ln = l // 3

	# Cuenta la frecuencia
	while(j < l):
		freq[ord(S[j]) - ord('a')] += 1
		j = j + 1

	# Cuenta el par de frecuencia
	cdef int i = 0
	for i in range(26):
		freqPair += (freq[i] // 2)

	# Devuelve el valor mínimo
	return min(freqPair, ln)

"""
# Código del conductor
if __name__ == '__main__':

	S = "geeksforg"

	print(maxNumPalindrome(S))
"""