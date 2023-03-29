# Произведение двух чисел
def multiply(a, b):
    return a * b

a = 2
b = 5

print('Первое число -', a, ', второе число -', b)
print('Произведение чисел -', multiply(a, b))
print()


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


# Сумма всех возможных пар элементов в массиве
def sum_of_pairs(arr):
    n = len(arr)
    total = 0
    for i in range(n):
        for j in range(i+1, n):
            total += arr[i] + arr[j]
    return total

arr = [10, 23, 1, 32, 5, 7, 9, 12, 72]
result = sum_of_pairs(arr)
print('Сумма всех возможных пар элементов -', result)
print()


# Нахождение числа Фибоначчи
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 10
result = fibonacci(n)
print('Число Фибоначчи под номером 10 -', result)