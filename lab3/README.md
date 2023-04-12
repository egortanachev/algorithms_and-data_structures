## Лабороторная работа №3

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

#### Программа

```
Код
```

> Описание

### Задание 3

Оцените достоинства, недостатки и сложность изученных методов сортировок. 

#### Сравнение

Сравнение изученных методом сортировок.