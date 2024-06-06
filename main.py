import os
import sys
import ctypes
from PySide6 import QtCore, QtWidgets, QtGui, QtUiTools
from PySide6.QtCore import QTimer
from scripts.settings import Settings
from scripts.logger import log_values, log_action
from scripts.devicesLink import list_all_devices
from datetime import datetime
import scripts.realTimePlotting as realTimePlotting
import ctypes
import numpy as np
from picosdk.ps2000a import ps2000a as ps
from picosdk.functions import adc2mV, assert_pico_ok
import time
from scripts.deviceLibs.picoDevices import open_pico, get_value
import threading
import datetime
import time
import threading
import sys
import numpy as np


def set_app_user_model_id(app_id):
    """
    Sets the current process explicit AppUserModelID.

    Parameters:
    - app_id (str): The AppUserModelID to set.

    Returns:
    None
    """
    if os.name == 'nt':
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)


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


def bind_values_to_log(MainWindow):
    timer = QTimer(MainWindow)
    spinBox_logFrequency = MainWindow.findChild(
        QtWidgets.QSpinBox, "spinBox_logFrequency")
    logFrequencyInMS = spinBox_logFrequency.value() * 1000  # Convert to milliseconds
    timer.setInterval(logFrequencyInMS)
    spinBox_fileSizeLimit = MainWindow.findChild(
        QtWidgets.QSpinBox, "spinBox_fileSizeLimit")
    fileSizeLimit = spinBox_fileSizeLimit.value()

    def log_values_periodically():
        spinBox_RayonCanneC1 = MainWindow.findChild(
            QtWidgets.QSpinBox, "spinBox_RayonCanneC1")
        spinBox_RayonCanneC2 = MainWindow.findChild(
            QtWidgets.QSpinBox, "spinBox_RayonCanneC2")
        values_to_log = [
            datetime.datetime.now().strftime("%H:%M:%S"),
            spinBox_RayonCanneC1.value(),
            spinBox_RayonCanneC2.value()
        ]
        log_values(values_to_log, fileSizeLimit)

    timer.timeout.connect(log_values_periodically)
    timer.start()


def bind_actions_to_log(MainWindow):
    """
    Binds actions to log.

    Parameters:
    - MainWindow: The main window object.

    Returns:
    None
    """
    log_action("Application started")
    pushButton_LogOnOff = MainWindow.findChild(
        QtWidgets.QPushButton, "pushButton_LogOnOff")
    pushButton_LogOnOff.clicked.connect(
        lambda: log_action("Logging is turned on" if pushButton_LogOnOff.isChecked() else "Logging is turned off"))
    pushButton_Diaphragme = MainWindow.findChild(
        QtWidgets.QPushButton, "pushButton_Diaphragme")
    pushButton_Diaphragme.clicked.connect(
        lambda: log_action("Diaphragme is turned on" if pushButton_Diaphragme.isChecked() else "Diaphragme is turned off"))
    pushButton_Diaphragme.clicked.connect(
        lambda: pushButton_Diaphragme.setText("On" if pushButton_Diaphragme.isChecked() else "Off"))
    pushButton_Refresh = MainWindow.findChild(
        QtWidgets.QPushButton, "pushButton_Refresh")
    pushButton_Refresh.clicked.connect(
        lambda: log_action("Ports are refreshed"))
    radioButton_C1S1 = MainWindow.findChild(
        QtWidgets.QRadioButton, "radioButton_C1S1")
    radioButton_C1S1.clicked.connect(
        lambda: log_action("Cible 1 Stripper 1 is selected"))
    radioButton_C1S2 = MainWindow.findChild(
        QtWidgets.QRadioButton, "radioButton_C1S2")
    radioButton_C1S2.clicked.connect(
        lambda: log_action("Cible 1 Stripper 2 is selected"))
    radioButton_C1S3 = MainWindow.findChild(
        QtWidgets.QRadioButton, "radioButton_C1S3")
    radioButton_C1S3.clicked.connect(
        lambda: log_action("Cible 1 Stripper 3 is selected"))
    radioButton_C2S1 = MainWindow.findChild(
        QtWidgets.QRadioButton, "radioButton_C2S1")
    radioButton_C2S1.clicked.connect(
        lambda: log_action("Cible 2 Stripper 1 is selected"))
    radioButton_C2S2 = MainWindow.findChild(
        QtWidgets.QRadioButton, "radioButton_C2S2")
    radioButton_C2S2.clicked.connect(
        lambda: log_action("Cible 2 Stripper 2 is selected"))
    radioButton_C2S3 = MainWindow.findChild(
        QtWidgets.QRadioButton, "radioButton_C2S3")
    radioButton_C2S3.clicked.connect(
        lambda: log_action("Cible 2 Stripper 3 is selected"))


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
    listWidget_PortList = main_window.findChild(
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

def update_data(plot):
    """
    Updates the data for the given plot.

    Args:
        plot: The plot object to update.

    Returns:
        None
    """
    settings = Settings()
    while plot.running:
        plot.add_datas([get_value('PS2000A_CHANNEL_A')])
        freq = float(settings.read_from_settings_file('logFrequency'))
        time.sleep(freq)


def plotting(parent, title, num_of_lines, legend_labels):
    """
    Create a real-time plotting widget and start a separate thread to update the data.

    Args:
        parent: The parent widget.
        title: The title of the plot.
        num_of_lines: The number of lines to be plotted.
        legend_labels: The labels for the legend.

    Returns:
        None
    """
    plot = realTimePlotting.RealTimePlot(parent, title, num_of_lines, legend_labels)
    data_thread = threading.Thread(target=update_data, args=(plot,))
    data_thread.start()
    layout = QtWidgets.QVBoxLayout()
    parent.setLayout(layout)
    layout.addWidget(plot)

if __name__ == "__main__":
    set_app_user_model_id("aima.minicyc")
    app = QtWidgets.QApplication([])
    main_window = loadUiWidget("GUI.ui")
    main_window.setWindowTitle("MiniCyc")
    app_icon = QtGui.QIcon("assets/icon.ico")
    app.setWindowIcon(app_icon)
    main_window.showFullScreen()
    main_window.showMaximized()
    tabWidget = main_window.findChild(QtWidgets.QTabWidget, "tabWidget")
    tabWidget.setCurrentIndex(tabWidget.count() - 1)

    # Settings
    settings = Settings()
    load_settings(main_window)
    bind_settings(main_window)

    # Logger
    bind_actions_to_log(main_window)
    bind_values_to_log(main_window)

    # Devices
    refresh_ports()
    pushButton_Refresh = main_window.findChild(
        QtWidgets.QPushButton, "pushButton_Refresh")
    pushButton_Refresh.clicked.connect(refresh_ports)

    # realTimePlot
    open_pico()
    listWidget_vacuum = main_window.findChild(QtWidgets.QWidget, "listWidget_vacuum")
    plotting(listWidget_vacuum, "Pompe à vide", 1, ["Channel A"])

    sys.exit(app.exec())