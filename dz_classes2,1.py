
import math
import tkinter as tk
from tkinter import messagebox
#1
"""
Создать абстрактный класс Figure (на плоскости) с методами вычисления пло-щади и периметра,
а также методом, выводящим информацию о фигуре на экран.
Создать подклассы: Rectangle (прямоугольник), Circle (круг), Triangle (треугольник) со своими методами вычисления площади и периметра.
Создать список из n фигур и вывести полную информацию о фигурах на экран.

"""
class Figure:      
    def area(self):
        """
        метод для вычисление площади (он должен быть переопределен в подклассах)
        """
        raise NotImplementedError("Метод area()должен быть переопределен в подклассах")
    
    def perimeter(self):
        """
        метод длф вычисление периметра (он должен быть переопределен в подклассах)
        """
        raise NotImplementedError("Метод perimeter()должен быть переопределен в подклассах")
    
    def display_info(self):
        """
        метод для вывода информации о фигуре (он должен быть переопределен в подклассах)
        """
        raise NotImplementedError("Метод perimeter()должен быть переопределен в подклассах")
    
class Rectangle(Figure):        #подкласс Rectangle(прямоугольник)
    def __init__(self,width,height,x,y):
        self.width = width
        self.height = height
        self.x = x      #x координата верхнего левого угла
        self.y = y      #y координата верхнего левого угла
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def display_info(self):
        print(f" Прямоугольник : ширина = {self.width}, высота = {self.height}")
        print(f" Площадь  : {self.area()}")
        print(f" Периметр : {self.perimeter()}")
        print()     # для промежутка

    def draw(self,canv,scale =1):      #рисуем квадрат
        scaled_width = self.width *scale
        scaled_height = self.height * scale
        scaled_x = self.x *scale
        scaled_y = self.y * scale
        canv.create_rectangle(scaled_x,scaled_y,scaled_x + scaled_width,scaled_y + scaled_height,outline="black")

class Circle(Figure):       #подкласс Circle(круг)
    def __init__(self,radius,x,y):
        self.radius = radius
        self.x = x      #x координата центра круга
        self.y = y      #y координата центра круга

    def area(self):
        return math.pi * self.radius ** 2 
    
    def perimeter(self):
        return  2 * math.pi * self.radius
    
    def display_info(self):
        print(f" Круг    : радиус = {self.radius}")
        print(f" Площадь : {self.area()}")
        print(f" Периметр (длина окружности): {self.perimeter()}")
        print()     # для промежутка

    def draw(self,canvas,scale=1):      #рисуем круг
        scaled_radius = self.radius *scale
        scaled_x = self.x *scale
        scaled_y = self.y * scale
        canvas.create_oval(scaled_x - scaled_radius,scaled_y -scaled_radius, scaled_x + scaled_radius,scaled_y + scaled_radius, outline = "black")

