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