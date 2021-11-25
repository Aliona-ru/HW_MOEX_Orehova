'''
Все решения поместить в файл task03.py и разместить его на github

Создать класс в конструктор которого передается одно число
В этом классе дожен быть метод show, который распечатывает
переданное число.
'''


class Number:

    def __init__(self, numb):
        self.data = numb

    def show(self, numb):
        print(self.data)


n = Number(525)
n.show(n.data)

'''
Создать класс, который наследуется от предыдущего класса и в этот
класс передается два числа.
Данный класс реализует метод calc, который складывает эти два числа.
'''


class Summ(Number):

    def __init__(self, a, b):
        self.sum1 = a
        self.sum2 = b
        self.data = 0

    def calc(self):
        self.data = self.sum1 + self.sum2
        return self.data


s = Summ(-3, 78)
s.show(s.calc())

'''
Создать блок try/except/finally
Внутри блока try создать выражение, которое делит на 0.
Перехватить эту ошибку и распечатать сообщение пользвоателю.
'''

try:
    3 / 0
except ZeroDivisionError:
    print("division by zero!!!")
finally:
    print("be carefully!!!")

'''
Создать декоратор, который перед запуском функции распечатывает все аргументы вызываемой функции.
'''


def print_args(func):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)

    return inner


@print_args
def func_with_args(a1, a2, a3, a4):
    return a1 + a2 + a3 + a4


func_with_args(1, 2, 3, 4)

'''
Создать класс в котором применить декоартор  @property для доступа к внутренней переменной.
'''


class Decor:
    def __init__(self, a, b, c):
        self.data1 = a
        self.data2 = b
        self.data3 = c

    @property
    def get_set_data1(self):
        return self.data1


cl = Decor(55, 44, 33)
print(cl.get_set_data1)

'''
Создать генератор который возвращается числа от 1 до 10
'''


def gen10():
    a = 1
    while a <= 10:
        yield a
        a += 1


for g in gen10():
    print(g)

'''
С помощью стандартной функции collections.namedtuple создать объект для хранения точки в трехмерном пространстве.
'''

import collections

Point3D = collections.namedtuple('Point3D', ['x', 'y', 'z'])

Point1 = Point3D(x=1, y=1, z=1)
Point2 = Point3D(2, 2, 2)
Point3 = (Point1.x + Point2.x, Point1.y + Point2.x, Point1.z + Point2.x)

'''Создать пакет в котором будет функция для распечатки текущей даты (можно использовать пакет datetime).
Для данного пакета подготовить setup.py для установки.
'''
