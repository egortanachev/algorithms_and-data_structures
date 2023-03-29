## Лабороторная работа №2

### Задание 1

Построить зависимость между количеством элементов и количеством шагов для алгоритмов со сложностью $О(1)$, $O(log n)$, $O(n^2)$, $O(2^n)$. Сравнить сложность данных алгоритмов.

#### Алгоритм со сложностью $О(1)$ (Произведение двух чисел)

```
def multiply(a, b):
    return a * b

a = 2
b = 5

print('Первое число -', a, ', второе число -', b)
print('Произведение чисел -', multiply(a, b))
```

> Количество элементов - 2, количество шагов для алгоритма - 1

#### Алгоритм со сложностью $О(log n)$ (Бинарный поиск)

```
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
    print(result[1])
else:
    print('Не найден')
```

> Количество элементов - 16, количество шагов для алгоритма - 4

#### Алгоритм со сложностью $О(n^2)$ (Сумма всех возможных пар элементов в массиве)

```
def sum_of_pairs(arr):
    n = len(arr)
    total = 0
    for i in range(n):
        for j in range(i+1, n):
            total += arr[i] + arr[j]
    return total

arr = [10, 23, 1, 32, 5, 7, 9, 12, 72]
result = sum_of_pairs(arr)
print(result)
```

> Количество элементов - 10, количество шагов для алгоритма - 100

#### Алгоритм со сложностью $О(2^n)$ (Нахождение числа Фибоначчи)

```
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 10
result = fibonacci(n)
print(result)
```

> Значение элемента - 5, количество шагов для алгоритма - 32

### Задание 2

Написать программу для пузырьковой сортировки. Оценить сложность данного метода. Сравнить с методом sort

```
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
```

> Сложность сортировки пузырьковым методом составляет $O(n^2)$. То есть, к примеру, для 10 элементов в худшем случае количество шагов составит 100.

### Задание 3

Придумать и реализовать алгоритмы, имеющие сложность $O(3n)$, $O(n \cdot logn)$, $O(n!)$, $O(n^3)$, $O(3log(n))$

```
Код
```