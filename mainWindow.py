from PyQt5 import QtWidgets , QtGui 
from Window.normalCalc import normal


class MainWin(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__(parent = None)
        self.initUI()

    def initUI(self):
        self.setGeometry(400,400, 300,300)
        self.setWindowTitle('CALC')
        icon = QtGui.QIcon("Window/calculator.png")
        self.setWindowIcon(icon)
        self.setCentralWidget(normal())


if __name__ == "__main__":
    import sys 
    app = QtWidgets.QApplication(sys.argv)
    window = MainWin()
    window.show()
    sys.exit(app.exec_())
