from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle("Logic Gate Calculator")
        self.initUI()

    def initUI(self):
        
        #Label for combo box of X
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setGeometry(QtCore.QRect(60, 50, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label1.setText("Select X")

        #Label for combo box of Y
        self.label2 = QtWidgets.QLabel(self)
        self.label2.setGeometry(QtCore.QRect(320, 50, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.label2.setText("Select Y")
        
        #Label for combo box of Gate
        self.label3 = QtWidgets.QLabel(self)
        self.label3.setGeometry(QtCore.QRect(580, 50, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.label3.setText("Select Gate")
        
        #Combo box for X
        self.comboX = QtWidgets.QComboBox(self)
        self.comboX.setGeometry(QtCore.QRect(60, 100, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.comboX.setFont(font)
        self.comboX.addItem("None")
        self.comboX.addItem("0")
        self.comboX.addItem("1")

        #Combo box for Y
        self.comboY = QtWidgets.QComboBox(self)
        self.comboY.setGeometry(QtCore.QRect(320, 100, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.comboY.setFont(font)
        self.comboY.setObjectName("comboY")
        self.comboY.addItem("None")
        self.comboY.addItem("0")
        self.comboY.addItem("1")

        #Combo box for Gate
        self.comboGateSelect = QtWidgets.QComboBox(self)
        self.comboGateSelect.setGeometry(QtCore.QRect(580, 100, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.comboGateSelect.setFont(font)
        self.comboGateSelect.setObjectName("comboGateSelect")
        self.comboGateSelect.addItem("AND")
        self.comboGateSelect.addItem("OR")
        self.comboGateSelect.addItem("NOT")
        self.comboGateSelect.addItem("NAND")
        self.comboGateSelect.addItem("NOR")
        self.comboGateSelect.addItem("XOR")

        #Setting up the Submit button
        self.submit = QtWidgets.QPushButton(self)
        self.submit.setGeometry(QtCore.QRect(290, 360, 160, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.submit.setFont(font)
        self.submit.setText("Submit")
        self.submit.setObjectName("submit")

        #Setting up the label for showing result
        self.result = QtWidgets.QLabel(self)
        self.result.setGeometry(QtCore.QRect(300, 240, 250, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setItalic(True)
        self.result.setFont(font)
        self.result.setObjectName("result")

        #Setting up dark/light mode toggle button
        self.mode = QtWidgets.QPushButton(self)
        self.mode.setGeometry(QtCore.QRect(680, 480, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.mode.setFont(font)
        self.mode.setCheckable(True)
        self.mode.setText("Dark Mode")
        self.mode.setObjectName("mode")

        self.mode.clicked.connect(self.changeCol)
        self.submit.clicked.connect(self.submitted)


    #function for changing dark/light mode
    def changeCol(self):
        if self.mode.isChecked():
            self.label1.setStyleSheet("color: rgb(255, 255, 255)")
            self.label2.setStyleSheet("color: rgb(255, 255, 255)")
            self.label3.setStyleSheet("color: rgb(255, 255, 255)")
            self.result.setStyleSheet("color: rgb(255, 255, 255)")
            self.mode.setText("Light Mode")
            self.mode.setStyleSheet("color: rgb(255, 255, 255)")
            self.submit.setStyleSheet("color: rgb(255, 255, 255)")
            self.setStyleSheet("background: rgb(12, 63, 135)")
            self.comboX.setStyleSheet("background: rgb(235, 137, 40); color: rgb(255, 255, 255)")
            self.comboY.setStyleSheet("background: rgb(235, 137, 40); color: rgb(255, 255, 255)")
            self.comboGateSelect.setStyleSheet("background: rgb(235, 137, 40); color: rgb(255, 255, 255)")
        else:
            self.label1.setStyleSheet("color: rgb(0, 0, 0)")
            self.label2.setStyleSheet("color: rgb(0, 0, 0)")
            self.label3.setStyleSheet("color: rgb(0, 0, 0)")
            self.result.setStyleSheet("color: rgb(0, 0, 0)")
            self.mode.setText("Dark Mode")
            self.mode.setStyleSheet("color: rgb(0, 0, 0)")
            self.submit.setStyleSheet("color: rgb(0, 0, 0)")
            self.setStyleSheet("background: rgb(253, 246, 227)")
            self.comboX.setStyleSheet("background: rgb(235, 137, 40); color: rgb(0, 0, 0)")
            self.comboY.setStyleSheet("background: rgb(235, 137, 40); color: rgb(0, 0, 0)")
            self.comboGateSelect.setStyleSheet("background: rgb(235, 137, 40); color: rgb(0, 0, 0)")

    #function for selecting Gate
    def submitted(self):
        x = self.comboX.currentText()
        y = self.comboY.currentText()
        gate = self.comboGateSelect.currentText()
        if gate == "AND":
            self.and_gate(x, y)
        elif gate == "OR":
            self.or_gate(x, y)
        elif gate == "NOT":
            self.not_gate(x, y)
        elif gate == "NAND":
            self.nand_gate(x, y)
        elif gate == "NOR":
            self.nor_gate(x, y)
        elif gate == "XOR":
            self.xor_gate(x, y)

    def and_gate(self, x, y):
        if x=="None" or y == "None":
            self.result.setText("Error")
        else:
            a = int(x)
            b = int(y)
            res = a and b
            if res == True:
                res = 1
            else:
                res = 0
            self.result.setText("X AND Y = "+str(res))

    def or_gate(self, x, y):
        if x == "None" or y == "None":
            self.result.setText("Error")
        else:
            a = int(x)
            b = int(y)
            res = a or b
            if res == True:
                res = 1
            else:
                res = 0
            self.result.setText("X OR Y = "+str(res))

    def not_gate(self, x, y):
        if x == "None" and y == "None":
            self.result.setText("Error")
        elif x != "None" and y != "None":
            self.result.setText("Error")
        else:
            s = ""
            if x == "None":
                res = not(int(y))
                s = "Y"
            elif y == "None":
                res = not(int(x))
                s = "X"
            if res == True:
                res = 1
            else:
                res = 0
            self.result.setText("NOT "+s+" = "+str(res))

    def nand_gate(self, x, y):
        if x == "None" or y == "None":
            self.result.setText("Error")
        else:
            a = int(x)
            b = int(y)
            res = not(a and b)
            if res == True:
                res = 1
            else:
                res = 0
            self.result.setText("X NAND Y = "+str(res))

    def nor_gate(self, x, y):
        if x == "None" or y == "None":
            self.result.setText("Error")
        else:
            a = int(x)
            b = int(y)
            res = not(a or b)
            if res == True:
                res = 1
            else:
                res = 0
            self.result.setText("X NOR Y = "+str(res))
        
    def xor_gate(self, x, y):
        if x == "None" or y == "None":
            self.result.setText("Error")
        else:
            a = int(x)
            b = int(y)
            res = (not(a) and b) or (a and not(b))
            if res == True:
                res = 1
            else:
                res = 0
            self.result.setText("X XOR Y = "+str(res))
        
app = QtWidgets.QApplication(sys.argv)
style = """
    QMainWindow {
        background: rgb(253, 246, 227);
        font-family: Product Sans;
    }
    QLabel#label1, #label2, #label3  {
        color: rgb(0, 0, 0);
        text-decoration: underline;
        font-weight: bold;
    }
    QComboBox   {
        background: rgb(235, 137, 40);
        color: rgb(0, 0, 0);
        border: 2px solid rgb(12, 63, 135);
        border-radius: 5px;
    }
    QPushButton {
        color: rgb(0, 0, 0)
        background: white;
        border: 10px solid red;
        border-radius: 5px;
    }
"""   
app.setStyleSheet(style) 
m = MyWindow()
m.show()
sys.exit(app.exec_())