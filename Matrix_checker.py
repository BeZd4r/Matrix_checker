from random import randint
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog , QMessageBox
from Main_Window import Ui_MainWindow
import sys
import datetime

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_MainWindow()
ui.setupUi(window)
window.show()

size = 2
counter = 0
matrix_out = ""
matrix = None
stat = None
stat_check = {True: "Да", False:"Нет"}

def Reflexed():
    for i in range(size):
        if matrix[i][i] != 1:
            return False
    return True

def AntiReflexed():
    for i in range(size):
        if matrix[i][i] != 0:
            return False
    return True

def Symmetrical():
    for i in range(size):
        for j in range(size):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def AntiSymmetrical():
    for i in range(size):
        for j in range(size):
            if i == j:
                continue
            if matrix[i][j] == matrix[j][i]:
                return False
    return True

def Transitical():
    for i in range(size):
        for j in range(size):
            if i == j:
                continue
            for k in range(size):
                if k == i or k == j:
                    continue
                elif matrix[j][k] == 0:
                    continue
                elif matrix[i][k] == 0:
                    return False
    return True

def Error(err_type):
    match err_type:
        case "noNum":
            msg = QMessageBox.warning(window,"Ошибка","Неверный формат числа",QMessageBox.StandardButton.Ok)
        case "overSize":
            msg = QMessageBox.warning(window,"Ошибка","Число меньше 2 или больше 10",QMessageBox.StandardButton.Ok)

def Save_M():
    f = open("Saved_Matrix.txt","a")
    f.writelines(matrix_out + "\n")
    f.writelines(stat+"\n")
    f.close()

def Begin():
    global size, matrix, counter, stat, matrix_out

    size = ui.Input_Size.text()

    if size.isnumeric() == False :
        Error("noNum")
        return

    size = int(size)

    if size < 2 or size > 10:
        Error("overSize")
        return


    matrix = [[randint(0,1) for _ in range(size)] for _ in range(size)]
    counter += 1

    stat = f"Матрица {counter} ({size}x{size}) {datetime.date.today()}\n"
    stat += f"Матрица рефлексивна: {stat_check[Reflexed()]} \n"
    stat += f"Матрица антирефлексивна: {stat_check[AntiReflexed()]} \n"
    stat += f"Матрица симметрична: {stat_check[Symmetrical()]} \n"
    stat += f"Матрица антисимметрична: {stat_check[AntiSymmetrical()]} \n"
    stat += f"Матрица транзитна: {stat_check[Transitical()]} \n"

    ui.Statistic.setText(stat)

    matrix_out = ""
    for x in range(size):
        for z in range(size):
            matrix_out += str(matrix[x][z]) + " "
        matrix_out += "\n"

    ui.Matrix_text.setText("\n"*(int((10-size)/2)) + matrix_out)
    ui.Matrix_text.selectAll()
    ui.Matrix_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

ui.Lets.clicked.connect(Begin)
ui.Save.clicked.connect(Save_M)
sys.exit(app.exec())
