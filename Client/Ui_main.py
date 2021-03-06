# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\Freenove\RaspberryPi\RaspberryPi Car\Python\PyQt_Test\main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(780, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(780, 600))
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/imgs/logo_Mini")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.btn_Up = QtGui.QPushButton(self.centralWidget)
        self.btn_Up.setGeometry(QtCore.QRect(560, 400, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        self.btn_Up.setFont(font)
        self.btn_Up.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_Up.setObjectName(_fromUtf8("btn_Up"))
        self.btn_Left = QtGui.QPushButton(self.centralWidget)
        self.btn_Left.setGeometry(QtCore.QRect(480, 440, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        self.btn_Left.setFont(font)
        self.btn_Left.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_Left.setObjectName(_fromUtf8("btn_Left"))
        self.btn_Down = QtGui.QPushButton(self.centralWidget)
        self.btn_Down.setGeometry(QtCore.QRect(560, 480, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        self.btn_Down.setFont(font)
        self.btn_Down.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_Down.setObjectName(_fromUtf8("btn_Down"))
        self.btn_Right = QtGui.QPushButton(self.centralWidget)
        self.btn_Right.setGeometry(QtCore.QRect(640, 440, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        self.btn_Right.setFont(font)
        self.btn_Right.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_Right.setObjectName(_fromUtf8("btn_Right"))
        self.slider_Camera = QtGui.QSlider(self.centralWidget)
        self.slider_Camera.setGeometry(QtCore.QRect(520, 350, 160, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.slider_Camera.setFont(font)
        self.slider_Camera.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider_Camera.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.slider_Camera.setMinimum(1)
        self.slider_Camera.setMaximum(30)
        self.slider_Camera.setProperty("value", 10)
        self.slider_Camera.setOrientation(QtCore.Qt.Horizontal)
        self.slider_Camera.setObjectName(_fromUtf8("slider_Camera"))
        self.btn_Forward = QtGui.QPushButton(self.centralWidget)
        self.btn_Forward.setGeometry(QtCore.QRect(110, 400, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        self.btn_Forward.setFont(font)
        self.btn_Forward.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_Forward.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.btn_Forward.setAcceptDrops(False)
        self.btn_Forward.setObjectName(_fromUtf8("btn_Forward"))
        self.btn_TurnLeft = QtGui.QPushButton(self.centralWidget)
        self.btn_TurnLeft.setGeometry(QtCore.QRect(30, 440, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        self.btn_TurnLeft.setFont(font)
        self.btn_TurnLeft.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_TurnLeft.setObjectName(_fromUtf8("btn_TurnLeft"))
        self.btn_TurnRight = QtGui.QPushButton(self.centralWidget)
        self.btn_TurnRight.setGeometry(QtCore.QRect(190, 440, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        self.btn_TurnRight.setFont(font)
        self.btn_TurnRight.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_TurnRight.setObjectName(_fromUtf8("btn_TurnRight"))
        self.btn_Backward = QtGui.QPushButton(self.centralWidget)
        self.btn_Backward.setGeometry(QtCore.QRect(110, 480, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        self.btn_Backward.setFont(font)
        self.btn_Backward.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_Backward.setObjectName(_fromUtf8("btn_Backward"))
        self.slider_Speed = QtGui.QSlider(self.centralWidget)
        self.slider_Speed.setGeometry(QtCore.QRect(280, 370, 22, 160))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.slider_Speed.setFont(font)
        self.slider_Speed.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider_Speed.setMaximum(100)
        self.slider_Speed.setProperty("value", 50)
        self.slider_Speed.setOrientation(QtCore.Qt.Vertical)
        self.slider_Speed.setObjectName(_fromUtf8("slider_Speed"))
        self.slider_Direction = QtGui.QSlider(self.centralWidget)
        self.slider_Direction.setGeometry(QtCore.QRect(70, 530, 160, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.slider_Direction.setFont(font)
        self.slider_Direction.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider_Direction.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.slider_Direction.setMinimum(10)
        self.slider_Direction.setMaximum(60)
        self.slider_Direction.setPageStep(5)
        self.slider_Direction.setProperty("value", 35)
        self.slider_Direction.setOrientation(QtCore.Qt.Horizontal)
        self.slider_Direction.setObjectName(_fromUtf8("slider_Direction"))
        self.label_tAngle = QtGui.QLabel(self.centralWidget)
        self.label_tAngle.setGeometry(QtCore.QRect(70, 560, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_tAngle.setFont(font)
        self.label_tAngle.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_tAngle.setObjectName(_fromUtf8("label_tAngle"))
        self.btn_Connect = QtGui.QPushButton(self.centralWidget)
        self.btn_Connect.setGeometry(QtCore.QRect(260, 330, 81, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        self.btn_Connect.setFont(font)
        self.btn_Connect.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_Connect.setIconSize(QtCore.QSize(64, 64))
        self.btn_Connect.setAutoRepeat(False)
        self.btn_Connect.setObjectName(_fromUtf8("btn_Connect"))
        self.logo = QtGui.QGraphicsView(self.centralWidget)
        self.logo.setEnabled(False)
        self.logo.setGeometry(QtCore.QRect(450, 10, 320, 180))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.logo.setFont(font)
        self.logo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.logo.setFrameShape(QtGui.QFrame.NoFrame)
        self.logo.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.logo.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.logo.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.logo.setForegroundBrush(brush)
        self.logo.setObjectName(_fromUtf8("logo"))
        self.label_Speed = QtGui.QLabel(self.centralWidget)
        self.label_Speed.setGeometry(QtCore.QRect(280, 560, 54, 12))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_Speed.setFont(font)
        self.label_Speed.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_Speed.setObjectName(_fromUtf8("label_Speed"))
        self.label_Scale = QtGui.QLabel(self.centralWidget)
        self.label_Scale.setGeometry(QtCore.QRect(470, 350, 31, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_Scale.setFont(font)
        self.label_Scale.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_Scale.setObjectName(_fromUtf8("label_Scale"))
        self.lcd_tAngle = QtGui.QLCDNumber(self.centralWidget)
        self.lcd_tAngle.setGeometry(QtCore.QRect(150, 550, 41, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lcd_tAngle.setFont(font)
        self.lcd_tAngle.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lcd_tAngle.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcd_tAngle.setFrameShadow(QtGui.QFrame.Raised)
        self.lcd_tAngle.setSmallDecimalPoint(False)
        self.lcd_tAngle.setNumDigits(2)
        self.lcd_tAngle.setDigitCount(2)
        self.lcd_tAngle.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_tAngle.setProperty("value", 35.0)
        self.lcd_tAngle.setProperty("intValue", 35)
        self.lcd_tAngle.setObjectName(_fromUtf8("lcd_tAngle"))
        self.lcd_Speed = QtGui.QLCDNumber(self.centralWidget)
        self.lcd_Speed.setGeometry(QtCore.QRect(260, 530, 51, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lcd_Speed.setFont(font)
        self.lcd_Speed.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcd_Speed.setFrameShadow(QtGui.QFrame.Raised)
        self.lcd_Speed.setNumDigits(3)
        self.lcd_Speed.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_Speed.setProperty("value", 50.0)
        self.lcd_Speed.setObjectName(_fromUtf8("lcd_Speed"))
        self.lineEdit_IP_Addr = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_IP_Addr.setEnabled(True)
        self.lineEdit_IP_Addr.setGeometry(QtCore.QRect(120, 330, 141, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lineEdit_IP_Addr.setFont(font)
        self.lineEdit_IP_Addr.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_IP_Addr.setObjectName(_fromUtf8("lineEdit_IP_Addr"))
        self.lcd_Scale = QtGui.QLCDNumber(self.centralWidget)
        self.lcd_Scale.setGeometry(QtCore.QRect(690, 340, 41, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lcd_Scale.setFont(font)
        self.lcd_Scale.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lcd_Scale.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcd_Scale.setNumDigits(2)
        self.lcd_Scale.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_Scale.setProperty("value", 10.0)
        self.lcd_Scale.setObjectName(_fromUtf8("lcd_Scale"))
        self.label_IP_Addr = QtGui.QLabel(self.centralWidget)
        self.label_IP_Addr.setGeometry(QtCore.QRect(10, 330, 101, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_IP_Addr.setFont(font)
        self.label_IP_Addr.setObjectName(_fromUtf8("label_IP_Addr"))
        self.webView = QtWebKit.QWebView(self.centralWidget)
        self.webView.setEnabled(True)
        self.webView.setGeometry(QtCore.QRect(10, 10, 400, 300))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.webView.setFont(font)
        self.webView.setFocusPolicy(QtCore.Qt.NoFocus)
        self.webView.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.webView.setAutoFillBackground(False)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setZoomFactor(1.20000004768)
        self.webView.setObjectName(_fromUtf8("webView"))
        self.btn_RGB_R = QtGui.QPushButton(self.centralWidget)
        self.btn_RGB_R.setGeometry(QtCore.QRect(340, 370, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        self.btn_RGB_R.setFont(font)
        self.btn_RGB_R.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_RGB_R.setObjectName(_fromUtf8("btn_RGB_R"))
        self.btn_RGB_G = QtGui.QPushButton(self.centralWidget)
        self.btn_RGB_G.setGeometry(QtCore.QRect(340, 400, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        self.btn_RGB_G.setFont(font)
        self.btn_RGB_G.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_RGB_G.setObjectName(_fromUtf8("btn_RGB_G"))
        self.btn_RGB_B = QtGui.QPushButton(self.centralWidget)
        self.btn_RGB_B.setGeometry(QtCore.QRect(340, 430, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        self.btn_RGB_B.setFont(font)
        self.btn_RGB_B.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_RGB_B.setObjectName(_fromUtf8("btn_RGB_B"))
        self.btn_Buzzer = QtGui.QPushButton(self.centralWidget)
        self.btn_Buzzer.setGeometry(QtCore.QRect(340, 460, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        self.btn_Buzzer.setFont(font)
        self.btn_Buzzer.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_Buzzer.setObjectName(_fromUtf8("btn_Buzzer"))
        self.slider_Camera_H = QtGui.QSlider(self.centralWidget)
        self.slider_Camera_H.setGeometry(QtCore.QRect(520, 530, 160, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.slider_Camera_H.setFont(font)
        self.slider_Camera_H.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider_Camera_H.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.slider_Camera_H.setMaximum(180)
        self.slider_Camera_H.setProperty("value", 90)
        self.slider_Camera_H.setOrientation(QtCore.Qt.Horizontal)
        self.slider_Camera_H.setObjectName(_fromUtf8("slider_Camera_H"))
        self.slider_Camera_V = QtGui.QSlider(self.centralWidget)
        self.slider_Camera_V.setGeometry(QtCore.QRect(730, 370, 22, 160))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.slider_Camera_V.setFont(font)
        self.slider_Camera_V.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider_Camera_V.setMaximum(180)
        self.slider_Camera_V.setProperty("value", 90)
        self.slider_Camera_V.setOrientation(QtCore.Qt.Vertical)
        self.slider_Camera_V.setObjectName(_fromUtf8("slider_Camera_V"))
        self.lcd_Camera_H = QtGui.QLCDNumber(self.centralWidget)
        self.lcd_Camera_H.setGeometry(QtCore.QRect(570, 550, 51, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lcd_Camera_H.setFont(font)
        self.lcd_Camera_H.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lcd_Camera_H.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcd_Camera_H.setFrameShadow(QtGui.QFrame.Raised)
        self.lcd_Camera_H.setSmallDecimalPoint(False)
        self.lcd_Camera_H.setNumDigits(3)
        self.lcd_Camera_H.setDigitCount(3)
        self.lcd_Camera_H.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_Camera_H.setProperty("value", 90.0)
        self.lcd_Camera_H.setProperty("intValue", 90)
        self.lcd_Camera_H.setObjectName(_fromUtf8("lcd_Camera_H"))
        self.lcd_Camera_V = QtGui.QLCDNumber(self.centralWidget)
        self.lcd_Camera_V.setGeometry(QtCore.QRect(710, 530, 51, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lcd_Camera_V.setFont(font)
        self.lcd_Camera_V.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lcd_Camera_V.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcd_Camera_V.setFrameShadow(QtGui.QFrame.Raised)
        self.lcd_Camera_V.setSmallDecimalPoint(False)
        self.lcd_Camera_V.setNumDigits(3)
        self.lcd_Camera_V.setDigitCount(3)
        self.lcd_Camera_V.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_Camera_V.setProperty("value", 90.0)
        self.lcd_Camera_V.setProperty("intValue", 90)
        self.lcd_Camera_V.setObjectName(_fromUtf8("lcd_Camera_V"))
        self.groupBox_Servo = QtGui.QGroupBox(self.centralWidget)
        self.groupBox_Servo.setGeometry(QtCore.QRect(450, 200, 291, 141))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.groupBox_Servo.setFont(font)
        self.groupBox_Servo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_Servo.setObjectName(_fromUtf8("groupBox_Servo"))
        self.slider_FineServo1 = QtGui.QSlider(self.groupBox_Servo)
        self.slider_FineServo1.setGeometry(QtCore.QRect(70, 20, 160, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.slider_FineServo1.setFont(font)
        self.slider_FineServo1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider_FineServo1.setMinimum(-10)
        self.slider_FineServo1.setMaximum(10)
        self.slider_FineServo1.setPageStep(1)
        self.slider_FineServo1.setOrientation(QtCore.Qt.Horizontal)
        self.slider_FineServo1.setObjectName(_fromUtf8("slider_FineServo1"))
        self.slider_FineServo2 = QtGui.QSlider(self.groupBox_Servo)
        self.slider_FineServo2.setGeometry(QtCore.QRect(70, 50, 160, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.slider_FineServo2.setFont(font)
        self.slider_FineServo2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider_FineServo2.setMinimum(-10)
        self.slider_FineServo2.setMaximum(10)
        self.slider_FineServo2.setPageStep(1)
        self.slider_FineServo2.setOrientation(QtCore.Qt.Horizontal)
        self.slider_FineServo2.setObjectName(_fromUtf8("slider_FineServo2"))
        self.slider_FineServo3 = QtGui.QSlider(self.groupBox_Servo)
        self.slider_FineServo3.setGeometry(QtCore.QRect(70, 80, 160, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.slider_FineServo3.setFont(font)
        self.slider_FineServo3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider_FineServo3.setMinimum(-10)
        self.slider_FineServo3.setMaximum(10)
        self.slider_FineServo3.setPageStep(1)
        self.slider_FineServo3.setOrientation(QtCore.Qt.Horizontal)
        self.slider_FineServo3.setObjectName(_fromUtf8("slider_FineServo3"))
        self.slider_FineServo4 = QtGui.QSlider(self.groupBox_Servo)
        self.slider_FineServo4.setGeometry(QtCore.QRect(70, 110, 160, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.slider_FineServo4.setFont(font)
        self.slider_FineServo4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider_FineServo4.setMinimum(-10)
        self.slider_FineServo4.setMaximum(10)
        self.slider_FineServo4.setPageStep(1)
        self.slider_FineServo4.setOrientation(QtCore.Qt.Horizontal)
        self.slider_FineServo4.setObjectName(_fromUtf8("slider_FineServo4"))
        self.label_FineServo_1 = QtGui.QLabel(self.groupBox_Servo)
        self.label_FineServo_1.setGeometry(QtCore.QRect(20, 20, 41, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_FineServo_1.setFont(font)
        self.label_FineServo_1.setObjectName(_fromUtf8("label_FineServo_1"))
        self.label_FineServo_2 = QtGui.QLabel(self.groupBox_Servo)
        self.label_FineServo_2.setGeometry(QtCore.QRect(20, 50, 41, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_FineServo_2.setFont(font)
        self.label_FineServo_2.setObjectName(_fromUtf8("label_FineServo_2"))
        self.label_FineServo_3 = QtGui.QLabel(self.groupBox_Servo)
        self.label_FineServo_3.setGeometry(QtCore.QRect(20, 80, 41, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_FineServo_3.setFont(font)
        self.label_FineServo_3.setObjectName(_fromUtf8("label_FineServo_3"))
        self.label_FineServo_4 = QtGui.QLabel(self.groupBox_Servo)
        self.label_FineServo_4.setGeometry(QtCore.QRect(20, 110, 41, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_FineServo_4.setFont(font)
        self.label_FineServo_4.setObjectName(_fromUtf8("label_FineServo_4"))
        self.lcd_FineServo_1 = QtGui.QLCDNumber(self.groupBox_Servo)
        self.lcd_FineServo_1.setGeometry(QtCore.QRect(240, 20, 41, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lcd_FineServo_1.setFont(font)
        self.lcd_FineServo_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lcd_FineServo_1.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcd_FineServo_1.setNumDigits(3)
        self.lcd_FineServo_1.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_FineServo_1.setProperty("value", 0.0)
        self.lcd_FineServo_1.setObjectName(_fromUtf8("lcd_FineServo_1"))
        self.lcd_FineServo_2 = QtGui.QLCDNumber(self.groupBox_Servo)
        self.lcd_FineServo_2.setGeometry(QtCore.QRect(240, 50, 41, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lcd_FineServo_2.setFont(font)
        self.lcd_FineServo_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lcd_FineServo_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcd_FineServo_2.setNumDigits(3)
        self.lcd_FineServo_2.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_FineServo_2.setProperty("value", 0.0)
        self.lcd_FineServo_2.setObjectName(_fromUtf8("lcd_FineServo_2"))
        self.lcd_FineServo_3 = QtGui.QLCDNumber(self.groupBox_Servo)
        self.lcd_FineServo_3.setGeometry(QtCore.QRect(240, 80, 41, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lcd_FineServo_3.setFont(font)
        self.lcd_FineServo_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lcd_FineServo_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcd_FineServo_3.setNumDigits(3)
        self.lcd_FineServo_3.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_FineServo_3.setProperty("value", 0.0)
        self.lcd_FineServo_3.setObjectName(_fromUtf8("lcd_FineServo_3"))
        self.lcd_FineServo_4 = QtGui.QLCDNumber(self.groupBox_Servo)
        self.lcd_FineServo_4.setGeometry(QtCore.QRect(240, 110, 41, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lcd_FineServo_4.setFont(font)
        self.lcd_FineServo_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lcd_FineServo_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcd_FineServo_4.setNumDigits(3)
        self.lcd_FineServo_4.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_FineServo_4.setProperty("value", 0.0)
        self.lcd_FineServo_4.setObjectName(_fromUtf8("lcd_FineServo_4"))
        self.btn_Home = QtGui.QPushButton(self.centralWidget)
        self.btn_Home.setGeometry(QtCore.QRect(570, 440, 55, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        self.btn_Home.setFont(font)
        self.btn_Home.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_Home.setObjectName(_fromUtf8("btn_Home"))
        self.btn_Mode = QtGui.QPushButton(self.centralWidget)
        self.btn_Mode.setGeometry(QtCore.QRect(340, 530, 151, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_Mode.setFont(font)
        self.btn_Mode.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_Mode.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_Mode.setObjectName(_fromUtf8("btn_Mode"))
        self.label_Mode = QtGui.QLabel(self.centralWidget)
        self.label_Mode.setGeometry(QtCore.QRect(370, 490, 91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(22)
        self.label_Mode.setFont(font)
        self.label_Mode.setObjectName(_fromUtf8("label_Mode"))
        self.wgt_Drawing = QtGui.QWidget(self.centralWidget)
        self.wgt_Drawing.setGeometry(QtCore.QRect(260, 10, 181, 121))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.wgt_Drawing.setFont(font)
        self.wgt_Drawing.setObjectName(_fromUtf8("wgt_Drawing"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.slider_Direction, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcd_tAngle.display)
        QtCore.QObject.connect(self.slider_Speed, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcd_Speed.display)
        QtCore.QObject.connect(self.slider_Camera, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcd_Scale.display)
        QtCore.QObject.connect(self.slider_Camera_H, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcd_Camera_H.display)
        QtCore.QObject.connect(self.slider_Camera_V, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcd_Camera_V.display)
        QtCore.QObject.connect(self.slider_FineServo1, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcd_FineServo_1.display)
        QtCore.QObject.connect(self.slider_FineServo2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcd_FineServo_2.display)
        QtCore.QObject.connect(self.slider_FineServo3, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcd_FineServo_3.display)
        QtCore.QObject.connect(self.slider_FineServo4, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcd_FineServo_4.display)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Freenove Client for Smart Car", None))
        self.btn_Up.setText(_translate("MainWindow", "UP", None))
        self.btn_Left.setText(_translate("MainWindow", "LEFT", None))
        self.btn_Down.setText(_translate("MainWindow", "DOWN", None))
        self.btn_Right.setText(_translate("MainWindow", "RIGHT", None))
        self.btn_Forward.setText(_translate("MainWindow", "FORWARD", None))
        self.btn_TurnLeft.setText(_translate("MainWindow", "TURN LEFT", None))
        self.btn_TurnRight.setText(_translate("MainWindow", "TURN RIGHT", None))
        self.btn_Backward.setText(_translate("MainWindow", "BACKWARD", None))
        self.label_tAngle.setText(_translate("MainWindow", "Turning angle", None))
        self.btn_Connect.setText(_translate("MainWindow", "Connect", None))
        self.label_Speed.setText(_translate("MainWindow", "Speed", None))
        self.label_Scale.setText(_translate("MainWindow", "Scale", None))
        self.label_IP_Addr.setText(_translate("MainWindow", "Server IP Address", None))
        self.btn_RGB_R.setText(_translate("MainWindow", "RGB_R", None))
        self.btn_RGB_G.setText(_translate("MainWindow", "RGB_G", None))
        self.btn_RGB_B.setText(_translate("MainWindow", "RGB_B", None))
        self.btn_Buzzer.setText(_translate("MainWindow", "Buzzer", None))
        self.groupBox_Servo.setTitle(_translate("MainWindow", "Servo Fine Tuning", None))
        self.label_FineServo_1.setText(_translate("MainWindow", "Servo1", None))
        self.label_FineServo_2.setText(_translate("MainWindow", "Servo2", None))
        self.label_FineServo_3.setText(_translate("MainWindow", "Servo3", None))
        self.label_FineServo_4.setText(_translate("MainWindow", "Servo4", None))
        self.btn_Home.setText(_translate("MainWindow", "HOME", None))
        self.btn_Mode.setText(_translate("MainWindow", "VIDEO", None))
        self.label_Mode.setText(_translate("MainWindow", "MODE", None))

from PyQt4 import QtWebKit
import fn_logo_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

