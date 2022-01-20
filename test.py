import sys
import serial
import serial.tools.list_ports
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5.QtCore import QTimer
from form import Ui_Form
import time
import subprocess
import os
#subprocess.run(["ls", "-l"])
class Utility_Form(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(Utility_Form, self).__init__()
        self.setupUi(self)
        self.init()
        
    def init(self):
        self.btnUV4.clicked.connect(self.command_update)
        self.btnPrj.clicked.connect(self.project_update)
        self.btnCompile.clicked.connect(self.compile_project)
        
    def command_update(self):
        fileName=self.openFileNameDialog()
        self.txtUV4.setText(fileName)
        
    def project_update(self):
        fileName=self.openFileNameDialog()
        self.txtPrj.setText(fileName)
        print(os.path.dirname(fileName))
        
    def compile_project(self):
        cmd=self.txtUV4.toPlainText()
        prj=self.txtPrj.toPlainText()
        result=subprocess.run([cmd,"-j0","-r",prj,"-o","result1.txt"],capture_output=True, text=True).stdout
        self.txtCompileResult.setText(result)
        
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            return fileName
        return None
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = Utility_Form()
    myshow.show()
    sys.exit(app.exec_())