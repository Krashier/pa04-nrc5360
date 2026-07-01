def merge_sort(arr, inicio, fin):
    if inicio >= fin:
        return

    medio = (inicio + fin) // 2

    merge_sort(arr, inicio, medio)
    merge_sort(arr, medio + 1, fin)

    mezclar(arr, inicio, medio, fin)


def mezclar(arr, inicio, medio, fin):
    izquierda = arr[inicio:medio + 1]
    derecha = arr[medio + 1:fin + 1]

    i = 0
    j = 0
    k = inicio

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            arr[k] = izquierda[i]
            i += 1
        else:
            arr[k] = derecha[j]
            j += 1
        k += 1

    while i < len(izquierda):
        arr[k] = izquierda[i]
        i += 1
        k += 1
    while j < len(derecha):
        arr[k] = derecha[j]
        j += 1
        k += 1


if __name__ == "__main__":
    tiempos = [12, 7, 25, 4, 18, 9, 15, 2]
    merge_sort(tiempos, 0, len(tiempos) - 1)
    print(tiempos)   # Resultado esperado: [2, 4, 7, 9, 12, 15, 18, 25]