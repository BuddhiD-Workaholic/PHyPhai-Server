import os
import re
import subprocess as sp
import sys
import webbrowser
import socket
import threading
import datetime
from sys import platform

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox,QFileDialog

#When Installing
#Install PIP
#pip install --upgrade pyqt5
#pip install --upgrade psutil

#Global VariableDefine

#FilePath
path='./HTMLSite'
#PortNo
PORT='8020'
#CDate and Time
CDateT = datetime.datetime.now()

class Ui_MainWindow(object):
    
    def pathbutt(self):
        global path
         
        path=QFileDialog.getExistingDirectory()
        self.lineEdit.setPlainText(path)

    def mainfunc(self):
        global path
        global PORT
        
        if self.lineEdit.toPlainText() is not None:
            path=self.lineEdit.toPlainText()
        else: 
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("Path cannot be empty! \n Choose a path!")
            msgBox.setWindowTitle("Error!")
            msgBox.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox.exec() 
                  
        if self.lineEdit_2.toPlainText() is not None and self.lineEdit_2.toPlainText().strip().isdigit() and int(self.lineEdit_2.toPlainText()) >= 80 and int(self.lineEdit_2.toPlainText()) <= 65535:           
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('127.0.0.1',int(PORT)))
            if result == 0:
                PORT=PORT
                ptextth=self.plainTextEdit.toPlainText()
                ptextth=ptextth+"\n"+"Error: Port is in use! \t"+ CDateT.strftime("%m/%d/%Y, %H:%M:%S")
                self.plainTextEdit.setPlainText(ptextth)
                
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setText("The entered port is used by another program! \n Please select another port!")
                msgBox.setWindowTitle("Error!")
                msgBox.setStandardButtons(QMessageBox.Ok)
                returnValue = msgBox.exec()
            else:
                PORT=self.lineEdit_2.toPlainText()
                
                #Write everything 
                f = open("Server.txt", "w")
                f.write(path)
                f.write("\n")
                f.write(PORT)
                f.close()
                
                ptextth=self.plainTextEdit.toPlainText()
                ptextth=ptextth+"\n"+"Path and Port changed! \t"+ CDateT.strftime("%m/%d/%Y, %H:%M:%S")
                self.plainTextEdit.setPlainText(ptextth)
                
                msgBox = QMessageBox()
                msgBox.setText("Folder path and Server Port being changed!")
                msgBox.setWindowTitle("Success!")
                msgBox.setStandardButtons(QMessageBox.Ok)
                returnValue = msgBox.exec()
            sock.close()
        else: 
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("Port cannot be empty and only Numberse must be entered! \n Port number between 80<=65535")
            msgBox.setWindowTitle("Error!")
            msgBox.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox.exec()
    
    def Startbutt(self):
        global path
        global PORT
        
        self.lineEdit.setReadOnly(True)
        self.lineEdit_2.setReadOnly(True)
        
        try:
            sp.check_call(['php', '-v'])
        except:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("PHP is not installed in your PC, You need to install it!")
            msgBox.setWindowTitle("Error!")
            msgBox.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox.exec()
            sys.exit()    
        
        try:
            threading.Thread(target=MyThread1, args=[]).start()
            
            ptextth=self.plainTextEdit.toPlainText()
            ptextth=ptextth+"\n"+"Server started on http://localhost:"+ PORT +"      "+ CDateT.strftime("%m/%d/%Y, %H:%M:%S")
            self.plainTextEdit.setPlainText(ptextth)
                
        except:
            ptextth=self.plainTextEdit.toPlainText()
            ptextth=ptextth+"\n"+"Error: Server can't be Started on http://localhost:"+ PORT +"\t"+ CDateT.strftime("%m/%d/%Y, %H:%M:%S")
            self.plainTextEdit.setPlainText(ptextth)
            
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("PhyPy Server can't be starterd! \n Try again later!")
            msgBox.setWindowTitle("Error!")
            msgBox.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox.exec()
            
    def Endbutt(self): 
        
        global path
        global PORT
        
        self.lineEdit.setReadOnly(False)
        self.lineEdit_2.setReadOnly(False)

        try:
            #Platform
            if platform == "linux" or platform == "linux2":
                KillP = 'killall -9 php'
                os.system(KillP)
            elif platform == "darwin":
                KillP = 'killall -9 php'
                os.system(KillP)
            elif platform == "win32":
                KillP = 'taskkill /IM "php.exe" /F'
                os.system(KillP)
            
            ptextth=self.plainTextEdit.toPlainText()
            ptextth=ptextth+"\n"+"Server Stoped \t"+ CDateT.strftime("%m/%d/%Y, %H:%M:%S")+"\n"
            self.plainTextEdit.setPlainText(ptextth)

        except :
            ptextth=self.plainTextEdit.toPlainText()
            ptextth=ptextth+"\n"+"Error: Server can't be Stoped \t"+ CDateT.strftime("%m/%d/%Y, %H:%M:%S")
            self.plainTextEdit.setPlainText(ptextth)
            
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("PhyPy Server can't be Ended! \n Try killing the process!")
            msgBox.setWindowTitle("Error!")
            msgBox.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox.exec()
            
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(483, 401)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #Change Button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 90, 88, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.mainfunc)
        
        #CancelButton
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 340, 91, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(cancelbutt)
        
        #PAth Textbox
        self.lineEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 20, 271, 51))
        self.lineEdit.setObjectName("lineEdit")
        
        #Path
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 91, 19))
        self.label.setObjectName("label")
        
        #Port
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 101, 19))
        self.label_2.setObjectName("label_2")
        
        #Port Textbox
        self.lineEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 90, 171, 27))
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        #TextPain CMD
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 130, 461, 171))
        self.plainTextEdit.setObjectName("plainTextEdit")
        
        #Server Stops
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 310, 71, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.Endbutt)
        
        #Server Starts
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(180, 310, 71, 27))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.Startbutt)
        
        #Folderpath Browse
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 30, 88, 27))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.pathbutt)
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 90, 71, 19))
        self.label_3.setObjectName("label_3")
        
        #Help button 
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(330, 340, 41, 27))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(helpbutt)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PHyPhai Server V1.0"))
        self.pushButton.setText(_translate("MainWindow", "Change"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate("MainWindow", "Folder path:-"))
        self.label_2.setText(_translate("MainWindow", "Port number:-"))
        self.pushButton_3.setText(_translate("MainWindow", "Stop"))
        self.pushButton_4.setText(_translate("MainWindow", "Browse"))
        self.pushButton_5.setText(_translate("MainWindow", "Start"))
        self.pushButton_6.setText(_translate("MainWindow", "Help"))
        self.label_3.setText(_translate("MainWindow", "localhost:"))
        self.plainTextEdit.setReadOnly(True)
        
        #Read
        global path
        global PORT
        
        f = open("Server.txt", "r")
        path=f.readline()
        X=f.readline()
        PORT=f.readline()
        f.close()
        
        self.lineEdit.setPlainText(path)
        self.lineEdit_2.setPlainText(PORT)
        ptextth="Server lanuched  \t"+ CDateT.strftime("%m/%d/%Y, %H:%M:%S")
        self.plainTextEdit.setPlainText(ptextth)

def helpbutt():
    pass

def cancelbutt():
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Question)
    msgBox.setText("Are you Sure you wanna quite? ")
    msgBox.setWindowTitle("Quit")
    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        #Platform
        if platform == "linux" or platform == "linux2":
            KillP = 'killall -9 php'
            os.system(KillP)
        elif platform == "darwin":
            KillP = 'killall -9 php'
            os.system(KillP)
        elif platform == "win32":
            KillP = 'taskkill /IM "php.exe" /F'
            os.system(KillP) 
        sys.exit()

def MyThread1():
    if not path:
        cmd = 'php -S localhost:'+PORT
        url='http://localhost:'+PORT    
        webbrowser.open(url, new=1)
        os.system(cmd)
    else:
        cmd = 'php -S localhost:'+PORT+' -t '+path
        url='http://localhost:'+PORT    
        webbrowser.open(url, new=1)
        os.system(cmd)
     
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
