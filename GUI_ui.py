# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDial, QFrame,
    QLCDNumber, QLabel, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QSpinBox, QStatusBar, QTabWidget, QToolButton,
    QWidget)
import Injection_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1920, 1080))
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.Injection = QWidget()
        self.Injection.setObjectName(u"Injection")
        self.label_2 = QLabel(self.Injection)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(730, 260, 598, 519))
        self.label_2.setPixmap(QPixmap(u":/newPrefix/Schema Injection.png"))
        self.tabWidget.addTab(self.Injection, "")
        self.Aimant = QWidget()
        self.Aimant.setObjectName(u"Aimant")
        self.Container_2 = QWidget(self.Aimant)
        self.Container_2.setObjectName(u"Container_2")
        self.Container_2.setGeometry(QRect(20, 20, 341, 111))
        self.frame_2 = QFrame(self.Container_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 20, 341, 91))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.numInput_3 = QWidget(self.frame_2)
        self.numInput_3.setObjectName(u"numInput_3")
        self.numInput_3.setGeometry(QRect(10, 10, 145, 61))
        self.label_4 = QLabel(self.numInput_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 83, 16))
        self.spinBox = QSpinBox(self.numInput_3)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(0, 20, 121, 41))
        self.spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.label_5 = QLabel(self.numInput_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(130, 40, 15, 16))
        self.afficheur = QWidget(self.frame_2)
        self.afficheur.setObjectName(u"afficheur")
        self.afficheur.setGeometry(QRect(180, 10, 145, 61))
        self.label_6 = QLabel(self.afficheur)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 83, 16))
        self.label_7 = QLabel(self.afficheur)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(130, 40, 15, 16))
        self.lcdNumber = QLCDNumber(self.afficheur)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(0, 20, 121, 41))
        self.lcdNumber.setSmallDecimalPoint(False)
        self.label_3 = QLabel(self.Container_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 161, 16))
        self.tabWidget.addTab(self.Aimant, "")
        self.RF = QWidget()
        self.RF.setObjectName(u"RF")
        self.Container_3 = QWidget(self.RF)
        self.Container_3.setObjectName(u"Container_3")
        self.Container_3.setGeometry(QRect(20, 20, 441, 181))
        self.frame_3 = QFrame(self.Container_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 20, 441, 161))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.numInput_4 = QWidget(self.frame_3)
        self.numInput_4.setObjectName(u"numInput_4")
        self.numInput_4.setGeometry(QRect(10, 10, 145, 61))
        self.label_8 = QLabel(self.numInput_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 0, 71, 16))
        self.spinBox_2 = QSpinBox(self.numInput_4)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(0, 20, 121, 41))
        self.spinBox_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.label_9 = QLabel(self.numInput_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(130, 40, 15, 16))
        self.numInput_5 = QWidget(self.frame_3)
        self.numInput_5.setObjectName(u"numInput_5")
        self.numInput_5.setGeometry(QRect(10, 90, 145, 61))
        self.label_10 = QLabel(self.numInput_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 0, 70, 16))
        self.spinBox_3 = QSpinBox(self.numInput_5)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setGeometry(QRect(0, 20, 121, 41))
        self.spinBox_3.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.label_11 = QLabel(self.numInput_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(130, 40, 15, 16))
        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(220, 20, 101, 41))
        self.label_13.setAutoFillBackground(False)
        self.label_13.setScaledContents(False)
        self.label_13.setWordWrap(True)
        self.dial = QDial(self.frame_3)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(350, 30, 71, 81))
        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(340, 110, 91, 41))
        self.label_14.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_14.setAutoFillBackground(False)
        self.label_14.setScaledContents(False)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_14.setWordWrap(True)
        self.progressBar = QProgressBar(self.frame_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(190, 26, 24, 121))
        self.progressBar.setAcceptDrops(False)
        self.progressBar.setValue(24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(Qt.Orientation.Vertical)
        self.progressBar.setTextDirection(QProgressBar.Direction.BottomToTop)
        self.label_12 = QLabel(self.Container_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 0, 161, 16))
        self.tabWidget.addTab(self.RF, "")
        self.Exxtraction = QWidget()
        self.Exxtraction.setObjectName(u"Exxtraction")
        self.Container_4 = QWidget(self.Exxtraction)
        self.Container_4.setObjectName(u"Container_4")
        self.Container_4.setGeometry(QRect(20, 20, 551, 281))
        self.frame_4 = QFrame(self.Container_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 20, 551, 261))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.label_19 = QLabel(self.frame_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 10, 37, 16))
        self.label_20 = QLabel(self.frame_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(300, 10, 37, 16))
        self.radioButton = QRadioButton(self.frame_4)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(10, 40, 92, 20))
        self.radioButton_2 = QRadioButton(self.frame_4)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(10, 80, 92, 20))
        self.radioButton_5 = QRadioButton(self.frame_4)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setGeometry(QRect(10, 120, 92, 20))
        self.numInput_6 = QWidget(self.frame_4)
        self.numInput_6.setObjectName(u"numInput_6")
        self.numInput_6.setGeometry(QRect(10, 160, 145, 91))
        self.label_15 = QLabel(self.numInput_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(0, 20, 71, 31))
        self.label_15.setWordWrap(True)
        self.spinBox_4 = QSpinBox(self.numInput_6)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setGeometry(QRect(0, 50, 121, 41))
        self.spinBox_4.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.label_16 = QLabel(self.numInput_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(130, 70, 15, 16))
        self.numInput_7 = QWidget(self.frame_4)
        self.numInput_7.setObjectName(u"numInput_7")
        self.numInput_7.setGeometry(QRect(300, 160, 145, 91))
        self.label_17 = QLabel(self.numInput_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(0, 20, 71, 31))
        self.label_17.setWordWrap(True)
        self.spinBox_5 = QSpinBox(self.numInput_7)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setGeometry(QRect(0, 50, 121, 41))
        self.spinBox_5.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.label_18 = QLabel(self.numInput_7)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(130, 70, 15, 16))
        self.radioButton_6 = QRadioButton(self.frame_4)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setGeometry(QRect(300, 40, 92, 20))
        self.radioButton_7 = QRadioButton(self.frame_4)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setGeometry(QRect(300, 80, 92, 20))
        self.radioButton_8 = QRadioButton(self.frame_4)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setGeometry(QRect(300, 120, 92, 20))
        self.afficheur_7 = QWidget(self.frame_4)
        self.afficheur_7.setObjectName(u"afficheur_7")
        self.afficheur_7.setGeometry(QRect(390, 40, 145, 31))
        self.label_48 = QLabel(self.afficheur_7)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(130, 10, 15, 16))
        self.lcdNumber_7 = QLCDNumber(self.afficheur_7)
        self.lcdNumber_7.setObjectName(u"lcdNumber_7")
        self.lcdNumber_7.setGeometry(QRect(0, 0, 111, 31))
        self.lcdNumber_7.setSmallDecimalPoint(False)
        self.afficheur_8 = QWidget(self.frame_4)
        self.afficheur_8.setObjectName(u"afficheur_8")
        self.afficheur_8.setGeometry(QRect(390, 80, 145, 31))
        self.label_49 = QLabel(self.afficheur_8)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(130, 10, 15, 16))
        self.lcdNumber_8 = QLCDNumber(self.afficheur_8)
        self.lcdNumber_8.setObjectName(u"lcdNumber_8")
        self.lcdNumber_8.setGeometry(QRect(0, 0, 111, 31))
        self.lcdNumber_8.setSmallDecimalPoint(False)
        self.afficheur_9 = QWidget(self.frame_4)
        self.afficheur_9.setObjectName(u"afficheur_9")
        self.afficheur_9.setGeometry(QRect(390, 120, 145, 31))
        self.label_50 = QLabel(self.afficheur_9)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(130, 10, 15, 16))
        self.lcdNumber_9 = QLCDNumber(self.afficheur_9)
        self.lcdNumber_9.setObjectName(u"lcdNumber_9")
        self.lcdNumber_9.setGeometry(QRect(0, 0, 111, 31))
        self.lcdNumber_9.setSmallDecimalPoint(False)
        self.label_21 = QLabel(self.Container_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(0, 0, 161, 16))
        self.afficheur_4 = QWidget(self.Exxtraction)
        self.afficheur_4.setObjectName(u"afficheur_4")
        self.afficheur_4.setGeometry(QRect(120, 80, 145, 31))
        self.label_45 = QLabel(self.afficheur_4)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(130, 10, 15, 16))
        self.lcdNumber_4 = QLCDNumber(self.afficheur_4)
        self.lcdNumber_4.setObjectName(u"lcdNumber_4")
        self.lcdNumber_4.setGeometry(QRect(0, 0, 111, 31))
        self.lcdNumber_4.setSmallDecimalPoint(False)
        self.afficheur_5 = QWidget(self.Exxtraction)
        self.afficheur_5.setObjectName(u"afficheur_5")
        self.afficheur_5.setGeometry(QRect(120, 120, 145, 31))
        self.label_46 = QLabel(self.afficheur_5)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(130, 10, 15, 16))
        self.lcdNumber_5 = QLCDNumber(self.afficheur_5)
        self.lcdNumber_5.setObjectName(u"lcdNumber_5")
        self.lcdNumber_5.setGeometry(QRect(0, 0, 111, 31))
        self.lcdNumber_5.setAutoFillBackground(False)
        self.lcdNumber_5.setSmallDecimalPoint(False)
        self.afficheur_6 = QWidget(self.Exxtraction)
        self.afficheur_6.setObjectName(u"afficheur_6")
        self.afficheur_6.setGeometry(QRect(120, 160, 145, 31))
        self.label_47 = QLabel(self.afficheur_6)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(130, 10, 15, 16))
        self.lcdNumber_6 = QLCDNumber(self.afficheur_6)
        self.lcdNumber_6.setObjectName(u"lcdNumber_6")
        self.lcdNumber_6.setGeometry(QRect(0, 0, 111, 31))
        self.lcdNumber_6.setSmallDecimalPoint(False)
        self.tabWidget.addTab(self.Exxtraction, "")
        self.Vide = QWidget()
        self.Vide.setObjectName(u"Vide")
        self.Container_8 = QWidget(self.Vide)
        self.Container_8.setObjectName(u"Container_8")
        self.Container_8.setGeometry(QRect(20, 20, 341, 111))
        self.frame_9 = QFrame(self.Container_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(0, 20, 341, 91))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.label_53 = QLabel(self.Container_8)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(0, 0, 161, 16))
        self.Container_9 = QWidget(self.Vide)
        self.Container_9.setObjectName(u"Container_9")
        self.Container_9.setGeometry(QRect(380, 20, 341, 111))
        self.frame_10 = QFrame(self.Container_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(0, 20, 341, 91))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.label_54 = QLabel(self.Container_9)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(0, 0, 161, 16))
        self.tabWidget.addTab(self.Vide, "")
        self.Eau = QWidget()
        self.Eau.setObjectName(u"Eau")
        self.tabWidget.addTab(self.Eau, "")
        self.Paramtres = QWidget()
        self.Paramtres.setObjectName(u"Paramtres")
        self.widget = QWidget(self.Paramtres)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 371, 284))
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 20, 371, 264))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_43 = QLabel(self.frame)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(10, 10, 99, 16))
        self.toolButton = QToolButton(self.frame)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(10, 30, 351, 31))
        self.toolButton.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        self.toolButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.toolButton.setArrowType(Qt.ArrowType.NoArrow)
        self.numInput_14 = QWidget(self.frame)
        self.numInput_14.setObjectName(u"numInput_14")
        self.numInput_14.setGeometry(QRect(10, 70, 149, 61))
        self.label_56 = QLabel(self.numInput_14)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(0, 0, 149, 16))
        self.spinBox_12 = QSpinBox(self.numInput_14)
        self.spinBox_12.setObjectName(u"spinBox_12")
        self.spinBox_12.setGeometry(QRect(0, 20, 121, 41))
        self.spinBox_12.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.label_57 = QLabel(self.numInput_14)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(130, 40, 19, 16))
        self.numInput_13 = QWidget(self.frame)
        self.numInput_13.setObjectName(u"numInput_13")
        self.numInput_13.setGeometry(QRect(10, 140, 148, 61))
        self.label_52 = QLabel(self.numInput_13)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(0, 0, 139, 16))
        self.spinBox_11 = QSpinBox(self.numInput_13)
        self.spinBox_11.setObjectName(u"spinBox_11")
        self.spinBox_11.setGeometry(QRect(0, 20, 121, 41))
        self.spinBox_11.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.label_55 = QLabel(self.numInput_13)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(130, 40, 18, 16))
        self.label_44 = QLabel(self.frame)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(10, 210, 197, 16))
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 230, 75, 24))
        self.pushButton.setCheckable(True)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 161, 16))
        icon = QIcon(QIcon.fromTheme(u"applications-development"))
        self.tabWidget.addTab(self.Paramtres, icon, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Injection), QCoreApplication.translate("MainWindow", u"Injection", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Courant bobine", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u00b5A", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Courant effectif", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u00b5A", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Bobine", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Aimant), QCoreApplication.translate("MainWindow", u"Aimant", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Amplificateur", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u00b5A", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Tension cr\u00eate", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"KV", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Position effective piston d'accord", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Position piston d'accord", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"RF", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RF), QCoreApplication.translate("MainWindow", u"RF", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Cible 1", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Cible 2", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Stripper 1", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Stripper 2", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"Stripper 3", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Rayon canne cible 1", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u00b5A", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Rayon canne cible 2", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u00b5A", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"Stripper 1", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"Stripper 2", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"Stripper 3", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"\u00b5A", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"\u00b5A", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"\u00b5A", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Cibles", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u00b5A", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"\u00b5A", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"\u00b5A", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Exxtraction), QCoreApplication.translate("MainWindow", u"Extraction", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Vide primaire", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Vide secondaire", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Vide), QCoreApplication.translate("MainWindow", u"Vide", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Eau), QCoreApplication.translate("MainWindow", u"Eau", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Chemin du dossier", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Fr\u00e9quence d'enregistrement", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Sec", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Limite de taille par fichiers", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Mb", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Activer l'enregistrement des donn\u00e9es", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enregistrement des donn\u00e9es", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Paramtres), QCoreApplication.translate("MainWindow", u"Param\u00e8tres", None))
    # retranslateUi

