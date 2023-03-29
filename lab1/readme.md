## Лабороторная работа №1

### Задание 1

Написать программу для бинарного поиска. Результатом должно быть количество шагов, которое потребуется, чтобы найти требуемое число.

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

list = [3, 5, 11, 12, 15, 23, 25, 34, 67, 86]
value = 67

result = binary_search(list, value)
if result[0]:
    print(result[1])
else:
    print('Не найден')
```

### Задание 2

Для учебной группы составить словарь, который будет описывать характеристики каждого из студентов. Реализовать программу, которая по определенным характеристикам будет угадывать студента.

Пример выполнения:

> Студент курит?

> Нет.

> Студент блондин?

> Да.

> …

> …

> Вы загадали Ивана Иванова. 

```
student_list = [
        {
            'name': 'Иван Иванов',
            'smoke': True,
            'blond': True,
            'grade': True
        },
        {
            'name': 'Даниил Петров',
            'smoke': True,
            'blond': True,
            'grade': False
        },
        {
            'name': 'Василий Теркин',
            'smoke': True,
            'blond': False,
            'grade': True
        },
        {
            'name': 'Кирилл Спешилов',
            'smoke': True,
            'blond': False,
            'grade': False
        },
        {
            'name': 'Денис Куертов',
            'smoke': False,
            'blond': True,
            'grade': True
        },
        {
            'name': 'Павел Гаврилов',
            'smoke': False,
            'blond': True,
            'grade': False
        },
        {
            'name': 'Андрей Чуркаев',
            'smoke': False,
            'blond': False,
            'grade': True
        },
        {
            'name': 'Алексей Сафонов',
            'smoke': False,
            'blond': False,
            'grade': False
        }
    ]

def guess_student(student_list, smoke, blond, grade):
    if (smoke == 'Да') or (smoke == 'да'):
        smoke = True
    if (smoke == 'Нет') or (smoke == 'нет'):
        smoke = False

    if (blond == 'Да') or (blond == 'да'):
        blond = True
    if (blond == 'Нет') or (blond == 'нет'):
        blond = False

    if (grade == 'Да') or (grade == 'да'):
        grade = True
    if (grade == 'Нет') or (grade == 'нет'):
        grade = False

    i = 0
    while i < len(student_list):
        if (student_list[i]['smoke'] == smoke) and (student_list[i]['blond'] == blond) and (
                student_list[i]['grade'] == grade):
            return(student_list[i]['name'])
        i += 1

    return('Студент не найден')

print('Студент курит?')
smoke = input()
print('Студент блондин?')
blond = input()
print('Студент отличник?')
grade = input()

result = guess_student(student_list, smoke, blond, grade)
print(result)
```

### Задание 3

Составьте граф для задания №2.

```
import networkx as nx
import matplotlib.pyplot as plt

students_keys = ['name', 'smoke', 'blond', 'grade']
students_list = [
        {
            'name': 'Иван Иванов',
            'smoke': True,
            'blond': True,
            'grade': True
        },
        {
            'name': 'Даниил Петров',
            'smoke': True,
            'blond': True,
            'grade': False
        },
        {
            'name': 'Василий Теркин',
            'smoke': True,
            'blond': False,
            'grade': True
        },
        {
            'name': 'Кирилл Спешилов',
            'smoke': True,
            'blond': False,
            'grade': False
        },
        {
            'name': 'Денис Куертов',
            'smoke': False,
            'blond': True,
            'grade': True
        },
        {
            'name': 'Павел Гаврилов',
            'smoke': False,
            'blond': True,
            'grade': False
        },
        {
            'name': 'Андрей Чуркаев',
            'smoke': False,
            'blond': False,
            'grade': True
        },
        {
            'name': 'Алексей Сафонов',
            'smoke': False,
            'blond': False,
            'grade': False
        }
    ]

graph = nx.Graph()
for i in range(len(students_list)):
    graph.add_node(students_list[i]['name'])

for i in range(len(students_keys)):
    graph.add_node(students_keys[i])

for i in range(len(students_list)):
    for j in range(len(students_keys)):
        if (students_list[i][students_keys[j]]):
            graph.add_edge(students_list[i]['name'], students_keys[j], graph=graph)


nx.draw_circular(graph, node_color='red', node_size=1000, with_labels=True)
plt.show()
```