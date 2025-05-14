
import tkinter as tk
from tkinter import filedialog, messagebox , font


class TextEditor:
    def __init__(self, mainm):
        self.mainm = mainm
        mainm.title('Текстовый редактор')
        mainm.geometry('800x600')



        #Начтройки шрифта по умолчанию
        self.current_font_family = "Arial"
        self.current_font_size = 12

        #создаем текстовое поле с ползунком для прокрутки
        self.text_area = tk.Text(self.mainm , wrap = "word", undo = True , font = (self.current_font_family, self.current_font_size))
        self.scrollbar = tk.Scrollbar(self.mainm, command = self.text_area.yview)
        self.text_area.configure(yscrollcommand= self.scrollbar.set)
       

        #Панель инстументов для шрифтов
        self.toolbar = tk.Frame(self.mainm)
        self.toolbar.pack(side = "top" , fill= "x")

        #выбор шрифта
        self.font_family = tk.StringVar(self.mainm)
        self.font_family.set(self.current_font_family)
        self.font_family_dropdown = tk.OptionMenu(self.toolbar, self.font_family, *font.families(), command=self.change_font)
        self.font_family_dropdown.pack(side="left", padx=5)
        
        # Выбор размера шрифта
        self.font_size = tk.IntVar(mainm)
        self.font_size.set(self.current_font_size)
        self.font_size_spinbox = tk.Spinbox(self.toolbar, from_=8, to=72, textvariable=self.font_size, width=5, command=self.change_font)
        self.font_size_spinbox.pack(side="left", padx=5)
        
        # Кнопки для стилей шрифта
        self.bold_btn = tk.Button(self.toolbar, text="Ж", command=self.toggle_bold)
        self.bold_btn.pack(side="left", padx=5)
        
        self.italic_btn = tk.Button(self.toolbar, text="К", command=self.toggle_italic)
        self.italic_btn.pack(side="left", padx=5)

        #прикрепляем элементы к экрану
        self.scrollbar.pack(side = "right", fill ="y")
        self.text_area.pack(side = "left", fill = "both", expand= True)
       
        #создаем меню
        self.create_menu()
       
        #переменная для хранения текущего файла
        self.current_file = None

        #переменные для стилей шрифта
        self.is_bold = False
        self.is_italic = False


    def create_menu(self):
        """
            Создает меню с пунктами "Файл", "Правка" и "Шрифт".  
            Настраивает горячие клавиши для быстрого доступа к функциям.
        """
        menubar = tk.Menu(self.mainm)

        #"Файл"
        file_menu = tk.Menu(menubar , tearoff = 0)
        file_menu.add_command(label = "Новый", command= self.new_file, accelerator= "CTRL+N")
        file_menu.add_command(label = "Открыть", command=self.open_file , accelerator= "Ctrl+O")
        file_menu.add_command(label = "Сохранить",command=self.save_file, accelerator= "Ctrl+S")
        file_menu.add_command(label = "Сохранить как",command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.exit_editor)
        menubar.add_cascade(label="Файл", menu = file_menu)

        #  "Правка"
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Отменить", command=self.text_area.edit_undo, accelerator="Ctrl+Z")
        edit_menu.add_command(label="Повторить", command=self.text_area.edit_redo, accelerator="Ctrl+Y")
        edit_menu.add_separator()
        edit_menu.add_command(label="Вырезать", command=self.cut_text, accelerator="Ctrl+X")
        edit_menu.add_command(label="Копировать", command=self.copy_text, accelerator="Ctrl+C")
        edit_menu.add_command(label="Вставить", command=self.paste_text, accelerator="Ctrl+V")
        edit_menu.add_separator()
        edit_menu.add_command(label="Выделить все", command=self.select_all, accelerator="Ctrl+A")
        menubar.add_cascade(label="Правка", menu=edit_menu)
        
        #"Шрифт"
        font_menu = tk.Menu(menubar , tearoff = 0)
        font_menu.add_command(label="Изменить шрифт", command=self.show_font_dialog)
        font_menu.add_command(label="Увеличить размер", command=self.increase_font_size, accelerator= "Ctrl++")
        font_menu.add_command(label="Уменьшить размер", command=self.decrease_font_size, accelerator= "Ctrl+-")
        menubar.add_cascade(label= "Шрифт",menu = font_menu)
        
        
        
        # Устанавливаем меню в главное окно
        self.mainm.config(menu=menubar)
        
        
        #  горячие клавиши
        self.text_area.bind("<Control-n>", lambda event: self.new_file())
        self.text_area.bind("<Control-o>", lambda event: self.open_file())
        self.text_area.bind("<Control-s>", lambda event: self.save_file())
        self.text_area.bind("<Control-a>", lambda event: self.select_all())
        self.text_area.bind("<Control-x>", lambda event: self.cut_text())
        self.text_area.bind("<Control-c>", lambda event: self.copy_text())
        self.text_area.bind("<Control-v>", lambda event: self.paste_text())
        self.text_area.bind("<Control-plus>", lambda event: self.increase_font_size())
        self.text_area.bind("<Control-minus>", lambda event: self.decrease_font_size())
        self.text_area.bind("<Control-y>", lambda event: self.text_area.edit_redo())


    def change_font(self, *args):
        """
            Изменяет шрифт текстового поля на основе текущих настроек (семейство, размер, жирность, курсив).  
        """
        new_font = (self.font_family.get(), self.font_size.get())
        if self.is_bold:
            new_font += ("bold",)
        if self.is_italic:
            new_font += ("italic",)
        
        self.text_area.configure(font=new_font)


    def toggle_bold(self):
        """
            Переключает жирность текста.  
            Обновляет кнопку и применяет изменения к шрифту.
        """
        self.is_bold = not self.is_bold
        self.change_font()
        self.bold_btn.config(relief="sunken" if self.is_bold else "raised")
    
    def toggle_italic(self):
        """
            Переключает курсив текста.  
            Обновляет кнопку и применяет изменения к шрифту
        """
        self.is_italic = not self.is_italic
        self.change_font()
        self.italic_btn.config(relief="sunken" if self.is_italic else "raised")
    
    def increase_font_size(self):
        """
            Увеличивает размер шрифта на 1 пункт.
        """
        self.font_size.set(self.font_size.get() + 1)
        self.change_font()
    
    def decrease_font_size(self):
        """
            Уменьшает размер шрифта на 1 пункт 
        """
        if self.font_size.get() > 8:
            self.font_size.set(self.font_size.get() - 1)
            self.change_font()
    
    def show_font_dialog(self):
        """
            Открывает диалоговое окно для выбора шрифта, размера и стилей (жирный, курсив).  
        """
        font_window = tk.Toplevel(self.mainm)
        font_window.title("Выбор шрифта")
        
        tk.Label(font_window, text="Шрифт:").grid(row=0, column=0, padx=5, pady=5)
        font_family = tk.StringVar(font_window)
        font_family.set(self.current_font_family)
        font_dropdown = tk.OptionMenu(font_window, font_family, *font.families())
        font_dropdown.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(font_window, text="Размер:").grid(row=1, column=0, padx=5, pady=5)
        font_size = tk.IntVar(font_window)
        font_size.set(self.current_font_size)
        spinbox = tk.Spinbox(font_window, from_=8, to=72, textvariable=font_size, width=5)
        spinbox.grid(row=1, column=1, padx=5, pady=5)
        
        bold_var = tk.IntVar(font_window)
        bold_check = tk.Checkbutton(font_window, text="Жирный", variable=bold_var)
        bold_check.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        
        italic_var = tk.IntVar(font_window)
        italic_check = tk.Checkbutton(font_window, text="Курсив", variable=italic_var)
        italic_check.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
        def apply_font():
            self.current_font_family = font_family.get()
            self.current_font_size = font_size.get()
            self.is_bold = bool(bold_var.get())
            self.is_italic = bool(italic_var.get())
            self.change_font()
            font_window.destroy()
        
        tk.Button(font_window, text="Применить", command=apply_font).grid(row=4, column=0, columnspan=2, pady=10)


    def new_file(self):
        """
            Создает новый файл, очищая текстовое поле
        """
        self.text_area.delete(1.0, tk.END)
        self.current_file = None
        self.mainm.title("Текстовый редактор - Новый файл")
    
    def open_file(self):
        """
           Открывает файл через диалоговое окно и загружт его содержимое в текстовое поле 
        """
        file_path = filedialog.askopenfilename(filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(1.0, file.read())
                self.current_file = file_path
                self.mainm.title(f"Текстовый редактор - {file_path}")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось открыть файл: {e}")
    
    def save_file(self):
        """
            Сохраняет текущий файл. Если файл не выбран, вызывает save_as_file()
        """
        if self.current_file:
            try:
                with open(self.current_file, "w", encoding="utf-8") as file:
                    file.write(self.text_area.get(1.0, tk.END))
                messagebox.showinfo("Сохранение", "Файл успешно сохранен!")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")
        else:
            self.save_as_file()
    
    def save_as_file(self):
        """
            Сохраняет файл с новым именем через диалоговое окно  
        """
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(self.text_area.get(1.0, tk.END))
                self.current_file = file_path
                self.mainm.title(f"Текстовый редактор - {file_path}")
                messagebox.showinfo("Сохранение", "Файл успешно сохранен!")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")
    
    def exit_editor(self):
        """
            Закрывает редактор
        """
        if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):
            self.mainm.destroy()
    
    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")
    
    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")
    
    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")
    
    def select_all(self):
        self.text_area.tag_add("sel", "1.0", tk.END)
    
   
        
if __name__ == "__main__":   

    mainm = tk.Tk()
    app = TextEditor(mainm)

    mainm.mainloop()