# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import random
import string

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(327, 358)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(80, 100, 81, 20))
        self.checkBox.setObjectName("checkBox")
        
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(80, 130, 81, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 180, 181, 71))
        self.pushButton.setStyleSheet("\n"
"QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(0, 255, 0);\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"    font: 12pt \"Yu Gothic UI Semilight\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:  rgb(0, 255, 255);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 20, 141, 20))
        self.label_2.setObjectName("label_2")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 221, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 327, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Подключаем функцию к кнопке
        self.pushButton.clicked.connect(self.generate_password)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "Буквы"))
        self.checkBox_2.setText(_translate("MainWindow", "Цифры"))
        self.pushButton.setText(_translate("MainWindow", "Сгенерировать"))
        self.label_2.setText(_translate("MainWindow", "Генератор паролей"))
        self.label.setText(_translate("MainWindow", "Пароль будет здесь!"))
    
    def generate_password(self):
        # Получаем, что выбрано
        use_letters = self.checkBox.isChecked()
        use_digits = self.checkBox_2.isChecked()
        
        # Если ничего не выбрано, не генерировать пароль
        if not use_letters and not use_digits:
            self.label.setText("Выберите хотя бы один тип символов.")
            return
        
        # Список допустимых символов
        characters = ''
        if use_letters:
            characters += string.ascii_letters  # Буквы
        if use_digits:
            characters += string.digits  # Цифры
        
        # Генерация пароля длиной 12 символов
        password = ''.join(random.choice(characters) for i in range(12))
        
        # Отображаем результат в лейбле
        self.label.setText(password)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
