
#1.	Написать функцию, для поиска минимума двух чисел.
'''
def search_for_min_2(d,f):
    """Функция ищет минимальное из дух чисел"""
    if d<f:
        return d
    else d>f:
        return f
z=int(input('Введите число:'))
x=int(input('Введите число:'))
print('Минимальное из двух введенных чисел это-',search_for_min_2(z,x))
'''
# 2.Написать функцию, для поиска максимума трёх чисел.
'''
def search_for_max_3(d,f,g):
    """Функция ищет максимальное из трех чисел """
    if d>f and d>g:
        return d
    elif f>g and f>d:
        return f
    elif g>d and g>f:
        return g
z=int(input('Введите число:'))
x=int(input('Введите число:'))
c=int(input('Введите число:'))
print('Максимальное из трех введенных чисел это-',search_for_max_3(z,x,c))
'''

#3.	Написать функцию для суммирования чисел списка.
'''
def sum_num_list(num_list):
    """ Функция ищет сумму чисел из списка"""
    s=0
    for i in num_list:
        s+=i
    return s
a=[] #список
print('Введите элементы списка.Для завершения нажмите 0:')
while 1:
    s= int(input('Введите элементы списка:'))
    if s==0:
        break
    else:
        a+=[s]
print('Сумма всех чисел списка=',sum_num_list(a))
'''

#4.	Написать функцию для перемножения чисел списка.
'''
def product_of_num_in_list(num_list):
    """Функция перемножает числа из списка """
    s=0
    for i in num_list:
        s*=i
    return s
a=[] #список
print('Введите элементы списка.Для завершения нажмите 0:')
while 1:
    s= int(input('Введите элементы списка:'))
    if s==0:
        break
    else:
        a+=[s]
print('Произведение всех чисел списка=',product_of_num_in_list(a))
'''

#5.	Написать функцию для обращения строки.
'''
def str_revers(string):
    """ Функция обращает строку"""
    string=string[::-1]
    return string
string="asdf1234"#строка
print(str_revers(string))
'''
#6.	Написать функцию для вычисления факториала числа. 
# Функция принимает число в качестве аргумента.
'''
def factorial_calculation(number):
    """ Функция вычисляет факториал"""
    c=1#Счетчик
    for i in range(2,number+1):
        c*=i
    return c
number=int(input('Введите число :'))
print('Факториал числа=',factorial_calculation(number))
'''
#7.	Написать функцию проверки, находится ли число в заданном диапазоне.
'''
def number_in_range(number,start,end):
    """ Функция ищет число в заданном диапазоне"""
    if start<=number<=end:
        return True
    else:
        return False
number=int(input('Введите число для проверки:'))
start=int(input('Введите начало диапазона:'))
end=int(input('Введите конец диапазона:'))
print('Выводится True значит число в заданном диапазоне,в противном случае False:')
print(number_in_range(number,start,end))
'''
#8.	Написать функцию, которая суммирует все целые числа
#  в указанном диапазоне от start до end. 
# Если start больше чем end, то поменять их местами.
'''
def sum_num_in_range(start,end):
    """ Функция суммирует все целые числа в заданном диапазоне"""
    s=0
    if end>start:
        for i in range(start,end+1):
            s+=i
    else:
        for i in range(end,start+1):
            s+=i
    return s
start=int(input('Введите начало диапазона:'))
end=int(input('Введите конец диапазона:'))
print('Сумма =',sum_num_in_range(start,end))
'''
