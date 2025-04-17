# Lista dada
numeros = [2, 5, 2, 2, 4, 8, 7, 3]

# 1. Mostrar la lista
print("1. Lista original:", numeros)

# 2. Sumar los números pares
suma_pares = sum(n for n in numeros if n % 2 == 0)
print("2. Suma de los números pares:", suma_pares)

# 3. Armar otra lista con los números impares
impares = [n for n in numeros if n % 2 != 0]
print("3. Lista con los números impares:", impares)

# 4. Verificar el tamaño de las listas con la función len
print("4. Tamaño de la lista original:", len(numeros))
print("   Tamaño de la lista de impares:", len(impares))

# 5. Hallar el elemento mayor y menor de la lista
mayor = max(numeros)
menor = min(numeros)
print("5. Elemento mayor:", mayor)
print("   Elemento menor:", menor)

# 6. Ordenar la lista
ordenada = sorted(numeros)
print("6. Lista ordenada:", ordenada)
