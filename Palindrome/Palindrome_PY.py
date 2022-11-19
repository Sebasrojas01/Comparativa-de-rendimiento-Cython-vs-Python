#Programa que maximiza el recuento de subsecuencias palindrómicas de 3 longitudes con cada parte de índice de una sola subsecuencia
def maxNumPalindrome(S):
	
	# Índice de la S
	i = 0

	# Almacena la frecuencia de cada carácter
	freq = [0] * 26

	# Almacena el par de frecuencias que contienen los mismos caracteres
	freqPair = 0

	# Número de subsecuencias teniendo longitud 3
	ln = len(S) // 3

	# Cuenta la frecuencia
	while (i < len(S)):
		freq[ord(S[i]) - ord('a')] += 1
		i += 1

	# Cuenta el par de frecuencia
	for i in range(26):
		freqPair += (freq[i] // 2)

	# Devuelve el valor mínimo
	return min(freqPair, ln)

