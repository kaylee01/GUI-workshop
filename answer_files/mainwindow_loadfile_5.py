# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QMenuBar, QPlainTextEdit, QSizePolicy,
    QSlider, QStatusBar, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(482, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.slice_label = QLabel(self.centralwidget)
        self.slice_label.setObjectName(u"slice_label")
        self.slice_label.setMaximumSize(QSize(16777215, 10))
        self.slice_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.slice_label, 3, 1, 1, 1)

        self.path_text = QPlainTextEdit(self.centralwidget)
        self.path_text.setObjectName(u"path_text")
        self.path_text.setMaximumSize(QSize(16777215, 25))
        self.path_text.setReadOnly(True)

        self.gridLayout.addWidget(self.path_text, 1, 1, 1, 1)

        self.select_file = QToolButton(self.centralwidget)
        self.select_file.setObjectName(u"select_file")

        self.gridLayout.addWidget(self.select_file, 1, 0, 1, 1)

        self.scan_view = QLabel(self.centralwidget)
        self.scan_view.setObjectName(u"scan_view")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scan_view.sizePolicy().hasHeightForWidth())
        self.scan_view.setSizePolicy(sizePolicy)
        self.scan_view.setMinimumSize(QSize(300, 300))
        self.scan_view.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.scan_view, 2, 0, 1, 2)

        self.slice_slider = QSlider(self.centralwidget)
        self.slice_slider.setObjectName(u"slice_slider")
        self.slice_slider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.slice_slider, 4, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 482, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.slice_label.setText(QCoreApplication.translate("MainWindow", u"Slice: -", None))
        self.path_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"No file selected", None))
        self.select_file.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.scan_view.setText("")
    # retranslateUi

