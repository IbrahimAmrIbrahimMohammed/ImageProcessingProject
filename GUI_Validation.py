'''
@author: Ibrahim Amr

'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Validation.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

global log
global labelImage
global imageDefaultSize
global imageCurrentSize

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(885, 630)
        Dialog.setMinimumSize(QtCore.QSize(885, 630))
        Dialog.setMaximumSize(QtCore.QSize(885, 630))
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 881, 631))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 6, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 200))
        self.textEdit.setObjectName("textEdit")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.gridLayout.addWidget(self.textEdit, 5, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(25, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.NormalSize = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.NormalSize.setObjectName("NormalSize")
        self.horizontalLayout.addWidget(self.NormalSize)
        self.AutoFit = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.AutoFit.setObjectName("AutoFit")
        self.horizontalLayout.addWidget(self.AutoFit)
        self.ZoomOut = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ZoomOut.setObjectName("ZoomOut")
        self.horizontalLayout.addWidget(self.ZoomOut)
        self.ZoomIn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ZoomIn.setObjectName("ZoomIn")
        self.horizontalLayout.addWidget(self.ZoomIn)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.gridLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.label = QtWidgets.QLabel(self.scrollArea)
        self.label.setGeometry(QtCore.QRect(0, 0, 55, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.scrollArea.setWidget(self.label)
        self.gridLayout.addWidget(self.scrollArea, 2, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.NormalSize.setText(_translate("Dialog", "Normal Size"))
        self.AutoFit.setText(_translate("Dialog", "Auto Fit"))
        self.ZoomOut.setText(_translate("Dialog", "Zoom Out"))
        self.ZoomIn.setText(_translate("Dialog", "Zoom In"))

        self.signals()

        self.textEdit.setReadOnly(True)

    def signals(self):
        '''
        function set events of different GUI buttons
        :param self:
        :return: void
        '''
        self.ZoomIn.clicked.connect(self.imageZoomIn)
        self.ZoomOut.clicked.connect(self.imageZoomOut)
        self.NormalSize.clicked.connect(self.imageNormalSize)
        self.AutoFit.clicked.connect(self.imageAutoFit)

    def loadImage(self, extLog, extImage):
        '''
        load image
        :param extLog: log information
        :param extImage: image
        :return: nothing
        '''
        global log, labelImage, imageDefaultSize, imageCurrentSize
        log = extLog
        labelImage = extImage

        self.textEdit.setText(log)

        height, width, channel = labelImage.shape
        bytesPerLine = 3 * width
        labelImage = QImage(labelImage.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()

        originalPixImage = QPixmap.fromImage(labelImage)
        imageDefaultSize = [originalPixImage.size().width(), originalPixImage.size().height()]
        imageCurrentSize = imageDefaultSize.copy()
        self.label.setFixedSize(originalPixImage.size())
        self.label.setPixmap(originalPixImage)

    def imageZoomIn(self):
        '''
        zoom in image
        :param self:
        :return: void
        '''
        global labelImage, imageCurrentSize
        imageCurrentSize[0] = (int)(imageCurrentSize[0] * 1.15)
        imageCurrentSize[1] = (int)(imageCurrentSize[1] * 1.15)
        originalPixImage = QPixmap.fromImage(labelImage)
        originalPixImage = originalPixImage.scaled(imageCurrentSize[0], imageCurrentSize[1], Qt.IgnoreAspectRatio,
                                                   Qt.SmoothTransformation)
        self.label.setFixedSize(originalPixImage.size())
        self.label.setPixmap(originalPixImage)

    def imageZoomOut(self):
        '''
        zoom out image
        :param self:
        :return: void
        '''
        global labelImage, imageCurrentSize
        imageCurrentSize[0] = (int)(imageCurrentSize[0] * 0.9)
        imageCurrentSize[1] = (int)(imageCurrentSize[1] * 0.9)
        originalPixImage = QPixmap.fromImage(labelImage)
        originalPixImage = originalPixImage.scaled(imageCurrentSize[0], imageCurrentSize[1], Qt.IgnoreAspectRatio,
                                                   Qt.SmoothTransformation)
        self.label.setFixedSize(originalPixImage.size())
        self.label.setPixmap(originalPixImage)

    def imageNormalSize(self):
        '''
        set image to normal size
        :param self:
        :return: void
        '''
        global labelImage, imageCurrentSize, imageDefaultSize
        imageCurrentSize = imageDefaultSize.copy()
        originalPixImage = QPixmap.fromImage(labelImage)
        self.label.setFixedSize(originalPixImage.size())
        self.label.setPixmap(originalPixImage)

    def imageAutoFit(self):
        '''
        fit image to window size
        :param self:
        :return: void
        '''
        global labelImage, imageCurrentSize
        imageCurrentSize[0] = self.scrollArea.width() - 22
        imageCurrentSize[1] = self.scrollArea.height() - 22
        originalPixImage = QPixmap.fromImage(labelImage)
        originalPixImage = originalPixImage.scaled(imageCurrentSize[0], imageCurrentSize[1], Qt.IgnoreAspectRatio,
                                                   Qt.SmoothTransformation)
        self.label.setFixedSize(originalPixImage.size())
        self.label.setPixmap(originalPixImage)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
