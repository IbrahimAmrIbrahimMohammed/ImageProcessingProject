'''
@author: sara khaled 

'''

# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'addAnchorDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from utils import object_file

global dialog_dump



def set_the_dialog_id(dialog_input):
    '''
    description : taking the id of the input dialog
    :param dialog_input:
    :return:
    '''
    global dialog_dump
    dialog_dump=dialog_input

def get_the_dialog_id():
    '''
    discription : return the id of the dialog
    :return:
    '''
    global dialog_dump
    return dialog_dump

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        set_the_dialog_id(Dialog)

        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 200)
        Dialog.setMinimumSize(QtCore.QSize(400, 200))
        Dialog.setMaximumSize(QtCore.QSize(400, 200))
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(150, 90, 211, 22))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 160, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 160, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.label.setText(_translate("Dialog", "Please choose the right anchor :"))
        self.label_2.setText(_translate("Dialog", "Anchors"))

        self.comboBox.addItem("0")
        self.comboBox.addItem("1")
        self.comboBox.addItem("2")
        self.comboBox.addItem("3")
        self.comboBox.addItem("4")
        self.comboBox.addItem("5")
        self.comboBox.addItem("6")
        self.comboBox.addItem("7")
        self.comboBox.addItem("8")
        self.comboBox.addItem("9")
        self.comboBox.addItem("/")
        self.comboBox.addItem("Arrow")
        self.comboBox.addItem("Loop Back Arrow")
        self.comboBox.addItem("Arrow Head")
        self.comboBox.addItem("State")
        self.comboBox.addItem("State Condition")

        self.signals()

    def signals(self):
        '''
        function set events of different GUI buttons
        :param self:
        :return: void
        '''
        self.pushButton.clicked.connect(self.Done)
        self.pushButton_2.clicked.connect(self.Cancelled)



    def Done(self):
        '''
        function set global anchor variables in main file (addAnchorResult -> 1, addAnchorChoice -> combobox choice),then close dialog
        :return:
        '''
        object_file.anchorDialogResult = 1
        object_file.anchorDialogChoice = str(self.comboBox.currentText())
        get_the_dialog_id().close()


    def Cancelled(self):
        '''
        function set global anchor variables in main file (addAnchorResult -> -1, addAnchorChoice -> ''),then close dialog
        :return:
        '''
        object_file.anchorDialogResult = -1
        object_file.anchorDialogChoice = ''
        get_the_dialog_id().close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
