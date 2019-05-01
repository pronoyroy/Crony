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

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName(_fromUtf8("About"))
        About.resize(372, 493)
        About.setMinimumSize(QtCore.QSize(372, 493))
        About.setMaximumSize(QtCore.QSize(372, 493))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Logo/Logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        About.setWindowIcon(icon)
        self.logo = QtGui.QLabel(About)
        self.logo.setGeometry(QtCore.QRect(80, 27, 211, 171))
        self.logo.setText(_fromUtf8(""))
        self.logo.setPixmap(QtGui.QPixmap(_fromUtf8(":/Logo/name.png")))
        self.logo.setScaledContents(True)
        self.logo.setObjectName(_fromUtf8("logo"))
        self.bt_help = QtGui.QPushButton(About)
        self.bt_help.setGeometry(QtCore.QRect(150, 430, 75, 23))
        self.bt_help.setObjectName(_fromUtf8("bt_close"))
        def open_help(self):
            import Help
            global helpDialog 
            helpDialog = QtGui.QDialog()
            helpUi = Help.Ui_Help()
            helpUi.setupUi(helpDialog)
            helpDialog.show()
        self.bt_help.clicked.connect(open_help) #close button
        self.version_info = QtGui.QLabel(About)
        self.version_info.setGeometry(QtCore.QRect(146, 193, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.version_info.setFont(font)
        self.version_info.setObjectName(_fromUtf8("version_info"))
        self.label_3 = QtGui.QLabel(About)
        self.label_3.setGeometry(QtCore.QRect(30, 234, 311, 111))
        self.label_3.setFrameShadow(QtGui.QFrame.Raised)
        self.label_3.setMidLineWidth(1)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(_translate("About", "About", None))
        self.bt_help.setWhatsThis(_translate("About", "<html><head/><body><p>Open Help</p></body></html>", None))
        self.bt_help.setText(_translate("About", "Help", None))
        self.version_info.setWhatsThis(_translate("About", "<html><head/><body><p>Version of Crony</p></body></html>", None))
        self.version_info.setText(_translate("About", "Version 1.1", None))
        self.label_3.setText(_translate("About", "Crony is a file and folder cleaning and management for removing unnessary content from the system. Thus, providing a smooth and seamless computing experience.", None))

    

import Resources

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    About = QtGui.QDialog()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())

