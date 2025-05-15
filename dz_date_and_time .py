"""
Днанный модуль содержит следующие функции:
2)Функция leap_year() определяет по введенному году является ли он високосным
3)Функция time_count() принимает один аргумент в str виде ,в зависимости от введенного выводятся дни ли часы или минуты
для того чтобы вывести дни введите 'days' для часов 'hours' для минут 'minutes'
4)Функция counting_seconds считает количество секунд с начала эпохи

6)Функция  the_oldest_student принимает список студенов в формате 'surname name dd.mm.yyyy' после выводит список  из самого(самых) стршего(старших) студента(студентов)  
7)Функция принимает список(list) сотрудников в формате 'surname name dd.mm.yyyy' , и выводит список (list) с тем у кого в блишайшее время будет день рождения
8)Функиця  num_of_days_off_per_year определяет количество выходных дней (суббот,воскресений)в зависимости от того является ли год високосным
для вычисления нужно ввести нужный год

"""
import datetime
from datetime import date 


#2 Задача

"""
Написать функцию, которая по переданной ей дате определяет, является ли год этой даты високосным
"""
def leap_year(date:datetime.date):
    """
    функция принимает в качестве параметра дату в строковом формате (str)): yyyy.mm.dd

    возвращает логическое выражение типа boolean является год высокосным или нет
    """
    year = int(date.year)
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


#3 Задача

"""
Вычислить количество дней (часов/минут), прошедших с начала года
"""
def time_count(ddate:str,time:str):
    """
    функция принимает два аргумента:
        ddate - дата время с начала года коорого надо посчитать
        time - что посчитать (пройденные дни, часы, минуты)
        

        возвращает int число пройденных дней, часов, минут.
    """
    current_date = datetime.date(ddate)
    current_date_year = current_date.year
    beginning_of_the_year = datetime.date(current_date_year,1,1)
    days = (current_date-beginning_of_the_year).days
    hours = days*24
    minutes = hours*60


    if time == 'days':
        return days
    elif time == 'hours':
        return hours
    elif time == 'minutes':
        return minutes


#4 Задача

"""
Вычислить количество секунд, прошедших с начала эпохи Unix (1 января 1970).
"""

def counting_seconds():
    """
    Функция ничего не принимает , возвращает str пройденные секунды
    """
    current_date=date.today()
    beginning_of_an_era_Unix=datetime.date(1970,1,1)
    days=(current_date-beginning_of_an_era_Unix).days
    seconds=days*86400
    
    d='С начала эпохи Unix прошло '+ str(seconds)+' секунд '
    return d

#5 Задача

"""
Написать  функцию – русифицированный аналог strftime(), 
которая работает также как strftime(),
только имена дней недели и месяцев выдаёт на русском языке.
"""
def strftime_Rus(dat:datetime.datetime,format:str) -> str:
    """
    Функция возвращает дату типа данных строки в определенном формате
    date(datetime.datetime)-дата которая преобразуется в строку
    form(str)- это формат в который мы преобразуемм введенную дату
    """
    Months = {'January': 'Январь', 'February': 'Февраль', 'March': 'Март', 'April': 'Апрель','May': 'Май','June': 'Июнь','July':'Июль','August': 'Август','September': 'Сентябрь','October': 'Октябрь','November': 'Ноябрь','December': 'Декабрь'}
    
    months = {'Jan': 'Янв','Feb': 'Февр','Mar': 'Март','Apr': 'Апр','May': 'Май','Jun': 'Июнь','Jul': 'Июль','Aug': 'Авг','Sep': 'Сент','Oct': 'Окт','Nov': 'Нояб','Dec': 'Дек'}
    
    Weekdays = {'Monday': 'Понедельник', 'Tuesday': 'Вторник','Wednesday': 'Среда','Thursday': 'Четверг','Friday': 'Пятница','Saturday': 'Суббота','Sunday': 'Воскресенье'}
    
    weekdays = {'Mon': 'Пн','Tue': 'Вт','Wed': 'Ср','Thu': 'Чт','Fri': 'Пт','Sat': 'Сб','Sun': 'Вс'}
    if format == '%A':
        Ru_form = format.replace('%A', Weekdays[dat.strftime('%A')])
    elif format == '%a':
        Ru_form = format.replace('%a', weekdays[dat.strftime('%a')])
    elif format == '%B':
        Ru_form = format.replace('%B', Months[dat.strftime('%B')]) 
    elif format == '%b':
        Ru_form = format.replace('%b', months[dat.strftime('%b')])
   


    return dat.strftime(Ru_form)


#6 Задача


