# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Danish\Documents\GitHub\Hazir-smart-attendance-management\src\frontend\password_confirmtion_pop_up.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_password_confirmation(object):
    def setupUi(self, password_confirmation):
        password_confirmation.setObjectName("password_confirmation")
        password_confirmation.resize(582, 111)
        password_confirmation.setStyleSheet("background-color:#fbeaeb;")
        self.ok_cancel_button = QtWidgets.QDialogButtonBox(password_confirmation)
        self.ok_cancel_button.setGeometry(QtCore.QRect(30, 70, 341, 32))
        self.ok_cancel_button.setStyleSheet("background-color:#2f3c7e")
        self.ok_cancel_button.setOrientation(QtCore.Qt.Horizontal)
        self.ok_cancel_button.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.ok_cancel_button.setObjectName("ok_cancel_button")
        self.password_inout_box = QtWidgets.QLineEdit(password_confirmation)
        self.password_inout_box.setGeometry(QtCore.QRect(0, 10, 581, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 60, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.password_inout_box.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_inout_box.setFont(font)
        self.password_inout_box.setStyleSheet("background-color:#2f3c7e;")
        self.password_inout_box.setText("")
        self.password_inout_box.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.password_inout_box.setObjectName("password_inout_box")

        self.retranslateUi(password_confirmation)
        self.ok_cancel_button.accepted.connect(password_confirmation.accept) # type: ignore
        self.ok_cancel_button.rejected.connect(password_confirmation.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(password_confirmation)

    def retranslateUi(self, password_confirmation):
        _translate = QtCore.QCoreApplication.translate
        password_confirmation.setWindowTitle(_translate("password_confirmation", "Dialog"))
        self.password_inout_box.setPlaceholderText(_translate("password_confirmation", "Enter password"))
