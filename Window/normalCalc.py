''' this a simple calculator  '''



from PyQt5 import QtWidgets , QtGui ,QtCore

from operations.functions import operations


class normal(QtWidgets.QWidget):

    def __init__(self):
        super().__init__(parent=None)
        self.initUI()

    def initUI(self):

        self.display = QtWidgets.QLabel("life is Dumb")     
        
        button0 = QtWidgets.QPushButton("0")
        button0.clicked.connect(self.clicked_0)
        button0.setShortcut("0")

        button1 = QtWidgets.QPushButton("1")
        button1.clicked.connect(self.clicked_1)
        button1.setShortcut("1")

        button2 = QtWidgets.QPushButton("2")
        button2.clicked.connect(self.clicked_2)
        button2.setShortcut("2")


        button3 = QtWidgets.QPushButton("3")
        button3.clicked.connect(self.clicked_3)
        button3.setShortcut("3")


        button4 = QtWidgets.QPushButton("4")
        button4.clicked.connect(self.clicked_4)
        button4.setShortcut("4")

        button5 = QtWidgets.QPushButton("5")
        button5.clicked.connect(self.clicked_5)
        button5.setShortcut("5")
        
        button6 = QtWidgets.QPushButton("6")
        button6.clicked.connect(self.clicked_6)
        button6.setShortcut("6")


        button7 = QtWidgets.QPushButton("7")
        button7.clicked.connect(self.clicked_7)
        button7.setShortcut("7")

        button8 = QtWidgets.QPushButton("8")
        button8.clicked.connect(self.clicked_8)
        button8.setShortcut("8")

        button9 = QtWidgets.QPushButton("9")
        button9.clicked.connect(self.clicked_9)
        button9.setShortcut("9")

        button_delete = QtWidgets.QPushButton("delete")
        button_delete.clicked.connect(self.clicked_delete)
        button_delete.setShortcut("delete")

    
        button_plus = QtWidgets.QPushButton("+")
        button_plus.clicked.connect(self.clicked_plus)
        button_plus.setShortcut("+")
        
        button_sub = QtWidgets.QPushButton("-")
        button_sub.clicked.connect(self.clicked_sub)
        button_sub.setShortcut("-")
        
        button_product = QtWidgets.QPushButton("*")
        button_product.clicked.connect(self.clicked_product)
        button_product.setShortcut("*")

        button_div = QtWidgets.QPushButton("/")
        button_div.clicked.connect(self.clicked_divide)
        button_div.setShortcut("/")

        button_decimal= QtWidgets.QPushButton(".")
        button_decimal.clicked.connect(self.clicked_decimal)
        button_decimal.setShortcut(".")
        
        button_square = QtWidgets.QPushButton("x^2")
        button_square.clicked.connect(self.clicked_square)

        button_sqrt = QtWidgets.QPushButton("sqrt")
        button_sqrt.clicked.connect(self.clicked_sqrt) 
        
        button_power = QtWidgets.QPushButton("power")
        button_power.clicked.connect(self.clicked_power)
        
        button_answer = QtWidgets.QPushButton("=")
        button_answer.setShortcut("Enter")

        button_answer.clicked.connect(self.clicked_answer)


        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.display,0,0,1,4)
        grid.addWidget(button_div,1,0)
        grid.addWidget(button_product,1,1)
        grid.addWidget(button_sub,1,2)
        grid.addWidget(button_delete,1,3)
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
        grid.addWidget(button_square,5,0)
        grid.addWidget(button0,5,1)
        grid.addWidget(button_decimal,5,2)
        grid.addWidget(button_answer,5,3)
        grid.setSpacing(10)

        self.setLayout(grid)

        self.num1  = "" 
        self.num2  = ""
        self.power  = ""

        style = ''' 
        QPushButton
        {
            border: solid;
            border-color:teal;
            border-width:2px;    
        }
           
         '''
        self.setStyleSheet(style)

    def clicked_0(self):
        
        self.num2 += "0"
        self.display_text()
    
    def clicked_1(self):
        
        self.num2  += "1"
        self.display_text()

    
    def clicked_2(self):
       
        self.num2 += "2"
        self.display_text()
    
    def clicked_3(self):
       
        self.num2 += "3"
        self.display_text()
    
    def clicked_4(self):
       
        self.num2 += "4"
        self.display_text()

    def clicked_5(self):
       
        self.num2 += "5"
        self.display_text()
    
    def clicked_6(self):
       
        self.num2 += "6"
        self.display_text()
    
    def clicked_7(self):
       
        self.num2 += "7"
        self.display_text()
    
    def clicked_8(self):
       
        self.num2 += "8"
        self.display_text()
    
    def clicked_9(self):
        self.num2 += "9"
        self.display_text()
    
    def clicked_decimal(self):
       
        self.num2 += "."
        self.display_text()

    def clicked_delete(self):
       
        self.num2 = self.num2[0:len(self.num2)-1]
        self.display_text()
        

    def clicked_divide(self):
        
        self.dump()
        self.operator = "/"
        self.clear_display()
    
    def clicked_product(self):
        
        self.dump()
        self.operator = "*"
        self.clear_display()

    def clicked_plus(self):
        
        self.dump()
        self.operator = "+"
        self.clear_display()
        
    def clicked_sub(self):
        
        self.dump()
        self.operator = "-"
        self.clear_display()

    def clicked_power(self):
        
        self.dump()
        self.operator = "power"
        self.clear_display()
        self.display.setText("power")     

    def clicked_sqrt(self):
        
        if self.num2 == "":   
            self.display.setText("Please Enter a value")
        else:        
            buff = float(self.num2)
            answer = operations.squareRoot(self,buff)
            self.num2 = f"{answer}"
            self.display_text()

    def clicked_square(self):
        
        if self.num2 == "":   
            self.display.setText("Please Enter a value")
        else:        
            buff = float(self.num2)
            answer = operations.square(self,buff)
            self.num2 = f"{answer}"
            self.display_text()

    def clicked_answer(self):

        try:  
            a  = int(self.num1)
            b  = int(self.num2)
        except (ValueError):
            a = float(self.num1)
            b = float(self.num2)
        if  self.operator == "+":
            answer = operations.add(self,a,b)

        elif self.operator == "-":
            answer = operations.sub(self,a,b)
        
        elif self.operator == "*":
            answer = operations.product(self,a,b)

        elif self.operator == "/":
            answer = operations.divide(self,a,b)

        elif self.operator == "power":
            answer = operations.power(self,a,b)    
        
        self.num2 = f"{answer}"
        self.display_text()

    def dump(self):

        self.num1  = self.num2
        self.num2 = ""

    def display_text(self):

        self.display.setText(self.num2)

    def clear_display(self):

        self.display.setText("")
        
if __name__ == "__main__":
    import sys
    app  = QtWidgets.QApplication(sys.argv)
    win = normal()
    win.show()
    sys.exit(app.exec_())
