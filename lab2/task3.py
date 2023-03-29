# Сумма все возможных комбинации троек чисел в массиве
def find_triples_sum(arr):
    n = len(arr)
    total_sum = 0

    # Внешний цикл
    for i in range(n):

        # Средний цикл
        for j in range(i + 1, n):

            # Внутренний цикл
            for k in range(j + 1, n):
                total_sum += arr[i] + arr[j] + arr[k]

    return total_sum

arr = [1, 2, 5, 8, 9, 2]
result = find_triples_sum(arr)
print('Сумма все возможных комбинации троек чисел в массиве -', result)


# Сортировка слиянием
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

arr = [6, 5, 3, 4, 8, 0, 10, 100, 20, 14]
print('Изначальный массив:', arr)

result = merge_sort(arr)
print('Отсортированный массив:', result)

# Все перестановки элементов заданного массива
def permutations(arr):
    if len(lst) == 0:
        return [[]]
    result = []
    for i in range(len(lst)):
        rest = lst[:i] + lst[i+1:]
        for p in permutations(rest):
            result.append([lst[i]] + p)
    return result

arr = [1, 2, 3]
print(permutations(arr))

# Сумма кубов всех элементов в двумерном списке
def sum_of_cubes(arr):
    n = len(lst)
    result = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result += lst[i][j][k] ** 3
    return result

arr = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(sum_of_cubes(arr))

# Бинарный поиск
def binary_search(arr, search_item):
    low = 0
    high = len(arr) - 1
    search_res = False
    col = 0

    while (low <= high) and (not search_res):
        col += 1
        middle = (low + high) // 2
        guess = arr[middle]
        if guess == search_item:
            search_res = True
        if guess > search_item:
            high = middle - 1
        else:
            low = middle + 1
    return [search_res, col]


arr = [3, 5, 11, 12, 15, 23, 25, 34, 67, 86]
value = 67

result = binary_search(arr, value)
if result[0]:
    print('Найденное число -', result[1])
else:
    print('Не найден')
print()