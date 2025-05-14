import tkinter as tk
from math import *
from tkinter import font


class Graf:
    def __init__(self, mainm):
        self.mainm = mainm
        mainm.title('наше окно')
        mainm.geometry('650x550')
        mainm.resizable(False,False)

        
        self.offset_x = 0 
        self.offset_y = 0
        self.scale = 20

        self.create_widgets()
        self.create_dpsk()

    def create_widgets(self):
        """
        создает элементы интерфейса
        """
        #поле ввода функции
        tk.Label(master= self.mainm, text = "Функция:").place(x= 25, y=80)
        self.input_field=tk.Entry(master=self.mainm, relief= tk.SUNKEN, borderwidth = 2 , width=25)
        self.input_field.place(x=25, y=100)
        self.input_field.insert(0,"x*x")

        #кнопка для рисования графика
        self.btn_1 =tk.Button(master = self.mainm ,width=20,height=2, text="Построить график",command=self.draw_graph, )
        self.btn_1.place(x=25, y=130)

        #ползунок для масштабирования
        tk.Label(master = self.mainm, text= "Масштаб:").place(x=25 , y =180)
        self.scale_slider = tk.Scale(master=self.mainm , from_ = 5 , to =50,  orient=tk.HORIZONTAL,  command = self.update_scale, length = 200)
        self.scale_slider.set(20)   #начальное значение
        self.scale_slider.place(x =25 , y = 200)


        # Кнопки для перемещения графика
        self.btn_up = tk.Button(master=self.mainm, text="↑", width=5, command=lambda: self.move_graph(0, -1))
        self.btn_up.place(x=75, y=250)

        self.btn_left = tk.Button(master=self.mainm, text="←", width=5, command=lambda: self.move_graph(-1, 0))
        self.btn_left.place(x=25, y=280)

        self.btn_right = tk.Button(master=self.mainm, text="→", width=5, command=lambda: self.move_graph(1, 0))
        self.btn_right.place(x=125, y=280)

        self.btn_down = tk.Button(master=self.mainm, text="↓", width=5, command=lambda:self.move_graph(0, 1) )
        self.btn_down.place(x=75, y=280)

        #холст для рисования
        self.canv = tk.Canvas( master=self.mainm,relief= tk.SUNKEN, borderwidth = 3,width = 400, height = 450,bg='white')
        self.canv.place(x=250, y=100)   
        
        #центр координат 
        self.update_center()
        
    
    def move_graph(self,dx,dy):
        """
        перемещает график на указанное смещение
        """
        self.offset_x += dx
        self.offset_y += dy
        self.draw_graph()

    def update_center(self):
        """
        обновляет центр координат
        """ 
        
        self.center_x = int(self.canv['width'])//2 + self.offset_x * self.scale
        self.center_y = int(self.canv['height'])//2 + self.offset_y * self.scale  


    def update_scale(self,val):
        """
        обработчик изменений масштаба
        """
        self.scale = float(val)
        self.draw_graph()


    def draw_grid(self):
        """
            Рисует сетку на графике
        """
        width = int(self.canv['width'])
        height = int(self.canv['height'])

        #Вертикальные линии сетки(вправо от центра)
        x = self.center_x + self.scale
        while x < width:
            self.canv.create_line(x, 0, x, height, fill='lightgray', dash=(1, 1))
            x += self.scale     
        #Вертикальные линии сетки(влево от центра)
        x = self.center_x - self.scale
        while x > 0:
            self.canv.create_line(x, 0, x, height, fill='lightgray', dash=(1, 1))
            x -= self.scale

        # Горизонтальные линии сетки (от центра вниз)
        y = self.center_y + self.scale
        while y < height:
            self.canv.create_line(0, y, width, y, fill='lightgray', dash=(1, 1))
            y += self.scale
    
        # Горизонтальные линии сетки (от центра вверх)
        y = self.center_y - self.scale
        while y > 0:
            self.canv.create_line(0, y, width, y, fill='lightgray', dash=(1, 1))
            y -= self.scale    

    def drawScale(self, isVertical = True,  length: int =None):
        '''
         рисует шкалу на оси
        '''
        if length is None:
            length = int(self.canv['height'] if isVertical else self.canv['width']) 
        
        scale = self.scale
        if not isVertical:     # отчсечки на горизонтальной оси
            x_shift = (int(self.canv['width'])-length) 
            start = self.center_x - x_shift
            n = (length-start)//scale     # количество отсечек на  положительной части оси x
            m = (start)// scale      # количество отсеек на отрицательной части оси x
            
            for i in range(int(n)):
                self.canv.create_line(self.center_x + i*scale, self.center_y - 5, self.center_x + i*scale,  self.center_y + 5)
                #нумерация отсечек на положительной части оси
                self.canv.create_text(self.center_x + (i+1)*scale  , self.center_y + 15, text = str(i+1))

            for i in range(int(m)):
                self.canv.create_line(self.center_x - i*scale, self.center_y - 5, self.center_x - i*scale,  self.center_y + 5)  
                #нумерация отсечек отрицательной части оси
                self.canv.create_text(self.center_x - (i+1)*scale , self.center_y + 15, text = str(i+1))

            # промежуточные горизонтальные отсечки
            for i in range(int(n * 5)):
                self.canv.create_line(self.center_x + i*(scale/5), self.center_y - 2, self.center_x + i*(scale/5),  self.center_y + 2)
            for i in range(int(m * 5)):
                self.canv.create_line(self.center_x - i*(scale/5), self.center_y - 2, self.center_x - i*(scale/5),  self.center_y + 2)  


        else:     # отчсечки на вертикальной оси
            y_shift = (int(self.canv['height'])-length) 
            start = self.center_y - y_shift
            n = (length-start)//scale     # количество отсеек на отрицательной части оси y
            m = (start)// scale      # количество отсечек на  положительной части оси y
            for i in range(int(n)):
                self.canv.create_line(self.center_x + 5, self.center_y + i*scale, self.center_x -5,  self.center_y + i*scale)
                #нумерация отсечек на  положительной части оси
                self.canv.create_text(self.center_x - 15, self.center_y + (i+1)*scale, text = str(i+1))

            for i in range(int(m)):
                self.canv.create_line(self.center_x + 5, self.center_y - i*scale, self.center_x -5,  self.center_y - i*scale)     
                #нумерация отсечек на  отрицательной части оси
                self.canv.create_text(self.center_x - 15, self.center_y - (i+1)*scale, text = str(i+1) )
            
            # промежуточные вертикальные отсечки
            for i in range(int(n * 5)):
                self.canv.create_line(self.center_x + 2, self.center_y + i*(scale/5), self.center_x - 2,  self.center_y + i*(scale/5))
            for i in range(int(m * 5)):
                self.canv.create_line(self.center_x + 2, self.center_y - i*(scale/5), self.center_x - 2,  self.center_y - i*(scale/5))

    def drawAxe(self, isVertical = True, length: int = None):
        '''
        функция рисует ось координат (горизонтальную или вертикальную)
        '''
        if length is None:
            length = int(self.canv['height'] if isVertical else self.canv['width'])  

        if isVertical:
            y_shift = (int(self.canv['height'])-length) 
            self.canv.create_line(self.center_x, y_shift, self.center_x, y_shift + length, arrow = 'first')
            self.drawScale(True,  length)
        else:
            x_shift =  (int(self.canv['width'])-length)
            
            self.canv.create_line(x_shift, self.center_y, x_shift + length, self.center_y, arrow = 'last')
            self.drawScale(False,  length)
            
        

    def create_dpsk(self):
        '''
            рисует Декартову систему координат на плокости
        '''
        self.draw_grid()
        self.drawAxe()
        
        self.drawAxe( isVertical=0)


    def f(self, x):
        '''
            Вычисляет значение функции
        '''
        try:
            
            expression = self.input_field.get()
            # Заменяем 'x' на текущее значение
            expr = expression.replace('x', f'({x})')
            return eval(expr)
        except:
            return 0

    def draw_graph(self):
        ''' Функция для рисования графика с очисткой холста '''
        self.canv.delete("all")  # Очищаем холст

        self.update_center()
        

        self.create_dpsk() 
        self.draw_func(self.f, -10, 10,  "green")  


    def draw_func(self, func, a: int, b: int, colour = "black"):
        ''' 
            Рисует график функции
        '''
        length = b - a   # длина отрезка
        h = 0.001         # шаг для рисования графика функции
        n = int(length / h)
        
        points = []
        for i in range(n ):
            x = a + i * h
            y = func(x)
            points.append((self.center_x + x * self.scale,self.center_y - y * self.scale))

        if len(points) > 1 :
            self.canv.create_line(points , fill = colour, width = 2 , smooth = True)


if __name__ == "__main__":   

    mainm = tk.Tk()
    app = Graf(mainm)

    mainm.mainloop()