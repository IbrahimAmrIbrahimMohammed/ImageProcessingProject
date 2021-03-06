'''
@author: Ibrahim Amr

'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1880, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1880, 800))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.gridLayoutWidget = QtWidgets.QWidget(MainWindow)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1881, 791))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.LoadComputrizedImage = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LoadComputrizedImage.setFont(font)
        self.LoadComputrizedImage.setObjectName("LoadComputrizedImage")
        self.horizontalLayout_5.addWidget(self.LoadComputrizedImage)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.LoadHandWrittenImage = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LoadHandWrittenImage.setFont(font)
        self.LoadHandWrittenImage.setObjectName("LoadHandWrittenImage")
        self.horizontalLayout_5.addWidget(self.LoadHandWrittenImage)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 1, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.gridLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.Original_img = QtWidgets.QLabel(self.scrollArea)
        self.Original_img.setGeometry(QtCore.QRect(0, 0, 55, 16))
        self.Original_img.setText("")
        self.Original_img.setObjectName("Original_img")
        self.scrollArea.setWidget(self.Original_img)
        self.gridLayout.addWidget(self.scrollArea, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 3, 2, 1, 1)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.gridLayoutWidget)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.Predicted_img = QtWidgets.QLabel(self.scrollArea_2)
        self.Predicted_img.setGeometry(QtCore.QRect(0, 0, 55, 16))
        self.Predicted_img.setText("")
        self.Predicted_img.setObjectName("Predicted_img")
        self.scrollArea_2.setWidget(self.Predicted_img)
        self.gridLayout.addWidget(self.scrollArea_2, 2, 4, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Original_ZoomIn = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Original_ZoomIn.setFont(font)
        self.Original_ZoomIn.setObjectName("Original_ZoomIn")
        self.horizontalLayout.addWidget(self.Original_ZoomIn)
        self.Original_ZoomOut = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Original_ZoomOut.setFont(font)
        self.Original_ZoomOut.setObjectName("Original_ZoomOut")
        self.horizontalLayout.addWidget(self.Original_ZoomOut)
        self.Original_AutoFit = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Original_AutoFit.setFont(font)
        self.Original_AutoFit.setObjectName("Original_AutoFit")
        self.horizontalLayout.addWidget(self.Original_AutoFit)
        self.Original_NormalSize = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Original_NormalSize.setFont(font)
        self.Original_NormalSize.setObjectName("Original_NormalSize")
        self.horizontalLayout.addWidget(self.Original_NormalSize)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.GenerateVerilog = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.GenerateVerilog.setFont(font)
        self.GenerateVerilog.setObjectName("GenerateVerilog")
        self.horizontalLayout_3.addWidget(self.GenerateVerilog)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 2, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)
        self.loopBackArrow_ColorLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.loopBackArrow_ColorLabel.setMinimumSize(QtCore.QSize(100, 21))
        self.loopBackArrow_ColorLabel.setText("")
        self.loopBackArrow_ColorLabel.setObjectName("loopBackArrow_ColorLabel")
        self.gridLayout_2.addWidget(self.loopBackArrow_ColorLabel, 2, 0, 1, 1)
        self.stateCondition_ColorLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.stateCondition_ColorLabel.setMinimumSize(QtCore.QSize(100, 21))
        self.stateCondition_ColorLabel.setText("")
        self.stateCondition_ColorLabel.setObjectName("stateCondition_ColorLabel")
        self.gridLayout_2.addWidget(self.stateCondition_ColorLabel, 4, 0, 1, 1)
        self.arrowHead_ColorLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.arrowHead_ColorLabel.setMinimumSize(QtCore.QSize(100, 21))
        self.arrowHead_ColorLabel.setText("")
        self.arrowHead_ColorLabel.setObjectName("arrowHead_ColorLabel")
        self.gridLayout_2.addWidget(self.arrowHead_ColorLabel, 3, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 4, 1, 1, 1)
        self.arrow_ColorLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.arrow_ColorLabel.setMinimumSize(QtCore.QSize(100, 21))
        self.arrow_ColorLabel.setText("")
        self.arrow_ColorLabel.setObjectName("arrow_ColorLabel")
        self.gridLayout_2.addWidget(self.arrow_ColorLabel, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 5, 1, 1, 1)
        self.slash_ColorLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.slash_ColorLabel.setMinimumSize(QtCore.QSize(100, 21))
        self.slash_ColorLabel.setText("")
        self.slash_ColorLabel.setObjectName("slash_ColorLabel")
        self.gridLayout_2.addWidget(self.slash_ColorLabel, 5, 0, 1, 1)
        self.state_ColorLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.state_ColorLabel.setMinimumSize(QtCore.QSize(100, 21))
        self.state_ColorLabel.setText("")
        self.state_ColorLabel.setObjectName("state_ColorLabel")
        self.gridLayout_2.addWidget(self.state_ColorLabel, 0, 0, 1, 1)
        self.numbers_ColorLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.numbers_ColorLabel.setMinimumSize(QtCore.QSize(100, 21))
        self.numbers_ColorLabel.setText("")
        self.numbers_ColorLabel.setObjectName("numbers_ColorLabel")
        self.gridLayout_2.addWidget(self.numbers_ColorLabel, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 6, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Predict = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Predict.setFont(font)
        self.Predict.setObjectName("Predict")
        self.verticalLayout_3.addWidget(self.Predict)
        self.CheckConnection = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.CheckConnection.setFont(font)
        self.CheckConnection.setObjectName("CheckConnection")
        self.verticalLayout_3.addWidget(self.CheckConnection)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem8, 5, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 1, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 2, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem11, 0, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Predicted_Export = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Predicted_Export.setFont(font)
        self.Predicted_Export.setObjectName("Predicted_Export")
        self.horizontalLayout_2.addWidget(self.Predicted_Export)
        spacerItem12 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.Predicted_RemoveAnchor = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Predicted_RemoveAnchor.setFont(font)
        self.Predicted_RemoveAnchor.setCheckable(True)
        self.Predicted_RemoveAnchor.setObjectName("Predicted_RemoveAnchor")
        self.horizontalLayout_2.addWidget(self.Predicted_RemoveAnchor)
        self.Predicted_AddAnchor = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Predicted_AddAnchor.setFont(font)
        self.Predicted_AddAnchor.setCheckable(True)
        self.Predicted_AddAnchor.setObjectName("Predicted_AddAnchor")
        self.horizontalLayout_2.addWidget(self.Predicted_AddAnchor)
        spacerItem13 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem13)
        self.Predicted_NormalSize = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Predicted_NormalSize.setFont(font)
        self.Predicted_NormalSize.setObjectName("Predicted_NormalSize")
        self.horizontalLayout_2.addWidget(self.Predicted_NormalSize)
        self.Predicted_AutoFit = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Predicted_AutoFit.setFont(font)
        self.Predicted_AutoFit.setObjectName("Predicted_AutoFit")
        self.horizontalLayout_2.addWidget(self.Predicted_AutoFit)
        self.Predicted_ZoomOut = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Predicted_ZoomOut.setFont(font)
        self.Predicted_ZoomOut.setObjectName("Predicted_ZoomOut")
        self.horizontalLayout_2.addWidget(self.Predicted_ZoomOut)
        self.Predicted_ZoomIn = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Predicted_ZoomIn.setFont(font)
        self.Predicted_ZoomIn.setObjectName("Predicted_ZoomIn")
        self.horizontalLayout_2.addWidget(self.Predicted_ZoomIn)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 4, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem14, 7, 2, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem15, 2, 5, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setEnabled(True)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 120))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 120))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("")
        self.textEdit.setUndoRedoEnabled(False)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 6, 1, 1, 4)

        MainWindow.setCentralWidget(self.gridLayoutWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LoadComputrizedImage.setText(_translate("MainWindow", "Load Computrized Image"))
        self.LoadHandWrittenImage.setText(_translate("MainWindow", "Load Hand-Written Image"))
        self.Original_ZoomIn.setText(_translate("MainWindow", "Zoom In"))
        self.Original_ZoomOut.setText(_translate("MainWindow", "Zoom Out"))
        self.Original_AutoFit.setText(_translate("MainWindow", "Auto Fit"))
        self.Original_NormalSize.setText(_translate("MainWindow", "Normal Size"))
        self.GenerateVerilog.setText(_translate("MainWindow", "Generate Verilog file"))
        self.label_8.setText(_translate("MainWindow", "Loop back Arrow"))
        self.label_4.setText(_translate("MainWindow", "State"))
        self.label_10.setText(_translate("MainWindow", "Arrow Head"))
        self.label_12.setText(_translate("MainWindow", "State Condition"))
        self.label_6.setText(_translate("MainWindow", "Arrow"))
        self.label_14.setText(_translate("MainWindow", "/"))
        self.label_2.setText(_translate("MainWindow", "Numbers"))
        self.Predict.setText(_translate("MainWindow", "Predict"))
        self.CheckConnection.setText(_translate("MainWindow", "Check Connection"))
        self.Predicted_Export.setText(_translate("MainWindow", "Export"))
        self.Predicted_RemoveAnchor.setText(_translate("MainWindow", "Remove Anchor"))
        self.Predicted_AddAnchor.setText(_translate("MainWindow", "Add Anchor"))
        self.Predicted_NormalSize.setText(_translate("MainWindow", "Normal Size"))
        self.Predicted_AutoFit.setText(_translate("MainWindow", "Auto Fit"))
        self.Predicted_ZoomOut.setText(_translate("MainWindow", "Zoom Out"))
        self.Predicted_ZoomIn.setText(_translate("MainWindow", "Zoom In"))

        self.state_ColorLabel.setStyleSheet("background-color:#5059D9;")
        self.arrow_ColorLabel.setStyleSheet("background-color:#FFBD1B;")
        self.loopBackArrow_ColorLabel.setStyleSheet("background-color:#FF00FF;")
        self.arrowHead_ColorLabel.setStyleSheet("background-color:#40DFF9;")
        self.stateCondition_ColorLabel.setStyleSheet("background-color:#FF0032;")
        self.slash_ColorLabel.setStyleSheet("background-color:#00FF00;")
        self.numbers_ColorLabel.setStyleSheet("background-color:#2449a6;")
        self.textEdit.setReadOnly(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
