from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit,QPushButton,QCheckBox,QLabel
from PyQt5.QtGui import QIcon,QPixmap,QPalette,QBrush,QImage,QFont
global a
a = ""

class calc(QMainWindow):

    def __init__(self):
        super(calc,self).__init__()
        self.main()
    def main(self):
        self.setWindowTitle('NOT A CALCULATOR')

        
        self.setGeometry(500,300,300,400)
        self.dis  = QLabel(self)
        self.dis.setGeometry(15,8,270,50)
        
        self.box1 = QPushButton(self)
        
        
        self.box1.setGeometry(20,80,50,50)
        self.box1.setText('/')
        s = ('''QPushButton {
  border-color: #4aabff;
  border-width: 3px;   
  border-style: solid;
  border-radius: 15px;
  margin:3px;
  padding:5px;
  font-size:18px;
  font-weight:700;
  
  
}
QPushButton#box4{
    font-size: 11px;
}
QPushButton#box5{
    font-size: 12px;
}
QPushButton:hover{
    margin: 5px;
    border-color:orange;
}
QPushButton:pressed{
    margin:7px;
    border-color:orange;
    background-color:#ffffff;

}
QMainWindow{
    Background-color:#f4f4f4;
}
QLabel{
    Background-color:orange;
    font-size: 20px;
}
QPushButton#box20{
    font-size:11px;
}
QPushButton#box21{
    font-size:12px;
}
''')
         
        self.setStyleSheet(s)
        self.box1.clicked.connect(self.o1)
        

        self.box2 = QPushButton(self)
        self.box2.setGeometry(70,80,50,50)

        
        self.box2.setText('*')
        
        self.box2.clicked.connect(self.o2)

        self.box3 = QPushButton(self)
        self.box3.setGeometry(120,80,50,50)
        
        self.box3.setText('-')
        
        self.box3.clicked.connect(self.o3)
        

        self.box4 = QPushButton(self)
        self.box4.setGeometry(170,80,50,50)

        self.box4.setText("x**2")
        self.box4.setObjectName('box4')

        
        self.box4.clicked.connect(self.b1)

        self.box5 = QPushButton(self)
        self.box5.setGeometry(220,80,50,50)
        


        
        self.box5.setText('cube')

        
        self.box5.clicked.connect(self.b2)
        self.box5.setObjectName('box5')

        self.box6 = QPushButton(self)
        self.box6.setGeometry(20,135,50,50)
        self.box6.setText('9')
        
        
        self.box6.clicked.connect(self.c9)

        self.box7 = QPushButton(self)
        self.box7.setGeometry(70,135,50,50)
        self.box7.setText('8')
        
        self.box7.clicked.connect(self.c8)
        


        self.box8 = QPushButton(self)
        self.box8.setGeometry(120,135,50,50)
        

        self.box8.setText('7')
        self.box8.clicked.connect(self.c7)

        


        self.box9 = QPushButton(self)
        self.box9.setGeometry(170,135,50,50)
        self.box9.setText('6')
        self.box9.clicked.connect(self.c6)
        
        self.box10 = QPushButton(self)
        self.box10.setGeometry(222,135,50,105)
        
        self.box10.setText('+')
        self.box10.clicked.connect(self.o4)
        


        self.box11 = QPushButton(self)
        self.box11.setGeometry(20,190,50,50)
        

        self.box11.setText('5')
        self.box11.clicked.connect(self.c5)
        

        self.box12 = QPushButton(self)
        self.box12.setGeometry(70,190,50,50)
        

        self.box12.setText('4')
        
        self.box12.clicked.connect(self.c4)

        self.box13 = QPushButton(self)
        self.box13.setGeometry(120,190,50,50)
        
        self.box13.setText('3')
        self.box13.clicked.connect(self.c3)

        self.box14 = QPushButton(self)
        
        self.box14.setGeometry(170,190,50,50)
        

        self.box14.setText('2')
        self.box14.clicked.connect(self.c2)

        self.box15 = QPushButton(self)
        
        self.box15.setGeometry(20,245,50,50)
        self.box15.setText('1')
        self.box15.clicked.connect(self.c1)


        self.box16 = QPushButton(self)
        
        self.box16.setGeometry(70,245,50,50)
        
        self.box16.setText('0')
        self.box16.clicked.connect(self.c0)

        self.box17 = QPushButton(self)
        
        self.box17.setGeometry(120,245,50,50)
        

        self.box17.setText('.')
        self.box17.clicked.connect(self.dec)

        self.box18 = QPushButton(self)
        
        self.box18.setGeometry(175,245,100,50)
        
        self.box18.setText('delete')
        self.box18.clicked.connect(self.delete)
        self.box19 = QPushButton(self)
        self.box19.setGeometry(70,305,150,50)
        
        self.box19.setText('calculate')
        
        self.box19.clicked.connect(self.out)
        
        self.box20 = QPushButton(self)
        self.box20.setGeometry(20,305,50,50)
        
        self.box20.setText('sqrt')
        self.box20.setObjectName('box20')
        self.box20.clicked.connect(self.sqrt)
        

        self.box21 = QPushButton(self)
        self.box21.setGeometry(220,305,50,50)
        
        self.box21.setText('x**n')
        self.box21.setObjectName('box21')
       
        self.box21.clicked.connect(self.power)

        self.box1.setShortcut('/')
        self.box2.setShortcut('*')
        self.box3.setShortcut('-')
        self.box4.setShortcut('Shift+9')
        self.box5.setShortcut('Shift+0')
        self.box6.setShortcut('9')
        self.box7.setShortcut('8')
        self.box8.setShortcut('7')
        self.box9.setShortcut('6')
        self.box10.setShortcut('+')
        self.box11.setShortcut('5')
        self.box12.setShortcut('4')
        self.box13.setShortcut('3')
        self.box14.setShortcut('2')

        self.box15.setShortcut('1')
        self.box16.setShortcut('0')
        self.box17.setShortcut('.')
        self.box18.setShortcut('Backspace')
        self.box19.setShortcut('Enter')



    def c0(self):
        global a
        a = a+"0"
        self.dis.setText(a)
    def c1(self):
        global a
        a = a+"1"
        self.dis.setText(a)
    def c2(self):
        global a
        a = a+"2"
        self.dis.setText(a)
    def c3(self):
        global a
        a = a+"3"
        self.dis.setText(a)
    def c4(self):
        global a
        a = a+"4"
        self.dis.setText(a)
    def c5(self):
        global a
        a = a+"5"
        self.dis.setText(a)
    def c6(self):
        global a
        a = a+"6"
        self.dis.setText(a)
    def c7(self):
        global a
        a = a+"7"
        self.dis.setText(a)
    def c8(self):
        global a
        a = a+"8"
        self.dis.setText(a)
    def c9(self):
        global a
        a = a+"1"
        self.dis.setText(a)
    def o1(self):

         self.ope = '/'
         self.dis.setText('/')
         self.op()
    def o2(self):

         self.ope ='*'
         self.dis.setText('*')
         self.op()
    def o3(self):

        self.ope ='-'
        self.dis.setText('-')
        self.op()
    def o4(self):

         self.ope = '+'
         self.dis.setText('+')
         self.op()
    def b1(self):
        global a
        a = float(a)
        w = a**2
        self.dis.setText(f'{w}')


    def b2(self):
        global a
        a  = float(a)
        w = a**3
        self.dis.setText(f'{w}')



    def dec(self):
        global a
        a = a+"."
        self.dis.setText(a)





    def op(self):
        global a
        self.num1 = float(a)
        a = ""

    def delete(self):
        global a
        n = len(a)
        b = a[0:n-1]
        a = b
        self.dis.setText(a)
    def sqrt(self):
        global a
        a  = float(a)
        self.dis.setText(f'{a**0.5}')
    def power(self):
        self.ope = 'p'
        self.op()
        self.dis.setText(f'power')

    def gettxt(self):
            global a
            self.b = float(a)
            return self.b

    def out(self):
        global a

        d = self.gettxt()


        if  self.ope  == '/':
            if d == 0:
                self.dis.setText('Zero Divison Error')

            w = self.num1/d
            self.dis.setText(f'{w}')
        elif self.ope == '*':
            w =self.num1*d
            self.dis.setText(f'{w}')
        elif self.ope == '-':
            w = self.num1 - d
            self.dis.setText(f'{w}')
        elif self.ope  == '+':
            w = self.num1 + d
            self.dis.setText(f'{w}')
        elif self.ope == 'p':
            self.dis.setText(f'{self.num1**d}')

        a = str(w)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = calc()
    win.show()
    sys.exit(app.exec_())
