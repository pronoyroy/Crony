#! /usr/bin/python3

from PyQt4 import QtCore, QtGui
import threading

import desktop
import rbin
import tempfiles
import processes
import firefox
import chrome
import ie
import duplicates

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
        self.windows=[]                     #open window list
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(763, 519)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(763, 519))
        MainWindow.setMaximumSize(QtCore.QSize(763, 519))
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Logo/Logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabs = QtGui.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(140, 20, 591, 421))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        self.tabs.setObjectName(_fromUtf8("tabs"))
        self.tab_browsers = QtGui.QWidget()
        self.tab_browsers.setAccessibleName(_fromUtf8(""))
        self.tab_browsers.setObjectName(_fromUtf8("tab_browsers"))
        self.toolBox = QtGui.QToolBox(self.tab_browsers)
        self.toolBox.setGeometry(QtCore.QRect(0, 22, 591, 221))
        self.toolBox.setFrameShape(QtGui.QFrame.NoFrame)
        self.toolBox.setFrameShadow(QtGui.QFrame.Plain)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page_ff = QtGui.QWidget()
        self.page_ff.setGeometry(QtCore.QRect(0, 0, 591, 131))
        self.page_ff.setObjectName(_fromUtf8("page_ff"))
        self.cb_ff_cookies = QtGui.QCheckBox(self.page_ff)
        self.cb_ff_cookies.setGeometry(QtCore.QRect(19, 8, 161, 21))
        self.cb_ff_cookies.setObjectName(_fromUtf8("cb_ff_cookies"))
        self.cb_ff_history = QtGui.QCheckBox(self.page_ff)
        self.cb_ff_history.setGeometry(QtCore.QRect(19, 38, 151, 21))
        self.cb_ff_history.setObjectName(_fromUtf8("cb_ff_history"))
        self.cb_ff_tf = QtGui.QCheckBox(self.page_ff)
        self.cb_ff_tf.setGeometry(QtCore.QRect(20, 67, 151, 21))
        self.cb_ff_tf.setObjectName(_fromUtf8("cb_ff_tf"))
        self.img_ff = QtGui.QLabel(self.page_ff)
        self.img_ff.setGeometry(QtCore.QRect(452, 15, 111, 111))
        self.img_ff.setText(_fromUtf8(""))
        self.img_ff.setPixmap(QtGui.QPixmap(_fromUtf8(":/Background/firefox.png")))
        self.img_ff.setScaledContents(True)
        self.img_ff.setObjectName(_fromUtf8("img_ff"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Background/firefox.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_ff, icon1, _fromUtf8(""))
        self.page_gc = QtGui.QWidget()
        self.page_gc.setGeometry(QtCore.QRect(0, 0, 591, 131))
        self.page_gc.setObjectName(_fromUtf8("page_gc"))
        self.cb_gc_tf = QtGui.QCheckBox(self.page_gc)
        self.cb_gc_tf.setGeometry(QtCore.QRect(20, 69, 151, 21))
        self.cb_gc_tf.setObjectName(_fromUtf8("cb_gc_tf"))
        self.cb_gc_history = QtGui.QCheckBox(self.page_gc)
        self.cb_gc_history.setGeometry(QtCore.QRect(20, 40, 151, 21))
        self.cb_gc_history.setObjectName(_fromUtf8("cb_gc_history"))
        self.cb_gc_cookies = QtGui.QCheckBox(self.page_gc)
        self.cb_gc_cookies.setGeometry(QtCore.QRect(20, 10, 161, 21))
        self.cb_gc_cookies.setObjectName(_fromUtf8("cb_gc_cookies"))
        self.img_chrome = QtGui.QLabel(self.page_gc)
        self.img_chrome.setGeometry(QtCore.QRect(449, 10, 111, 111))
        self.img_chrome.setText(_fromUtf8(""))
        self.img_chrome.setPixmap(QtGui.QPixmap(_fromUtf8(":/Background/chrome.png")))
        self.img_chrome.setScaledContents(True)
        self.img_chrome.setObjectName(_fromUtf8("img_chrome"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Background/chrome.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_gc, icon2, _fromUtf8(""))
        self.page_ie = QtGui.QWidget()
        self.page_ie.setGeometry(QtCore.QRect(0, 0, 591, 131))
        self.page_ie.setObjectName(_fromUtf8("page_ie"))
        self.cb_ie_history = QtGui.QCheckBox(self.page_ie)
        self.cb_ie_history.setGeometry(QtCore.QRect(20, 42, 151, 21))
        self.cb_ie_history.setObjectName(_fromUtf8("cb_ie_history"))
        self.cb_ie_cookies = QtGui.QCheckBox(self.page_ie)
        self.cb_ie_cookies.setGeometry(QtCore.QRect(20, 12, 161, 21))
        self.cb_ie_cookies.setObjectName(_fromUtf8("cb_ie_cookies"))
        self.cb_ie_tf = QtGui.QCheckBox(self.page_ie)
        self.cb_ie_tf.setGeometry(QtCore.QRect(20, 71, 151, 21))
        self.cb_ie_tf.setObjectName(_fromUtf8("cb_ie_tf"))
        self.img_ie = QtGui.QLabel(self.page_ie)
        self.img_ie.setGeometry(QtCore.QRect(451, -11, 151, 151))
        self.img_ie.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255,10);"))
        self.img_ie.setText(_fromUtf8(""))
        self.img_ie.setPixmap(QtGui.QPixmap(_fromUtf8(":/Background/ie.png")))
        self.img_ie.setScaledContents(True)
        self.img_ie.setObjectName(_fromUtf8("img_ie"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/Background/ie.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_ie, icon3, _fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icon/browser.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabs.addTab(self.tab_browsers, icon4, _fromUtf8(""))
        self.tab_system = QtGui.QWidget()
        self.tab_system.setObjectName(_fromUtf8("tab_system"))
        self.cb_desktop = QtGui.QCheckBox(self.tab_system)
        self.cb_desktop.setGeometry(QtCore.QRect(30, 30, 181, 16))
        self.cb_desktop.setObjectName(_fromUtf8("cb_desktop"))
        self.cb_tempfiles = QtGui.QCheckBox(self.tab_system)
        self.cb_tempfiles.setGeometry(QtCore.QRect(30, 70, 161, 16))
        self.cb_tempfiles.setObjectName(_fromUtf8("cb_tempfiles"))
        self.cb_processes = QtGui.QCheckBox(self.tab_system)
        self.cb_processes.setGeometry(QtCore.QRect(30, 110, 201, 16))
        self.cb_processes.setObjectName(_fromUtf8("cb_processes"))
        self.cb_bin = QtGui.QCheckBox(self.tab_system)
        self.cb_bin.setGeometry(QtCore.QRect(30, 150, 181, 21))
        self.cb_bin.setObjectName(_fromUtf8("cb_bin"))
        self.img_system = QtGui.QLabel(self.tab_system)
        self.img_system.setGeometry(QtCore.QRect(440, 250, 111, 111))
        self.img_system.setText(_fromUtf8(""))
        self.img_system.setPixmap(QtGui.QPixmap(_fromUtf8(":/Background/PC.png")))
        self.img_system.setScaledContents(True)
        self.img_system.setObjectName(_fromUtf8("img_system"))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icon/notebook.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabs.addTab(self.tab_system, icon5, _fromUtf8(""))
        self.tab_files = QtGui.QWidget()
        self.tab_files.setObjectName(_fromUtf8("tab_files"))
        self.bt_duplicates = QtGui.QPushButton(self.tab_files)
        self.bt_duplicates.setGeometry(QtCore.QRect(174, 120, 251, 21))
        self.bt_duplicates.setObjectName(_fromUtf8("bt_duplicates"))
        self.bt_duplicates.clicked.connect(self.find_dupli) #duplicate button
        self.lbl_duplicateFiles = QtGui.QLabel(self.tab_files)
        self.lbl_duplicateFiles.setGeometry(QtCore.QRect(10, 20, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_duplicateFiles.setFont(font)
        self.lbl_duplicateFiles.setFrameShadow(QtGui.QFrame.Raised)
        self.lbl_duplicateFiles.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.lbl_duplicateFiles.setObjectName(_fromUtf8("lbl_duplicateFiles"))
        self.lbl_alert = QtGui.QLabel(self.tab_files)
        self.lbl_alert.setEnabled(True)
        self.lbl_alert.setGeometry(QtCore.QRect(20, 20, 531, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.lbl_alert.setPalette(palette)
        self.lbl_alert.setTextFormat(QtCore.Qt.PlainText)
        self.lbl_alert.setObjectName(_fromUtf8("lbl_alert"))
        self.img_files = QtGui.QLabel(self.tab_files)
        self.img_files.setGeometry(QtCore.QRect(440, 250, 111, 111))
        self.img_files.setText(_fromUtf8(""))
        self.img_files.setPixmap(QtGui.QPixmap(_fromUtf8(":/Background/files.png")))
        self.img_files.setScaledContents(True)
        self.img_files.setObjectName(_fromUtf8("img_files"))
        self.le_dir = QtGui.QLineEdit(self.tab_files)
        self.le_dir.setGeometry(QtCore.QRect(83, 90, 421, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_dir.sizePolicy().hasHeightForWidth())
        self.le_dir.setSizePolicy(sizePolicy)
        self.le_dir.setToolTip(_fromUtf8(""))
        self.le_dir.setStatusTip(_fromUtf8(""))
        self.le_dir.setWhatsThis(_fromUtf8(""))
        self.le_dir.setObjectName(_fromUtf8("le_dir"))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icon/file.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabs.addTab(self.tab_files, icon6, _fromUtf8(""))
        self.bt_apply = QtGui.QPushButton(self.centralwidget)
        self.bt_apply.setGeometry(QtCore.QRect(660, 455, 75, 23))
        self.bt_apply.setWhatsThis(_fromUtf8(""))
        self.bt_apply.setDefault(True)
        self.bt_apply.setFlat(False)
        self.bt_apply.setObjectName(_fromUtf8("bt_apply"))
        self.bt_apply.clicked.connect(self.apply_actions) #apply actions
        self.Background_icon = QtGui.QLabel(self.centralwidget)
        self.Background_icon.setGeometry(QtCore.QRect(-4, 327, 151, 151))
        self.Background_icon.setAutoFillBackground(False)
        self.Background_icon.setText(_fromUtf8(""))
        self.Background_icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/Background/back_image.png")))
        self.Background_icon.setScaledContents(True)
        self.Background_icon.setObjectName(_fromUtf8("Background_icon"))
        self.software_name = QtGui.QLabel(self.centralwidget)
        self.software_name.setGeometry(QtCore.QRect(-13, 2, 161, 141))
        self.software_name.setFrameShape(QtGui.QFrame.StyledPanel)
        self.software_name.setFrameShadow(QtGui.QFrame.Raised)
        self.software_name.setText(_fromUtf8(""))
        self.software_name.setPixmap(QtGui.QPixmap(_fromUtf8(":/Logo/name.png")))
        self.software_name.setScaledContents(True)
        self.software_name.setObjectName(_fromUtf8("software_name"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(-19, 492, 791, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.bt_all = QtGui.QPushButton(self.centralwidget)
        self.bt_all.setGeometry(QtCore.QRect(519, 455, 131, 23))
        self.bt_all.setObjectName(_fromUtf8("bt_all"))
        self.bt_all.clicked.connect(self.apply_all)   #all actions
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 763, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icon/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon7)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit.triggered.connect(self.close_application) #Exit function
        self.help = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icon/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help.setIcon(icon8)
        self.help.setObjectName(_fromUtf8("help"))
        self.actionAbout = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icon/about.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon9)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAbout.triggered.connect(self.open_about)     #open about
        self.help.triggered.connect(self.open_help)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.help)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        
        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def apply_actions(self):
        self.bt_apply.setEnabled(False)
        cky=0
        hist=0
        tf=0
        self.progressBar.setValue(5)
        msgbox=QtGui.QWidget()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Logo/Logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msgbox.setWindowIcon(icon)
        choice=QtGui.QMessageBox.question(msgbox,"Confirmation",
                                          "Are you sure, you want to proceed with the operations?",
                                          QtGui.QMessageBox.Yes|QtGui.QMessageBox.No|QtGui.QMessageBox.Cancel)

        if choice==QtGui.QMessageBox.Yes:
            if self.cb_desktop.isChecked():
                desktop.main()
                self.cb_desktop.toggle()
            self.progressBar.setValue(20)
            if self.cb_tempfiles.isChecked():
                tempfiles.main()
                self.cb_tempfiles.toggle()
            self.progressBar.setValue(30)
            if self.cb_processes.isChecked():
                processes.main()
                self.cb_processes.toggle()
            self.progressBar.setValue(40)
            if self.cb_bin.isChecked():
                rbin.main()
                self.cb_bin.toggle()
            self.progressBar.setValue(50)
            if self.cb_ff_cookies.isChecked():
                cky=1
                self.cb_ff_cookies.toggle()
            if self.cb_ff_history.isChecked():
                hist=1
                self.cb_ff_history.toggle()
            if self.cb_ff_tf.isChecked():
                tf=1
                self.cb_ff_tf.toggle()
            if cky==1 or hist==1 or tf==1:
                firefox.main(cky,hist,tf)
            self.progressBar.setValue(70)
            cky=hist=tf=0
            if self.cb_gc_cookies.isChecked():
                cky=1
                self.cb_gc_cookies.toggle()
            if self.cb_gc_history.isChecked():
                hist=1
                self.cb_gc_history.toggle()
            if self.cb_gc_tf.isChecked():
                tf=1
                self.cb_gc_tf.toggle()
            if cky==1 or hist==1 or tf==1:
                chrome.main(cky,hist,tf)
            self.progressBar.setValue(85)
            cky=hist=tf=0
            if self.cb_ie_cookies.isChecked():
                cky=1
                self.cb_ie_cookies.toggle()
            if self.cb_ie_history.isChecked():
                hist=1
                self.cb_ie_history.toggle()
            if self.cb_ie_tf.isChecked():
                tf=1
                self.cb_ie_tf.toggle()
            if cky==1 or hist==1 or tf==1:
                ie.main(cky,hist,tf)
            self.progressBar.setValue(100)
            cky=hist=tf=0
        elif choice==QtGui.QMessageBox.Cancel:
            if self.cb_desktop.isChecked():
                self.cb_desktop.toggle()
            if self.cb_tempfiles.isChecked():
                self.cb_tempfiles.toggle()
            if self.cb_processes.isChecked():
                self.cb_processes.toggle()
            if self.cb_bin.isChecked():
                self.cb_bin.toggle()
            if self.cb_ff_cookies.isChecked():
                self.cb_ff_cookies.toggle()
            if self.cb_ff_history.isChecked():
                self.cb_ff_history.toggle()
            if self.cb_ff_tf.isChecked():
                self.cb_ff_tf.toggle()
            if self.cb_gc_cookies.isChecked():
                self.cb_gc_cookies.toggle()
            if self.cb_gc_history.isChecked():
                self.cb_gc_history.toggle()
            if self.cb_gc_tf.isChecked():
                self.cb_gc_tf.toggle()
            if self.cb_ie_cookies.isChecked():
                self.cb_ie_cookies.toggle()
            if self.cb_ie_history.isChecked():
                self.cb_ie_history.toggle()
            if self.cb_ie_tf.isChecked():
                self.cb_ie_tf.toggle()
        else:
            pass
        self.bt_apply.setEnabled(True)
        self.progressBar.setValue(0)

    def apply_all(self):
        self.bt_all.setEnabled(False)
        if not self.cb_desktop.isChecked():
            self.cb_desktop.toggle()
        if not self.cb_tempfiles.isChecked():
            self.cb_tempfiles.toggle()
        if not self.cb_processes.isChecked():
            self.cb_processes.toggle()
        if not self.cb_bin.isChecked():
            self.cb_bin.toggle()
        if not self.cb_ff_cookies.isChecked():
            self.cb_ff_cookies.toggle()
        if not self.cb_ff_history.isChecked():
            self.cb_ff_history.toggle()
        if not self.cb_ff_tf.isChecked():
            self.cb_ff_tf.toggle()
        if not self.cb_gc_cookies.isChecked():
            self.cb_gc_cookies.toggle()
        if not self.cb_gc_history.isChecked():
            self.cb_gc_history.toggle()
        if not self.cb_gc_tf.isChecked():
            self.cb_gc_tf.toggle()
        if not self.cb_ie_cookies.isChecked():
            self.cb_ie_cookies.toggle()
        if not self.cb_ie_history.isChecked():
            self.cb_ie_history.toggle()
        if not self.cb_ie_tf.isChecked():
            self.cb_ie_tf.toggle()
        self.apply_actions()
        self.bt_all.setEnabled(True)

    def find_dupli(self):
        path=self.le_dir.text()
        msgbox=QtGui.QWidget()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Logo/Logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msgbox.setWindowIcon(icon)
        choice=QtGui.QMessageBox.question(msgbox,"Confirmation",
                                          "Are you sure, you want to proceed with the operation?",
                                          QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
        if choice==QtGui.QMessageBox.Yes:
            duplicates.main(path)
        else:
            pass
        
        
     
    def close_application(self):          #close
        self.windows[:]=[]
        sys.exit()

    def open_help(self):
        import Help
        helpDialog = QtGui.QDialog()
        helpUi = Help.Ui_Help()
        helpUi.setupUi(helpDialog)
        helpDialog.show()
        self.windows.append(helpDialog)   #list of open windows
        
    def open_about(self):
        import About
        aboutDialog = QtGui.QDialog()
        aboutUi = About.Ui_About()
        aboutUi.setupUi(aboutDialog)
        aboutDialog.show()
        self.windows.append(aboutDialog)   #list of open windows

        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Crony", None))
        self.tab_browsers.setToolTip(_translate("MainWindow", "<html><head/><body><p>Browser</p></body></html>", None))
        self.cb_ff_cookies.setText(_translate("MainWindow", "Clear Cookies", None))
        self.cb_ff_history.setText(_translate("MainWindow", "Clear History", None))
        self.cb_ff_tf.setText(_translate("MainWindow", "Clear Temporary Files", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_ff), _translate("MainWindow", "Mozilla Firefox", None))
        self.cb_gc_tf.setText(_translate("MainWindow", "Clear Temporary Files", None))
        self.cb_gc_history.setText(_translate("MainWindow", "Clear History", None))
        self.cb_gc_cookies.setText(_translate("MainWindow", "Clear Cookies", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_gc), _translate("MainWindow", "Google Chrome", None))
        self.cb_ie_history.setText(_translate("MainWindow", "Clear History", None))
        self.cb_ie_cookies.setText(_translate("MainWindow", "Clear Cookies", None))
        self.cb_ie_tf.setText(_translate("MainWindow", "Clear Temporary Files", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_ie), _translate("MainWindow", "Internet Explorer", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_browsers), _translate("MainWindow", "Browsers", None))
        self.cb_desktop.setText(_translate("MainWindow", "Clean Desktop", None))
        self.cb_tempfiles.setText(_translate("MainWindow", "Delete Temporary Files", None))
        self.cb_processes.setText(_translate("MainWindow", "Close Background Processes", None))
        self.cb_bin.setText(_translate("MainWindow", "Empty Recycle Bin", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_system), _translate("MainWindow", "System", None))
        self.bt_duplicates.setText(_translate("MainWindow", "Delete Duplicates", None))
        self.lbl_duplicateFiles.setText(_translate("MainWindow", "Delete duplicate files:", None))
        self.lbl_alert.setText(_translate("MainWindow", "Alert: Before continuing with this action, please note that all duplicate files in the PC (except C:) will be  \n"
"          permanently deleted and will be unrecoverable.  Do not continue if you are unsure with this action.", None))
        self.le_dir.setPlaceholderText(_translate("MainWindow", "Enter directory location", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_files), _translate("MainWindow", "Files", None))
        self.bt_apply.setText(_translate("MainWindow", "Apply", None))
        self.bt_all.setText(_translate("MainWindow", "Optimize PC", None))
        self.menuFile.setTitle(_translate("MainWindow", "Menu", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.help.setText(_translate("MainWindow", "Help", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))


import Resources

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    app.setQuitOnLastWindowClosed(False)
    MainWindow.show()
    sys.exit(app.exec_())

