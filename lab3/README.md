## Лабораторная работа №3

### Задание 1

Написать программу с функциями для быстрой сортировки и сортировки расческой. Оценить время выполнения функций с помощью модуля timeit.

#### Быстрая сортировка

```
import timeit

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = [10, 7, 8, 9, 1, 5]
print("Неотсортированный массив:", arr)
sorted_arr = quick_sort(arr)
print("Отсортированный массив:", sorted_arr)

# Оценка времени выполнения функции
time = timeit.timeit(lambda: quick_sort(arr), number=100)
print("Время выполнения:", time)
```

> Время выполнения: 0.0009859330000000013

#### Сортировка расчесткой

```
import timeit

def comb_sort(arr):
    gap = len(arr)
    shrink = 1.3
    sorted = False
    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True
        i = 0
        while i + gap < len(arr):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
            i += 1
    return arr

arr = [10, 7, 8, 9, 1, 5]
print("Неотсортированный массив:", arr)
sorted_arr = comb_sort(arr)
print("Отсортированный массив:", sorted_arr)

# Оценка времени выполнения функции
time = timeit.timeit(lambda: comb_sort(arr), number=100)
print("Время выполнения:", time)
```

> Время выполнения: 0.0004420889999999997

### Задание 2

Изучить блочную, пирамидальную и сортировку слиянием. Написать соответствующие программы.

#### Блочная сортировка

```
import timeit

def bucket_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    bucket_range = max_val - min_val + 1
    buckets = []
    for i in range(bucket_range):
        buckets.append([])
    for num in arr:
        buckets[num - min_val].append(num)
    sorted_arr = []
    for bucket in buckets:
        sorted_arr += sorted(bucket)
    return sorted_arr

arr = [10, 7, 8, 9, 1, 5]
print("Неотсортированный массив:", arr)
sorted_arr = bucket_sort(arr)
print("Отсортированный массив:", sorted_arr)

# Оценка времени выполнения функции
time = timeit.timeit(lambda: bucket_sort(arr), number=100)
print("Время выполнения:", time)
```

> Время выполнения: 0.0005160080000000053

#### Пирамидная сортировка

```
import timeit

def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[largest] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

arr = [10, 7, 8, 9, 1, 5]
print("Неотсортированный массив:", arr)
sorted_arr = heap_sort(arr)
print("Отсортированный массив:", sorted_arr)

# Оценка времени выполнения функции
time = timeit.timeit(lambda: heap_sort(arr), number=100)
print("Время выполнения:", time)
```

> Время выполнения: 0.0009704380000000006


#### Сортировка слиянием

```
import timeit

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

arr = [10, 7, 8, 9, 1, 5]
print("Неотсортированный массив:", arr)
sorted_arr = merge_sort(arr)
print("Отсортированный массив:", sorted_arr)

# Оценка времени выполнения функции
time = timeit.timeit(lambda: merge_sort(arr), number=100)
print("Время выполнения:", time)
```

> Время выполнения: 0.0008619700000000001

### Задание 3

Оцените достоинства, недостатки и сложность изученных методов сортировок. 

#### Сравнение

Сравнение изученных методом сортировок.