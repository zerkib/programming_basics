"""
Данный модуль содержит следующие функции:
1)file_info принимает один аргумент в формате str и выводит список файлов заданного каталога, с указанием размеров файлов и даты их последней модификации
для корректной работы ввидите путь проверяемого файла вида   r"путь файла"
пример       r"c:\\Users\\user\\Desktop\\дз по оимп"

2)backup принимает два аргумента(str) и выводит путь(str) созданной копии
первый из аргументов это путь к файлу/каталогу резервную копию которой создает функция
второй из аргументов это путь (то где будет хранится копия )
первый и второй аргументы должны имет вид r"c:\\Users\\user\\Desktop\\дз по оимп"

3)print_directory_tree принимает один аргумент(str) и рисует дерево каталогов
аргумент должен иметь вид r"c:\\Users\\user\\Desktop\\дз по оимп"

4)
Функция my_cat() ункция не принимает аргумент
Функция  воспроизводит основные функции команды cat,
объединяет и отображает содержимое нескольких файлов из командной строки.
пример испозования: python my_cat.py file1.txt file2.txt
"""
import os
import datetime 
import sys
#1 Задание
"""
Написать функцию, которая выводит список файлов заданного каталога,
с указанием размеров файлов и даты их последней модификации
"""
def file_info(directory):
    """
    Функция принимает одни аргумент directory(str) 
    Функция выводит список файлов(str) заданного каталога,
    с указанием размеров файлов и даты их последней модификации 
    """
   
    file_info = []
    files = os.listdir(directory)       #получил список файлов

    for index, fil in enumerate (files):        #index- индекс fil-название файла
        file_path = os.path.join(directory, fil)        #соединил путь к документу с его названием
        file_weight = os.path.getsize(file_path)        #вывел вес файла
        last_file_modification = datetime.date.fromtimestamp(os.path.getmtime(file_path))        #вывел дату последней модификации файла
        #files[index] += ' вес = ' + str(file_weight) + '  дата последней модификации =' +  str(last_file_modification)
        file_info.append(f"{fil}  размер = {file_weight} байт, последнее изменение = {last_file_modification} ")
    return file_info


#2 Задание
"""
Написать функцию,
которая создает резервную копию заданного файла/каталога в имени резервной копии
должны использоваться дата и время создания резервной копии
"""
def backup(path, backup_path):
    """
    Функция принимает два аргумента path(str)-то что будет копироватся  
    и backup_path(str)-путь к месту где будет хранится копия
    Функция выводит путь копии
    """

    data_now=(datetime.datetime.now()).strftime('%Y%m%d_%H%M%S')
    back = os.path.join(backup_path, f"{data_now}")
    
    # Проверяет является ли путь файлом
    if os.path.isfile(path):
        #получаем расширение файла
        file_extension = os.path.splitext(path)[1]
        backup_file_path =os.rename( back, os.path.join(backup_path, f"{data_now}{file_extension}"))
        
        os.makedirs(os.path.dirname(backup_file_path), exist_ok=True)  # Создаем директорию для резервной копии
        
        with open(path, 'rb') as f :
            data= f.read()
        with open(backup_file_path, 'wb') as f:
            f.write(data)
    
    # Проверяем является ли путь каталогом
    elif os.path.isdir(path):
        os.makedirs(back, exist_ok=True)      #exist_ok=True позволяет не выбрасывать ошибку если директория уже существует
        
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                backup_file_path = os.path.join(back, item)     # Полный путь для резервной копии файла
                with open(item_path, 'rb') as f:
                    data=f.read()
                with open(backup_file_path, 'wb') as f:
                    f.write(data)
            elif os.path.isdir((item_path)):    #рекурсивно создается копия подкаталоги
                # Рекурсивно создаем резервную копию подкаталога
                backup(os.path.join(path, item), back)
               
    else:
        raise ValueError('Указанный путь не является файлом или каталогом')
    return back

#3
"""
Написать Функцию, которая рисует дерево каталогов заданного каталога
"""
def print_directory_tree(startpath):
    """
    Функция принимает один аргумент startpath(str)-это то откуда начнется древо 
    """
    for root, dirs, files in os.walk(startpath):        #walk для того чтобы пройти по всем файлам и подкаталогам 
        level = root.replace(startpath, '').count(os.sep) #sep испольуется чтобы отформатировать вывод с отступами
        indent = '|' + '-' * 6 * (level + 1)
        print(f'{indent} {os.path.basename(root)}/')
        paragraph_below_line =  ' ' + ' ' * 7 * (level + 1)
        for i in files :
            print(f'{paragraph_below_line} {i}')
    
#4
"""
Написать аналог команды cat (OS Linux)
"""
def  my_cat():
    """
    Функция не принимает аргумент
    Функция  воспроизводит основные функции команды cat,
    объединяет и отображает содержимое нескольких файлов из командной строки.
    """
    if len(sys.argv) < 2:
        print("Использование: python dz_os.py <file1> <file2> ...")        # Проверка, что передано хотя бы одно имя файла
        sys.exit(1)
    for filename in sys.argv[1:]:       # Перебор каждого файла, указанного в аргументах командной строки
        abs_path = os.path.abspath(filename)        # Получение абсолютного пути к файлу
        
        try:
            
            with open(abs_path, 'r') as file:
                print(f"Содержимое {abs_path}:")          # Чтение и вывод содержимого файла
                print(file.read())                          
        except FileNotFoundError:
            print(f"Ошибка: {abs_path} не найден.")
        except IsADirectoryError:
            print(f"Ошибка: {abs_path} является директорией.")
        except Exception as e:
            print(f"Ошибка при чтении {abs_path}: {e}")




if __name__ == "__main__":
    
    #1
    directory = '.'
    file_inf=file_info(directory)
    for i in file_inf:
        print(i)

    #2
    pat1=r"c:\Users\user\Desktop\дз по оимп"
    backup_pat=r"c:\Users\user\Desktop"
    print(backup(pat1, backup_pat))
    
    #3
    pat2=r"E:\Games\Mad Max"
    print(print_directory_tree(pat2))

    #4
    my_cat()