import sys
from PySide6 import QtCore, QtWidgets, QtGui, QtUiTools
from PySide6.QtCore import QTimer
from scripts.settings import Settings
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
    
    # Load Settings
    settings = Settings()
    ## Log Frequency
    spinBox_logFrequency = MainWindow.findChild(QtWidgets.QSpinBox, "spinBox_logFrequency")
    if not settings.does_setting_exist('logFrequency'):
        settings.write_to_settings_file('logFrequency', spinBox_logFrequency.value())
    else:
        spinBox_logFrequency.setValue(int(settings.read_from_settings_file('logFrequency')))
    ## File Size Limit
    spinBox_fileSizeLimit = MainWindow.findChild(QtWidgets.QSpinBox, "spinBox_fileSizeLimit")
    if not settings.does_setting_exist('fileSizeLimit'):
        settings.write_to_settings_file('fileSizeLimit', spinBox_fileSizeLimit.value())
    else:
        spinBox_fileSizeLimit.setValue(int(settings.read_from_settings_file('fileSizeLimit')))
    ## Log On/Off
    pushButton_LogOnOff = MainWindow.findChild(QtWidgets.QPushButton, "pushButton_LogOnOff")
    if not settings.does_setting_exist('logOnOff'):
        settings.write_to_settings_file('logOnOff', pushButton_LogOnOff.isChecked())
    else:
        pushButton_LogOnOff.setChecked(bool(settings.read_from_settings_file('logOnOff')))
    
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
    print("List of avaible ports : ", list_available_ports())
        
    sys.exit(app.exec())