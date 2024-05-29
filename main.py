def quicksort(list):
    #Verificar si la lista tiene 0 o 1 elementos
    if len(list) <= 1:
        return list
    else:
        #Seleccionar el pivote
        pivot = list[0]
        #Partición de la lista
        menor =[]
        mayor = []
        igual = []
        #Recorrer la lista
        for i in list:
            #Reorganizar los elementos de la sublista
            #Menores que el pivote
            if i < pivot:
                menor.append(i)
                #Iguales al pivote
            elif i == pivot:
                igual.append(i)
                #Mayores que el pivote
            else:
                mayor.append(i)
    #Llamadas recursivas y concatenación de las sublistas
        return quicksort(menor) + igual + quicksort(mayor)


# Pruebas
assert(quicksort([4,3,6,5,8,7,1,9]) == [1,3,4,5,6,7,8,9])


print("Pruebas exitosas")
