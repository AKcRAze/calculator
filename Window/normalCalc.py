from PyQt5 import QtWidgets , QtGui 

from operations.functions import operations


class normal(QtWidgets.QWidget):

    def __init__(self):
        super().__init__(parent=None)
        self.initUI()

    def initUI(self):
        display = QtWidgets.QLineEdit()
        display.textChanged(False)
        
        button0 = QtWidgets.QPushButton("0")
        button1 = QtWidgets.QPushButton("1")
        button2 = QtWidgets.QPushButton("2")
        button3 = QtWidgets.QPushButton("3")
        button4 = QtWidgets.QPushButton("4")
        button5 = QtWidgets.QPushButton("5")
        button6 = QtWidgets.QPushButton("6")
        button7 = QtWidgets.QPushButton("7")
        button8 = QtWidgets.QPushButton("8")
        button9 = QtWidgets.QPushButton("9")
        
        
        button_plus = QtWidgets.QPushButton("+")
        
        button_sub = QtWidgets.QPushButton("-")
        button_product = QtWidgets.QPushButton("*")
        button_div = QtWidgets.QPushButton("/")
        button_decimal= QtWidgets.QPushButton(".")
        button_square = QtWidgets.QPushButton("x^2")
        button_sqrt = QtWidgets.QPushButton("sqrt")
        button_power = QtWidgets.QPushButton("power")
        button_answer = QtWidgets.QPushButton("=")

        grid = QtWidgets.QGridLayout()
        grid.addWidget(display,0,0,1,4)
        grid.addWidget(button_square,1,0)
        grid.addWidget(button_div,1,1)
        grid.addWidget(button_product,1,2)
        grid.addWidget(button_sub,1,3)
        grid.addWidget(button7,2,0)
        grid.addWidget(button8,2,1)
        grid.addWidget(button9,2,2)
        grid.addWidget(button_plus,2,3)

        grid.addWidget(button4,3,0)
        grid.addWidget(button5,3,1)
        grid.addWidget(button6,3,2)
        grid.addWidget(button_sqrt,3,3)
        grid.addWidget(button1,4,0)
        grid.addWidget(button2,4,1)
        grid.addWidget(button3,4,2)
        grid.addWidget(button_power,4,3)
        grid.addWidget(button0,5,0,1,2)
        grid.addWidget(button_decimal,5,2)
        grid.addWidget(button_answer,5,3)
        grid.setSpacing(10)

        self.setLayout(grid)
        a = QtWidgets.QLabel(self)
        a.setText("Sdfsa")
        b = a.text()
        print(b)        
    


if __name__ == "__main__":
    import sys
    app  = QtWidgets.QApplication(sys.argv)
    win = normal()
    win.show()
    sys.exit(app.exec_())
