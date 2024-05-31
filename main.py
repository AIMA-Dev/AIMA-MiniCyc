import os
import sys
from PySide6 import QtCore, QtWidgets, QtGui, QtUiTools
from PySide6.QtCore import QTimer
from scripts.settings import Settings
from scripts.logger import log_values, log_action
from scripts.devicesLink import list_all_devices
from datetime import datetime
import scripts.realTimePlot as realTimePlot


def loadUiWidget(uifilename, parent=None):
    """
    Loads a UI file and returns the corresponding widget.

    Parameters:
    - uifilename (str): The path to the UI file.
    - parent (QWidget): The parent widget (default: None).

    Returns:
    - QWidget: The loaded widget.

    """
    loader = QtUiTools.QUiLoader()
    uifile = QtCore.QFile(uifilename)
    uifile.open(QtCore.QFile.ReadOnly)
    ui = loader.load(uifile, parent)
    uifile.close()
    return ui


def load_settings(MainWindow):
    """
    Loads the settings for the application.

    Parameters:
    - MainWindow: The main window of the application.

    Returns:
    None
    """

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
    """
    Binds the settings of the MainWindow to the corresponding UI elements.

    Args:
        MainWindow: The main window object.

    Returns:
        None
    """
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
    pushButton_LogOnOff.clicked.connect(
        lambda: log_action("Logging is turned on" if pushButton_LogOnOff.isChecked() else "Logging is turned off"))


def refresh_ports():
    """
    Refreshes the list of available ports in the GUI.

    This function clears the existing list of ports in the GUI, retrieves the updated list of available ports,
    and populates the GUI list with the new ports. If no ports are detected, a message indicating that no ports
    were found is displayed in the GUI.

    Args:
        None

    Returns:
        None
    """
    listWidget_PortList = MainWindow.findChild(
        QtWidgets.QListView, "listWidget_PortList")
    listWidget_PortList.clear()
    item = QtWidgets.QListWidgetItem("Refreshing...")
    listWidget_PortList.addItem(item)
    ports = list_all_devices()
    if not ports:
        listWidget_PortList.clear()
        item = QtWidgets.QListWidgetItem("No device detected")
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

    # Resize tabWidget to screen size in width and 95% of screen size in height
    tabWidget = MainWindow.findChild(QtWidgets.QTabWidget, "tabWidget")
    tabWidget.resize(QtWidgets.QApplication.primaryScreen().availableSize())
    tabWidget.resize(MainWindow.width(), int(
        QtWidgets.QApplication.primaryScreen().availableSize().height() * 0.95))

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
    spinBox_fileSizeLimit = MainWindow.findChild(
        QtWidgets.QSpinBox, "spinBox_fileSizeLimit")
    fileSizeLimit = spinBox_fileSizeLimit.value()
    values_to_log = [datetime.now().strftime("%Y-%m-%d %H:%M:%S"),2,3]
    timer.timeout.connect(log_values(values_to_log, fileSizeLimit))
    timer.start()

    # Serial Link
    refresh_ports()
    pushButton_Refresh = MainWindow.findChild(
        QtWidgets.QPushButton, "pushButton_Refresh")
    pushButton_Refresh.clicked.connect(refresh_ports)

    # realTimePlot
    # Vacuum pump
    plot1 = realTimePlot.RealTimePlot("Plot 1", num_lines=2)
    plot1.start_animation()
    figure = plot1.figure
    listWidget_vacuum = MainWindow.findChild(
        QtWidgets.QListWidget, "listWidget_vacuum")
    item = QtWidgets.QListWidgetItem()
    item.setSizeHint(QtCore.QSize(0, 500))
    listWidget_vacuum.addItem(item)
    listWidget_vacuum.setItemWidget(item, figure.canvas)
    # Magnet
    plot2 = realTimePlot.RealTimePlot("Plot 2", num_lines=1)
    plot2.start_animation()
    figure = plot2.figure
    listWidget_magnet = MainWindow.findChild(
        QtWidgets.QListWidget, "listWidget_magnet")
    item = QtWidgets.QListWidgetItem()
    item.setSizeHint(QtCore.QSize(0, 500))
    listWidget_magnet.addItem(item)
    listWidget_magnet.setItemWidget(item, figure.canvas)

    sys.exit(app.exec())
# Développé avec ❤️ par : www.noasecond.com.
