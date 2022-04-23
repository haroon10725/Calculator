from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')

        self.setFixedSize(500,500)

        self.create_widgets()



    def create_widgets(self):

        btn0 = QPushButton(self)
        btn0.setFixedSize(90,90)
        btn0.move(10, 400)
        btn0.setText('0')
        btn0.setFont(QFont('Times New Roman', 100))

        btn1 = QPushButton(self)
        btn1.setFixedSize(90,90)
        btn1.move(10, 300)
        btn1.setText('1')
        btn1.setFont(QFont('Times New Roman',100))

        btn4 = QPushButton(self)
        btn4.setFixedSize(90,90)
        btn4.move(10, 200)
        btn4.setText('4')
        btn4.setFont(QFont('Times New Roman', 100))

        btn7 = QPushButton(self)
        btn7.setFixedSize(90,90)
        btn7.move(10, 100)
        btn7.setText('7')
        btn7.setFont(QFont('Times New Roman', 100))

        btn4 = QPushButton(self)
        btn4.setFixedSize(90, 90)
        btn4.move(120, 100)
        btn4.setText('8')
        btn4.setFont(QFont('Times New Roman', 100))

        btn5 = QPushButton(self)
        btn5.setFixedSize(90, 90)
        btn5.move(230, 200)
        btn5.setText('6')
        btn5.setFont(QFont('Times New Roman', 100))

        btn6 = QPushButton(self)
        btn6.setFixedSize(90, 90)
        btn6.move(230, 100)
        btn6.setText('9')
        btn6.setFont(QFont('Times New Roman', 100))

        btn7 = QPushButton(self)
        btn7.setFixedSize(90, 90)
        btn7.move(120, 200)
        btn7.setText('5')
        btn7.setFont(QFont('Times New Roman', 100))

        btn8 = QPushButton(self)
        btn8.setFixedSize(90, 90)
        btn8.move(120, 300)
        btn8.setText('2')
        btn8.setFont(QFont('Times New Roman', 100))

        btn9 = QPushButton(self)
        btn9.setFixedSize(90,90)
        btn9.move(120, 400)
        btn9.setText('.')
        btn9.setFont(QFont('Times New Roman', 100))

        btn10 = QPushButton(self)
        btn10.setFixedSize(90, 90)
        btn10.move(230, 300)
        btn10.setText('3')
        btn10.setFont(QFont('Times New Roman', 100))

        btn11 = QPushButton(self)
        btn11.setFixedSize(90, 90)
        btn11.move(230, 400)
        btn11.setText('=')
        btn11.setFont(QFont('Times New Roman', 100))

        btn12 = QPushButton(self)
        btn12.setFixedSize(90, 90)
        btn12.move(340, 400)
        btn12.setText('+')
        btn12.setFont(QFont('Times New Roman', 100))

        btn13 = QPushButton(self)
        btn13.setFixedSize(90, 90)
        btn13.move(340, 300)
        btn13.setText('-')
        btn13.setFont(QFont('Times New Roman', 100))

        btn14 = QPushButton(self)
        btn14.setFixedSize(90, 90)
        btn14.move(340, 200)
        btn14.setText('x')
        btn14.setFont(QFont('Times New Roman', 100))

        btn15 = QPushButton(self)
        btn15.setFixedSize(90, 90)
        btn15.move(340, 100)
        btn15.setText('%')
        btn15.setFont(QFont('Times New Roman', 100))


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
