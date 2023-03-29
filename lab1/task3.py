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