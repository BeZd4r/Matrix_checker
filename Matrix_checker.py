from random import randint
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog , QMessageBox
from Main_Window import Ui_MainWindow
import sys

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_MainWindow()
ui.setupUi(window)
window.show()

size = 2
def Error(err_type):
    match err_type:
        case "noNum":
            msg = QMessageBox.warning(window,"Ошибка","Неверный формат числа",QMessageBox.StandardButton.Ok)
        case "overSize":
            msg = QMessageBox.warning(window,"Ошибка","Число меньше 2 или больше 10",QMessageBox.StandardButton.Ok)

def Begin():
    global size
    size = ui.Input_Size.text()

    if size.isnumeric() == False :
        Error("noNum")
        return

    size = int(size)

    if size < 2 or size > 10:
        Error("overSize")
        return

    out_m = ""

    matrix = [[randint(0,1) for _ in range(size)] for _ in range(size)]

    for x in range(size):
        for z in range(size):
            out_m += str(matrix[x][z]) + " "
        out_m += "\n"

    ui.Matrix_text.setText("\n"*(int((10-size)/2)) + out_m)
    ui.Matrix_text.selectAll()
    ui.Matrix_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

ui.Lets.clicked.connect(Begin)
sys.exit(app.exec())
