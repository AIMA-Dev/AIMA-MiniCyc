import sys
from PySide6 import QtCore, QtWidgets, QtGui, QtUiTools
from PySide6.QtCore import QTimer
from scripts.logger import log_values

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
    
    # Logger
    timer = QTimer()
    timer.setInterval(500)
    values_to_log = [1, 2, 3]
    timer.timeout.connect(log_values(values_to_log, 100))
    timer.start()
    
    sys.exit(app.exec())