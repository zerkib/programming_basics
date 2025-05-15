#1 Задание
'''
"""Написать функцию, которая создает файл, содержащий 10 строк из 30 цифр и букв. (цифры или буквы зависит от параметра)"""
def file_creator(file_name,character_type):
    """Функция создает файл из 10 строк и 30 символов
    символы могут быть буквами или цифрами в зависмоти от их типа"""
    string_of_numbers=''
    file= open(file_name,"w")
    for i in range(30):
        string_of_numbers +=str(i) #Создается строка из чисел
    for _ in range(10):
        if character_type =='nums':
            file.write(string_of_numbers+'\n')
        elif character_type =='string':
            file.write(('a'*30) + '\n')
    file.close()
file_creator('test_file.txt','string')
'''
#2 Задание
'''
"""Считать из файла input.txt 10 чисел (числа записаны через пробел). Затем записать их произведение в файл output.txt."""
def product_of_num(input_file,output_file):
    """ Функция открывает файл считывает числа и сохраняет их произведения в другой файл"""
    file1=open(input_file,"r")
    s=file1.read()
    file2=open(output_file, "w")
    prod_num=1
    t=''#временная переменная 
    for i in s:
        if i.isdigit():
            t+=i
        else:
            if t !='':
               prod_num*=int(t)
               t=''
    file2.write(str(prod_num))
    file1.close()
    file2.close()
product_of_num('input.txt','output.txt')
'''
#3 Задание
'''
"""В файле записаны целые числа. Найти максимальное и минимальное число и записать в другой файл"""
def min_max__num(input_file,output_file):
    """Функция ищет из одного файла минимальное и максимальное натуральное число и записывает их в другой файл """
    file1=open(input_file,"r")
    s=file1.read()
    file2=open(output_file, "w")
    lst=[]
    t=''#временная переменная
    for i in s:
        if i.isdigit():
            t+=i
        else:
            if t !='':
                lst.append(int(t))
                t=''
    max_num=max(lst)
    min_num=min(lst)
    file2.write(str(max_num)+'\n'+str(min_num))
    file1.close()
    file2.close()
min_max__num('input.txt','output.txt')
'''
#4 Задание
# не знаю как сделать

#5 Задание
'''
"""Дан файл, состоящий из цифр и других символов.  Подсчитать сумму чисел этого файла"""
def sum_num(input_file):
    """Функция проверяет является ли символ находящийся в файле числом,посел суммирует все числа """
    file1=open(input_file,"r")
    s=file1.read()
    counter=0
    t=''#временная переменная
    for i in s :
        if i.isdigit():
            t+=i
        else:
            if t !='':
                counter+=int(t)
                t=''
    file1.close()
    return counter
print('Сумма =',sum_num('input.txt'))
'''
#Лдгу4р874ер4ш5г5з98н56зш он65 89н5486зн5г9 -текст для файла input.txt
#НЕ РАБОТАЕТ