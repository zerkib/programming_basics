from PySide6.QtWidgets import QApplication
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox
import sys
from main_window import Ui_MainWindow

import hashlib

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bt_confirm.clicked.connect(self.save_user)
        self.bt_cancel.clicked.connect(self.exit);
        self.invalid_message = ""
    
    def save_user(self):
        if self.validate():
             user_type = None
             with open("db.txt", "a") as file:
                 if self.admin_radio.isChecked():
                     user_type = "Admin"
                 else:
                     user_type = "User"
                 hashed_pass = hashlib.sha256(self.ed_password.text().encode())
                 
                 file.write(self.ed_username.text() + " " + hashed_pass.hexdigest() + " " + user_type + "\n") # сохраняем в файл
                 QMessageBox.information(self, "success", "you are registered")
                 self.ed_username.setText("")
                 self.ed_password.setText("")
                 self.ed_confirm_pass.setText("")
        else:
            QMessageBox.warning(self, "error", self.invalid_message)
    
    
        
            
    def validate(self):
        if len(self.ed_username.text()) == 0:
            self.invalid_message = "Вы не ввели имя, попробуйте снова"
            return False
        if len(self.ed_password.text()) < 8:
            self.invalid_message = "Ваш пороль слишком короткий, попробуйте ещё раз"
            return False
        if self.ed_password.text() != self.ed_confirm_pass.text():
            self.invalid_message = "Пароли не не совподают, попробуйте ещё раз"
            return False
        if not self.admin_radio.isChecked() and not self.user_radio.isChecked():
            self.invalid_message = "Вам следует выбрать тип пользователя , попробуйте еще раз"
            return False
        if ' ' in self.ed_username.text():
            self.invalid_message = "Вы не должны использовать пробелы в имени пользователя"
            return False
        with open("db.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                username = line.split(' ')[0]
                if self.ed_username.text() == username:
                    self.invalid_message = "Это имя уже используется"
                    return False
                
        return True
    

    def exit(self):
        self.close()
    
    
    
        
    


app = QApplication(sys.argv)

win = MainWindow()

win.show()
app.exec()