class Triangle(Figure):         #подкласс Triangle(треугольник)
    def __init__(self,x1,y1,x2,y2,x3,y3):
        """
        инициализация по координатам трех вершин
        """
        self.x1,self.y1 = x1,y1
        self.x2,self.y2 = x2,y2
        self.x3,self.y3 = x3,y3

        self.side1 = self.calc_lenght(x1,y1,x2,y2)
        self.side2 = self.calc_lenght(x2,y2,x3,y3)
        self.side3 = self.calc_lenght(x3,y3,x1,y1)

        if not self.the_triangle_ex():
            raise ValueError("треугольник с такими сторонами не существует")
        
    def calc_lenght(self,x1,y1,x2,y2):
        """
        вычисляет длину стороны
        """
        return math.sqrt((x2 - x1)**2 +(y2 - y1)**2)


    def the_triangle_ex(self):
        """
        проверяет существование треугольника
        """
        return (self.side1 + self.side2 > self.side3 and self.side1 + self.side3 > self.side2 and self.side2 + self.side3 > self.side1)
    

    def area(self):
        #Формула Герона
        s =self.perimeter() / 2
        return math.sqrt(s* (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    
    def display_info(self):
        print(f" Треугольник с вершинами : A ({self.x1},{self.y1}),B ({self.x2},{self.y2}),C ({self.x3},{self.y3}),")
        print(f"Длины сторон : {self.side1:.2f},{self.side2:.2f},{self.side3:.2f},")
        print(f" Площадь  : {self.area()}")
        print(f" Периметр : {self.perimeter()}")
        print()     # для промежутка

    def draw(self,canvas,scale =1):      #рисуем треугольник по заданным вершинам
        scaled_x1 = self.x1 *scale
        scaled_y1 = self.y1 * scale
        scaled_x2= self.x2 *scale
        scaled_y2 = self.y2 * scale
        scaled_x3 = self.x3 *scale
        scaled_y3 = self.y3 * scale
        
        canvas.create_polygon(scaled_x1,scaled_y1, scaled_x2,scaled_y2 , scaled_x3,scaled_y3, outline ="black",fill="",width= 2  )
        





#2
"""
Составить описание класса для вектора,
заданного координатами его концов в трехмерном пространстве.
Реализовать операции сложения и вычитания векто-ров, 
результатом которого является вектор,
а также вычисления скалярно-го произведения двух векторов,
длины вектора, косинуса угла между двумя век-торами.

"""


class Vector:
    def __init__(self,x1,y1,z1,x2,y2,z2):
        """
        инициализирает координаты вектора
        x1,y1,z1 :коодинаты начала вектора
        x2,y2,z2 :координаты конца вектора
        """
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2 
        self.z2 =z2 

    def coord(self):
        """
        находит координаты вектора и возвращает их кортежом
        """
        return ( self.x2 - self.x1, self.y2 -self.y1 , self.z2 - self.z1)
    
    def __add__(self,other):
        """
        сложение двух векторов
        other : другой вектор
        """
        x1,y1,z1 = self.coord()
        x2,y2,z2 = other.coord()
        return Vector(0,0,0,x1+x2,y1+y2,z1+z2)
    def __sub__(self,other):
        """
        вычитание двух векторов
        other : другой вектор
        """
        x1,y1,z1 = self.coord()
        x2,y2,z2 = other.coord()
        return Vector(0,0,0,x1-x2,y1-y2,z1-z2)
    
    def scalar_product(self,other):
        """
        вычисляется скалярное произведение двух векторов
        other : другой вектор
        """
        x1,y1,z1 = self.coord()
        x2,y2,z2 = other.coord()
        return x1*x2+y1*y2+z1*z2
    def lengtV(self):
        """
        вычисление длины вектора

        """
        x,y,z = self.coord()
        return math.sqrt(x**2+y**2+z**2)
    
    def cosV(self,other):
        """
        нахождение косинуса угла между двумя векторами
        other : другой вектор
        """
        scal=self.scalar_product(other)
        len1=self.lengtV()
        len2=other.lengtV()
        return scal/(len1*len2)
    
    def draw (self,canvas , color = "black",scale =50 ,x_offset=500,y_offset=400):
        """
        рисует вектор
        canvas:холст для рисования
        color :цвет вектора
        scale:масштаб
        x_offset : смешение по x
        y_offset : смешение по y
        """
        x1 = self.x1 * scale + x_offset
        y1 = -self.y1 * scale + y_offset  
        x2 = self.x2 * scale + x_offset
        y2 = -self.y2 * scale + y_offset
        
        # Рисуем вектор со стрелкой
        canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, fill=color, width=2)
        
        # Подписываем вектор
        vec_x, vec_y, _ = self.coord()
        canvas.create_text((x1+x2)/2, (y1+y2)/2 - 10,text=f"({vec_x:.1f}, {vec_y:.1f})",fill=color)


    def __str__(self):
        """
        возвращаем строковое представление вектора
        """
        x,y,z = self.coord()
        return f"вектор : ({x},{y},{z})"

#функция для рисования осей координат
def draw_axes (canvas,width,height,step = 50,scale=1):
    """
    step :шаг шкалы = 50 пикселей
    рисует оси координат
    """
    center_x ,center_y = width //2,height//2
    scaled_step =int( step *scale)

    # ось Оx
    canvas.create_line(0,center_y ,width ,center_y ,fill="black",width =1 ,arrow = tk.LAST)
    canvas.create_text(width - 20,center_y -10, text="X")  
    #Ось Оy
    canvas.create_line(center_x , height, center_x ,0 , fill="black",width =1 ,arrow = tk.LAST)
    canvas.create_text(center_x+10,10, text="Y")

    #сентр координат
    canvas.create_text(center_x +10 , center_y +10 , text = "0")


    # Ось X
    canvas.create_line(0, center_y, width, center_y, fill="black", width=1, arrow=tk.LAST)
    canvas.create_text(width - 20, center_y - 10, text="X")
    
    # Ось Y
    canvas.create_line(center_x, height, center_x, 0, fill="black", width=1, arrow=tk.LAST)
    canvas.create_text(center_x + 10, 10, text="Y")
    
    canvas.create_text(center_x + 10, center_y + 10, text="0")

    # шкала на положительной оси Ox
    x = center_x + scaled_step
    while x < width:  
        canvas.create_line(x, center_y - 5, x, center_y + 5, fill="black")
        canvas.create_text(x, center_y + 15, text=str((x - center_x) // scaled_step))
        x += scaled_step
    # шкала на отрицательной оси Ox    
    x = center_x - scaled_step
    while x > 0:  
        canvas.create_line(x, center_y - 5, x, center_y + 5, fill="black")
        canvas.create_text(x, center_y + 15, text=str((x - center_x) // scaled_step))
        x -= scaled_step

    #шкала на положительной оси Oy
    y = center_y + scaled_step
    while y < height:  
        canvas.create_line(center_x - 5, y, center_x + 5, y, fill="black")
        canvas.create_text(center_x - 20, y, text=str((center_y - y) // scaled_step))
        y += scaled_step
    #шкала на отрицательной оси Oy    
    y = center_y - scaled_step
    while y > 0:  
        canvas.create_line(center_x - 5, y, center_x + 5, y, fill="black")
        canvas.create_text(center_x - 20, y, text=str((center_y - y) // scaled_step))
        y -= scaled_step


    
    

if __name__ == "__main__":
    mainm = tk.Tk()
    mainm.title('наше окно')
    mainm.geometry('1000x800')
    width,height = 1000,800
    canvas = tk.Canvas(mainm, width = width, height = height,bg='white')
    canvas.pack()

    scale =0.5

    

    
    #1
    try:                                                                                                                #Вершина A                Вершина C               Вершина B           
        figures = [ Rectangle(100, 50,width//2 + 50,height // 2 -25), Circle(40,width //2 +150,height//2 -100), Triangle(width//2, height//2-100, width//2-300,height-30,width//2 +100,height//2+100)]
    except ValueError as e:
        print(e)
    for figure in figures:
        figure.display_info()
        
    draw_axes(canvas , width , height,step = 50, scale = scale)
    for figure in figures :
        figure.draw(canvas,scale = scale)
    

     #2
    
    vect1 = Vector(0,0,0,1,2,3)
    vect2 = Vector(0,0,0,3,4,5)
    
    print("вектор 1 :",vect1)
    print("вектор 2 :",vect2)

    #сложение векторов

    vect3 = vect1 +vect2
    print("сумма векторов  :",vect3) 

    #вычитание векторов   
    vect3 = vect1 -vect2
    print("разность векторов  :",vect3) 

    #скаярное произведение
    scal = vect1.scalar_product(vect2)
    print("скаляное произведение :",scal)

    #длина вектора
    len1 = vect1.lengtV()
    len2 = vect2.lengtV()
    print("длина вектора 1 :",len1)
    print("длина вектора 2 :",len2)

    #косинус угла между векторами
    cos =vect1.cosV(vect2)
    print("Косинус угла меду векторами",cos)

    #рисуем векторы
    vectors = [vect1,vect2,vect1+vect2]
    colors = ["red", "green", "blue"]
    for i, vector in enumerate(vectors):
        vector.draw(canvas, color=colors[i], scale=50*scale, 
                   x_offset=width//2, y_offset=height//2)

    
    
    mainm.mainloop()