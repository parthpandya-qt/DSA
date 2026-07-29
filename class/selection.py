def selectionSort(l):
    n = len(l)

    for i in range(n - 1):
        min = i

        for j in range(i + 1, n):
            if l[j] < l[min]:
                min = j

        l[min], l[i] = l[i], l[min]

    return l


print(selectionSort([9, 6, 5, 7, 8, 4, 3]))