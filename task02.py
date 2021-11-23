"""
Third hw
"""

its_my_list = ['one', 'two', 'and three']
its_my_vocabulary = {'0': 'B-52', '1': 'Tequila', '2': 'Long-Ailend'}
its_my_set = {'Geltok', 'Belok', 'YAiko'}

print(its_my_list[1])
print('=' * 80)
# Напиать условие if с двумя блоками elif и блоком else.
a = '3'
if a == '0':
    print(its_my_vocabulary.get(a))
elif a == '1':
    print(its_my_vocabulary.get(a))
elif a == '2':
    print(its_my_vocabulary.get(a))
else:
    print('go home!')

print('=' * 80)
# Написать цикл while.
b = int(a)
while b >= 0:
    its_my_set.add('new {}'.format(a))
    b = b - 1

print('-' * 80)
# Создать список из трех элементов и распечать его элементы с помощью цикла for
for m in its_my_set:
    print(m)

print('*' * 80)
# распечатать числа от 0 до 5
for m in range(6):
    print(m)

print('~' * 80)
# * создать строку 'TEST', если в ней есть буква 'E', напечатать 'pass'

s = 'TEST'
if s.find('E'):
    print('pa"s"s')

print('~' * 80)
# * Запросить данные у пользователя и распечатать их используя  форматированную строку.

name = input('Input your name')
print('You are beautiful, {}!!!'.format(name))

print('~' * 80)
# * Распечатать содержимое файла.
f = open('task01.py', encoding="utf8")
ll = f.readlines()
print(ll)

print('~' * 80)
'''
Создать функцию, которая принимает два аргумента, 
вернуть сумму двух аргументов.
'''


def func(aff: float = 1,
         bff: float = 1) -> float:
    return aff + bff


print(func(2, 3))

print('~' * 80)
'''
Создать функцию которая принимает любое количество параметров,
распечаатать эти параметры.
'''


def func1(*args):
    print(args)


func1(5, 6, 98, 74, 25, 12, 36, 1)
