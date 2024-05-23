import sys
from PySide6 import QtCore, QtWidgets, QtGui, QtUiTools
from PySide6.QtCore import QTimer
# from scripts.settings import
from scripts.logger import log_values
from scripts.serialLink import list_available_ports

def loadUiWidget(uifilename, parent=None):
    loader = QtUiTools.QUiLoader()
    uifile = QtCore.QFile(uifilename)
    uifile.open(QtCore.QFile.ReadOnly)
    ui = loader.load(uifile, parent)
    uifile.close()
    return ui

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    MainWindow = loadUiWidget("GUI.ui")
    MainWindow.showFullScreen()
    MainWindow.showMaximized()
    
    # Settings
    
    # Logger
    timer = QTimer()
    spinBox_logFrequency = MainWindow.findChild(QtWidgets.QSpinBox, "spinBox_logFrequency")
    logFrequencyInMB = spinBox_logFrequency.value() * 1000
    timer.setInterval(logFrequencyInMB)
    values_to_log = [1, 2, 3]
    spinBox_fileSizeLimit = MainWindow.findChild(QtWidgets.QSpinBox, "spinBox_fileSizeLimit")
    fileSizeLimit = spinBox_fileSizeLimit.value()
    timer.timeout.connect(log_values(values_to_log, fileSizeLimit))
    timer.start()
    
    # Serial Link
    print("List of avaible ports : ",list_available_ports())
        
    sys.exit(app.exec())