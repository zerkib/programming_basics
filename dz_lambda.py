
lst=['asdfb','zfghfj','abgffsg']
lst_num=[10,7,9]
lst_num2=[5,6,1]
lst_num3=[4,5,3]
'''
#1 задание
"""Функция проверяет находится ли b в списке с помощью фильтра и лямбды"""
new_list=list(filter(lambda x: 'b' in x, lst))
print (new_list)
"""функция проверяет находится ли b в списке с помощью генератра списков"""
new_list=[lst[i] for i in range(len(lst)) if 'b' in lst[i]]
print(new_list)
'''
'''
#2 Задание
"""Функция переводит сиволы спсика в верхний регистр"""
new_list=list(map(lambda x: x.upper()  , lst))
print(nes_list)
"""Функция переводит символы спсика в верхний регистр"""
new_list=[i.upper() for i in lst ]
print(new_list)
'''
'''
#3 Задание
"""Функция выводит сумму квадратов соответствующих элементов с помощью map и lambda"""
new_list=list(map(lambda x,y: (x**2)+(y**2),lst_num,lst_num2))
print(new_list)
""" Функция выводит сумму квадратов соответствующих элементов """
new_list=[lst_num[i]**2 + lst_num2[i]**2 for i in range(min(len(lst_num2), len(lst_num)))]
print(new_list)
'''
'''
#4 Задание
sides1 = [3, 4, 5, 1, 1, 7]
sides2 = [4, 5, 6, 1, 2, 2]
sides3 = [5, 6, 7, 3, 3, 8]
perimeters = list(map(lambda a, b, c: a + b + c if (a + b > c) and (a + c > b) and (b + c > a) and a > 0 and b > 0 and c > 0 else 0,sides1, sides2, sides3))
print(perimeters)
'''
'''
#5 Задание
"""Функция выводит список составленный из остатков от деления элементов первого списка на соответсвующие элементы второго с помощью map и lambda """
new_list=list(map(lambda x,y: x%y,lst_num,lst_num2))
print(new_list)
"""Функция выводит список составленный из остатков от деления элементов первого списка на соответсвующие элементы второго"""
new_list=[lst_num[i] % lst_num2[i] for i in range(min(len(lst_num),len(lst_num2)))]
print (new_list)
'''
'''
#6 Задание
"""Функция сравнивает элементы первого и второго списка потом составляет список из повторяющихся элементов """
new_list=list(filter(lambda x,: x in lst_num2  , lst_num,))
print(new_list)
"""функция сравнивает элементы первого и второго списка потом составляет список из повторяющихся элементов """
new_list=[i for i in lst_num if i in lst_num2 ]
print(new_list)
'''
'''
#7 Задание
"""Функция сравнивает элементы первого и второго списка потом составляет список з не повторяющихся элементов"""
new_list=list(filter(lambda x : x not in lst_num2 , lst_num))
print(new_list)
"""Функция сравнивает элементы первого и второго списка потом составляет список з не повторяющихся элементов"""
new_list=[i for i in lst_num if i not in lst_num2 ]
print(new_list)
'''
'''
#8 Задание
list_of_natural_num=[2,64,88,17,45]
def natural_num (natural):
    """еси число простое то функция возвращает 1 в противном случае 0"""
    for i in range (2,int(natural**0.5)+1):
        if natural%i==0:
            return 0
    return 1
"""Выводится простое число с помощью filter и функции natural_num"""
new_list=list(filter(natural_num,list_of_natural_num))
print(new_list)
"""Выводится простое число"""
new_list=[i for i in list_of_natural_num if natural_num(i)]
print(new_list)
'''