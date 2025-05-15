
#1.    Написать функцию, которая принимает два аргумента. Если аргументы – числа, то возвращает их сумму, а если строки или списки, то возвращает конкатенацию.
'''
def sum_or_concatenation(argument1,argument2):

    """Функция проверяет два аргумента и в случае ели они числа,то суммирует их, противноесли строки или списки,то конкатенирует их"""
    
    if type(argument1) != type(argument2):
       return 'Не возможно выполнить не одно из действий т.к типы аргументов не равны'
    else:
        sum_or_concatenation=argument1+argument2
        return sum_or_concatenation
argument1="asd"
argument2="asd"
print(sum_or_concatenation(argument1,argument2))

'''
#2.	Написать функцию, осуществляющую циклический сдвиг списка на указанное количество шагов и в указанном направлении.
'''
def cyclic_shift(lis:list,number:int):
    """ функция осуществляет циклический сдвиг списка на указанное количество шагов и в указанном направлении.
    направление указывается знаком перед указанным количеством шагов , если - то сдвигается влево , если + то в право"""
    
    length=len(lis)
    
    if number > 0:
        for i in range(number) :
            element = lis.pop(0) # здесь удаляем первый элемент и сохраняем его
            lis.append(element) # добавляем сохраненный элемент в конец списка
    elif number < 0:    
        for i in range(abs(number)) # берем количество отриц. шагов по модулю чтобы их считать:
            element = lis.pop(length - 1) # удаляем последний элемент и сохраняем его
            lis.insert(0, element) # вставляем его на первой позиции
    return lis
lis=[1,2,3,4]
number=-2
print(cyclic_shift(lis,number))
'''

#3.	Написать функцию, вычисляющую число размещений без повторений  .
'''
def calculation_placements(methods,quantity_elements):
    """ Функция считает сколько можно построить векторов используя число способов и количество различных элементов исползуя формулу n!/(n-k)!"""
    factorial_quantity_elements=1#Счетчик
    for i in range(2,quantity_elements+1):
        factorial_quantity_elements*=i

    difference=quantity_elements-methods

    factorial_difference=1#Счетчик
    for i in range(2,difference+1):
        factorial_difference*=i
    calculation=factorial_quantity_elements/factorial_difference
    return calculation
methods=int(input('Введите количество способов k='))
quantity_elements=int(input('Введите количество различных элементов n='))
print(calculation_placements(methods,quantity_elements))
'''

#4.	Написать функцию, вычисляющую число сочетаний  .
'''
def ccalculation_combinations(methods,quantity_elements):
    """ Функция считает число способов сколькими можно из различных лементов выбрать скоько то штук без учета порядка"""
    factorial_quantity_elements=1#Счетчик
    for i in range(2,quantity_elements+1):
        factorial_quantity_elements*=i

    difference=quantity_elements-methods

    factorial_difference=1#Счетчик
    for i in range(2,difference+1):
        factorial_difference*=i

    factorial_methods=1#Счетчик
    for i in range(2,methods+1):
        factorial_methods*=i
    calculation=factorial_quantity_elements/(factorial_methods*difference)   
    return calculation
methods=int(input('Введите количество способов k='))
quantity_elements=int(input('Введите количество различных элементов n='))
if quantity_elements<methods:
    print('k не может быть больше n')
else:
    print(ccalculation_combinations(methods,quantity_elements))
'''

#5.	Написать программу, выводящую в консоль треугольник Паскаля.
'''
def pascal_triangle(term):
    """Функция создает треугольрник паскаля , """
    term=[1] + term 
    for i in range (1,len(term)-1):
        term[i]+=term[i+1]
    return term
degree=int(input('Введите степень для создания треугольника паскаля:'))
term=[]
for i in range(degree):
    term=pascal_triangle(term)
    print(term)
'''