"""

Дан список студентов, содержащий их фамилии, имена и даты рождения (dd.mm.yyyy). Напишите программу, которая будет находить самого старшего студента из этого списка и выводить его фамилию, имя и дату рождения, а если имеется несколько старших студентов с одинаковой датой рождения, то определять их дату рождения и количество.Пример: “ИвановИван 12.09.2000”, и т.д.
"""
def the_oldest_student(list_of_students:list):
    """
    Функция принимает список(list) студентов , и выводит список(list) из самого(самых) стршего(старших) студента(студентов)
    """
    oldest_date=None   
    oldest_students=[]



    for i in list_of_students :
        surname, name, birth_date_str = i.split()
        birth_date = datetime.datetime.strptime(birth_date_str, '%d.%m.%Y')
        if oldest_date is None or birth_date < oldest_date:
            oldest_date = birth_date
            oldest_students = [(surname, name, birth_date_str)]
        elif birth_date == oldest_date :
            oldest_students.append((surname, name, birth_date_str))

    return oldest_students 



#7 Задача
"""
Дан список сотрудников организации с указанием их фамилии, имени и даты рождения.
Администрация ежедневно поздравляет всех сотрудников, родившихся в этот день.
Напишите программу, которая будет определять сотрудника, чей день рождения будет в ближайшие 5 дней от текущей даты. 
Программа должна выводить фамилию, имя и дату рождения сотрудника.
"""

def happy_birthday(list_of_employees:list):
    """
    Функция принимает список(list) сотрудников , и выводит список (list) с тем у кого в блишайшее время будет день рождения
    """
    lst1=[]
    lst4=['день рождения']
    happy=[]

    for i in list_of_employees:
        lst1 += i.split()
    lst2 = lst1[2::3]
    lst3 = [lst1[:3:] , lst1[4:6] , lst1[8:9]]
    
    today = datetime.date.today()
    tuday_year = today.year

    for index, u in enumerate(lst2):
        

        birth_date = datetime.datetime.strptime(u,'%d.%m.%Y')
        birth_date_day = birth_date.day   #вытаскиваем день
        birth_date_month = birth_date.month   #вытаскиваем день
        birth_date_this_year = datetime.date(tuday_year,birth_date_month,birth_date_day) 

        if  today + datetime.timedelta(days=1) <= birth_date_this_year <= today + datetime.timedelta(days=5) :
            happ=  f"{lst3[index]} {lst4[0]} {birth_date.strftime('%d.%m.%Y')}"
            happy.append(happ)
            return happy
        
            


#8 Задача
"""
Для заданного года посчитать количество выходных дней в этом году (то есть количество суббот и воскресений).
"""
def num_of_days_off_per_year(year):
    """
    Функция принимает одну переменную year в формате int , возвращет количество дней
    """
    new_data=datetime.date(year,1,1)
    day_of_the_week=new_data.weekday()
    weekends=0
    if year%4==0 and year%100!=0 or year%400==0:#Если год високосный
        if day_of_the_week in (4,6):
            weekends=53+52#если год начинается спятницы то 53 суббот и 52 воскресений,если год начинается с воскресения то суббот 52 ,воскресений 53
        elif day_of_the_week==5:
            weekends=53+53# воскресений и суббот по 53 дня
        else:  # Начинается с понедельника по четверг
            weekends = 52 + 52
    else:
        if day_of_the_week in (0,1,2,3,4):
            weekends=52+52 #если год начинается с понедельника по пятницу включително то воскресений и суббот по 52 дня
        elif day_of_the_week in (5,6):
            weekends=52+53 #если год начинается с субботы то 53 суббот и 52 воскресений,если год начинается с воскресения то суббот 52 ,воскресений 53
    return weekends


#9 Задача
"""
9.	Написать программу, которая выводит на экран календарь на месяц
 в виде таблицы, столбцами которой являются недели. 
На вход программе подаётся год и месяц или дата.
"""
def my_calendar(year:int,month:int):
    """
    Функция принимает два аргумента year(int) и month(int) и выводит календарть
    """
    counter=0
    dat=datetime.date(year,month,1)
    n = int(dat.strftime('%u'))
    days_of_the_week='  Пн  Вт  Ср  Чт  Пт  Сб  Вс' + '\n' + '    ' * (n-1) 
    print('          ' + strftime_Rus(dat,'%B'))
    
    while int((date(year, month, 1) + datetime.timedelta(counter)).strftime('%m')) == month :
        counter += 1
        
        if counter < 10:
            days_of_the_week += '  ' + ' ' + str(counter)
        else:
            days_of_the_week += '  ' + str(counter)
        if (n + counter - 1) % 7 == 0:
            days_of_the_week += '\n'
    
    return days_of_the_week       


if __name__ == "__main__":

    list_of_student=['Иванов Иван 21.10.2000', 'Петров Петр 20.11.2002','Кирилов Кирил 3.11.2004']
    #5
    print(strftime_Rus(datetime.datetime.today(),'%b'))
    #6
    oldest_students = the_oldest_student(list_of_student)
    for student in oldest_students :
        print("{} {} {}".format(student[0], student[1], student[2]))

    
    #7
    happy_bir=str(happy_birthday(list_of_student))  
    if happy_bir == 'None' :
        print ('В ближайшше время ни у кого нет дня рождения')
    else :
        print ('У', happy_bir)
    #8
    print(num_of_days_off_per_year(2024))
    #9
    print(my_calendar(2024,11))
