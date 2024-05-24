import os
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


def load_settings(MainWindow):
    # Log path
    label_logPath = MainWindow.findChild(
        QtWidgets.QLabel, "label_logPath")
    if not settings.does_setting_exist('logPath'):
        settings.write_to_settings_file('logPath', './logs/')
    label_logPath.setText(
        os.getcwd()+settings.read_from_settings_file('logPath'))

    # Log Frequency
    spinBox_logFrequency = MainWindow.findChild(
        QtWidgets.QSpinBox, "spinBox_logFrequency")
    if not settings.does_setting_exist('logFrequency'):
        settings.write_to_settings_file(
            'logFrequency', spinBox_logFrequency.value())
    else:
        spinBox_logFrequency.setValue(
            int(settings.read_from_settings_file('logFrequency')))

    # File Size Limit
    spinBox_fileSizeLimit = MainWindow.findChild(
        QtWidgets.QSpinBox, "spinBox_fileSizeLimit")
    if not settings.does_setting_exist('fileSizeLimit'):
        settings.write_to_settings_file(
            'fileSizeLimit', spinBox_fileSizeLimit.value())
    else:
        spinBox_fileSizeLimit.setValue(
            int(settings.read_from_settings_file('fileSizeLimit')))

    # Log On/Off
    pushButton_LogOnOff = MainWindow.findChild(
        QtWidgets.QPushButton, "pushButton_LogOnOff")
    if not settings.does_setting_exist('logOnOff'):
        settings.write_to_settings_file(
            'logOnOff', pushButton_LogOnOff.isChecked())
    else:
        pushButton_LogOnOff.setChecked(
            settings.read_from_settings_file('logOnOff') == 'True')
    pushButton_LogOnOff.setText(settings.read_from_settings_file('logOnOff'))


def bind_settings(MainWindow):
    # Log Frequency
    spinBox_logFrequency = MainWindow.findChild(
        QtWidgets.QSpinBox, "spinBox_logFrequency")
    spinBox_logFrequency.valueChanged.connect(
        lambda value: settings.write_to_settings_file('logFrequency', value))

    # File Size Limit
    spinBox_fileSizeLimit = MainWindow.findChild(
        QtWidgets.QSpinBox, "spinBox_fileSizeLimit")
    spinBox_fileSizeLimit.valueChanged.connect(
        lambda value: settings.write_to_settings_file('fileSizeLimit', value))

    # Log On/Off
    pushButton_LogOnOff = MainWindow.findChild(
        QtWidgets.QPushButton, "pushButton_LogOnOff")
    pushButton_LogOnOff.clicked.connect(
        lambda: settings.write_to_settings_file('logOnOff', pushButton_LogOnOff.isChecked()))
    pushButton_LogOnOff.clicked.connect(
        lambda: pushButton_LogOnOff.setText(settings.read_from_settings_file('logOnOff')))

def refresh_ports():
    listWidget_PortList = MainWindow.findChild(
        QtWidgets.QListView, "listWidget_PortList")
    listWidget_PortList.clear()
    item = QtWidgets.QListWidgetItem("Refreshing...")
    listWidget_PortList.addItem(item)
    ports = list_available_ports() 
    if not ports:
        listWidget_PortList.clear()
        item = QtWidgets.QListWidgetItem("No ports detected")
        listWidget_PortList.addItem(item)
    else:
        listWidget_PortList.clear()
        for port in ports:
            item = QtWidgets.QListWidgetItem(port)
            listWidget_PortList.addItem(item)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    MainWindow = loadUiWidget("GUI.ui")
    MainWindow.showFullScreen()
    MainWindow.showMaximized()

    # Settings
    settings = Settings()
    load_settings(MainWindow)
    bind_settings(MainWindow)

    # Logger
    timer = QTimer()
    spinBox_logFrequency = MainWindow.findChild(
        QtWidgets.QSpinBox, "spinBox_logFrequency")
    logFrequencyInMB = spinBox_logFrequency.value() * 1000
    timer.setInterval(logFrequencyInMB)
    values_to_log = [1, 2, 3]
    spinBox_fileSizeLimit = MainWindow.findChild(
        QtWidgets.QSpinBox, "spinBox_fileSizeLimit")
    fileSizeLimit = spinBox_fileSizeLimit.value()
    timer.timeout.connect(log_values(values_to_log, fileSizeLimit))
    timer.start()

    # Serial Link
    refresh_ports()
    pushButton_Refresh = MainWindow.findChild(
        QtWidgets.QPushButton, "pushButton_Refresh")
    pushButton_Refresh.clicked.connect(refresh_ports)
    
    sys.exit(app.exec())
