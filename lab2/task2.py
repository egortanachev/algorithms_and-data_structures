def bubble_sort(arr):
    n = len(arr)
    # Повторяем проходы через массив n-1 раз
    for i in range(n-1):
        # Перебираем элементы массива от 0 до n-i-1
        for j in range(0, n-i-1):
            # Если текущий элемент больше следующего, меняем их местами
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [6, 5, 3, 4, 8, 0, 10, 100, 20, 14]
print('Изначальный массив:', arr)

result = bubble_sort(arr)
print('Отсортированный массив:', result)