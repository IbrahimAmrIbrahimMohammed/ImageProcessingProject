'''
@author: Ibrahim Amr

file controls el main GUI window
'''

##################################### Modified in GUI_Design file #####################################
#                                                                                                     #
# remove : self.scrollAreaWidgetContents = QtWidgets.QWidget()                                        #
# remove : self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 399, 199))                    #
# remove : self.scrollAreaWidgetContents.setAutoFillBackground(True)                                  #
# remove : self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")                    #
# remove : self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)                               #
# add    : self.label = QtWidgets.QLabel(self.scrollArea)                                             #
# add    : self.scrollArea.setWidget(self.label)                                                      #
#                                                                                                     #
# remove : self.centralwidget = QtWidgets.QWidget(MainWindow)                                         #
# remove : self.centralwidget.setObjectName("centralwidget")                                          #
# remove : self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)                              #
# add    : self.gridLayoutWidget = QtWidgets.QWidget(MainWindow)                                      #
# add    : MainWindow.setCentralWidget(self.gridLayoutWidget)                                         #
#                                                                                                     #
# add    : self.state_ColorLabel.setStyleSheet("background-color:#5059D9;")                           #
# add    : self.arrow_ColorLabel.setStyleSheet("background-color:#FFBD1B;")                           #
# add    : self.loopBackArrow_ColorLabel.setStyleSheet("background-color:#FF00FF;")                   #
# add    : self.arrowHead_ColorLabel.setStyleSheet("background-color:#40DFF9;")                       #
# add    : self.stateCondition_ColorLabel.setStyleSheet("background-color:#FF0032;")                  #
# add    : self.slash_ColorLabel.setStyleSheet("background-color:#00FF00;")                           #
#######################################################################################################


from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import Qt
from GUI_Design import *
from PyQt5.QtGui import QPixmap, QImage
import addAnchorDialog
import GUI_Validation
from utils import matching

from utils import image_operations
from utils import object_file
from utils import log_config

import predict
import transactionToVerilog
global fileName
global originalImage
global originalDefaultSize
global originalCurrentSize

global predictedImage
global predictedDefaultSize
global predictedCurrentSize


def setPredictedImage(img):
    '''
    function set the value of global variable predicatedImage
    :param img: input image
    :return: void
    '''
    global predictedImage
    predictedImage = img

def getPredictedImage():
    '''
    function returns the value of global variable predicatedImage
    :return: image
    '''
    global predictedImage
    return predictedImage

def signals(self):
    '''
    function set events of different GUI buttons
    :param self:
    :return: void
    '''
    self.LoadComputrizedImage.clicked.connect(self.loadComputrized)
    self.LoadHandWrittenImage.clicked.connect(self.loadHandWritten)
    
    self.Predict.clicked.connect(self.predictObjects)
    self.Predicted_Export.clicked.connect(self.exportPredictedImage)
    self.CheckConnection.clicked.connect(self.CheckConnectionValidation)

    self.GenerateVerilog.clicked.connect(self.Generate_VeriLog_Code)

    self.Predicted_RemoveAnchor.clicked.connect(self.deleteAnchor)
    self.Predicted_AddAnchor.clicked.connect(self.addNewAnchor)

    self.Predicted_img.mousePressEvent = self.Predicted_img_mousePress
    self.Predicted_img.mouseReleaseEvent = self.Predicted_img_mouseRelease

    self.Original_ZoomIn.clicked.connect(self.originalZoomIn)
    self.Original_ZoomOut.clicked.connect(self.originalZoomOut)
    self.Original_NormalSize.clicked.connect(self.originalNormalSize)
    self.Original_AutoFit.clicked.connect(self.originalAutoFit)

    self.Predicted_ZoomIn.clicked.connect(self.predictedZoomIn)
    self.Predicted_ZoomOut.clicked.connect(self.predictedZoomOut)
    self.Predicted_NormalSize.clicked.connect(self.predictedNormalSize)
    self.Predicted_AutoFit.clicked.connect(self.predictedAutoFit)


def start(self):
    '''
    function initialize GUI and parameters
    :param self:
    :return: void
    '''
    setAllDisabled(self)
    predict.first_step_config()
    self.textEdit.setText(log_config.start_up_log())

def setAllDisabled(self):
    '''
    function disable GUI buttons in first use
    :param self:
    :return: void
    '''
    self.Original_ZoomIn.setEnabled(False)
    self.Original_ZoomOut.setEnabled(False)
    self.Original_AutoFit.setEnabled(False)
    self.Original_NormalSize.setEnabled(False)

    self.Predicted_ZoomIn.setEnabled(False)
    self.Predicted_ZoomOut.setEnabled(False)
    self.Predicted_AutoFit.setEnabled(False)
    self.Predicted_NormalSize.setEnabled(False)
    self.Predicted_AddAnchor.setEnabled(False)
    self.Predicted_RemoveAnchor.setEnabled(False)
    self.Predicted_Export.setEnabled(False)

    self.Predict.setEnabled(False)
    self.CheckConnection.setEnabled(False)
    self.GenerateVerilog.setEnabled(False)

def loadComputrized(self):
    object_file.hand_written = False
    self.loadOriginalImage()

def loadHandWritten(self):
    object_file.hand_written = True
    self.loadOriginalImage()

def loadOriginalImage(self):
    '''
    function load image of state machine to the GUI
    :param self:
    :return: void
    '''
    global originalImage, originalDefaultSize, originalCurrentSize, fileName

    setAllDisabled(self)
    self.Predicted_img.clear()

    options = QFileDialog.Options()
    # fileName = QFileDialog.getOpenFileName(self, "Open File", QDir.currentPath())
    fileName, _ = QFileDialog.getOpenFileName(MainWindow, 'QFileDialog.getOpenFileName()', '',
                                              'Images (*.png *.jpeg *.jpg)', options=options)
    if fileName:
        originalImage = QImage(fileName)
        if originalImage.isNull():
            QMessageBox.information(self, "Image Viewer", "Cannot load %s." % fileName)
            return

        originalPixImage = QPixmap.fromImage(originalImage)
        originalDefaultSize = [originalPixImage.size().width(), originalPixImage.size().height()]
        originalCurrentSize = originalDefaultSize.copy()
        self.Original_img.setFixedSize(originalPixImage.size())
        self.Original_img.setPixmap(originalPixImage)

        self.Original_ZoomIn.setEnabled(True)
        self.Original_ZoomOut.setEnabled(True)
        self.Original_AutoFit.setEnabled(True)
        self.Original_NormalSize.setEnabled(True)

        self.Predict.setEnabled(True)

        self.Predicted_ZoomIn.setEnabled(False)
        self.Predicted_ZoomOut.setEnabled(False)
        self.Predicted_AutoFit.setEnabled(False)
        self.Predicted_NormalSize.setEnabled(False)
        self.Predicted_AddAnchor.setEnabled(False)
        self.Predicted_RemoveAnchor.setEnabled(False)
        self.Predicted_Export.setEnabled(False)

        self.CheckConnection.setEnabled(False)
        self.GenerateVerilog.setEnabled(False)


def predictObjects(self):
    global predictedDefaultSize, predictedCurrentSize
    '''
    function run predict and load predicted image to GUI
    :param self:
    :return: void
    '''
    predict.reset_object_file()
    text = predict.predict_main(fileName)

    predictedDefaultSize = [1600, 1200]
    predictedCurrentSize = predictedDefaultSize.copy()

    self.set_Predicted_img()

    self.textEdit.setText(self.textEdit.toPlainText() + text)
    self.textEdit.moveCursor(QtGui.QTextCursor.End)

    self.Predicted_ZoomIn.setEnabled(True)
    self.Predicted_ZoomOut.setEnabled(True)
    self.Predicted_AutoFit.setEnabled(True)
    self.Predicted_NormalSize.setEnabled(True)
    self.Predicted_AddAnchor.setEnabled(True)
    self.Predicted_RemoveAnchor.setEnabled(True)
    self.Predicted_Export.setEnabled(True)

    self.CheckConnection.setEnabled(True)

    self.GenerateVerilog.setEnabled(False)


def CheckConnectionValidation(self):
    '''
    function run automatic check to validate predict
    :param self:
    :return: void
    '''


    matching.connect_anchors()
    a, b, c = matching.connect_transactions()

    if (a == -1):
        Dialog = QtWidgets.QDialog()
        ui2 = GUI_Validation.Ui_Dialog()
        ui2.setupUi(Dialog)
        ui2.loadImage(b, c)
        Dialog.exec()

    elif (a == 1):
        self.textEdit.setText(self.textEdit.toPlainText() + b)
        self.textEdit.moveCursor(QtGui.QTextCursor.End)
        self.set_Predicted_img()
        self.GenerateVerilog.setEnabled(True)


def exportPredictedImage(self):
    '''
    function export el predicted image to be saved on computer
    :param self:
    :return: void
    '''
    options = QFileDialog.Options()
    # options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getSaveFileName(MainWindow, "QFileDialog.getSaveFileName()", "", 'Images (*.png *.jpeg *.jpg)',
                                              options=options)

    if fileName:
        image_operations.set_output_path(fileName)
        image_operations.export_image()


def deleteAnchor(self):
    '''
    function change cursor and disable button of add anchors
    :param self:
    :return: void
    '''
    if(self.Predicted_RemoveAnchor.isChecked()):
        self.Predicted_img.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Predicted_AddAnchor.setEnabled(False)
    else:
        self.Predicted_img.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Predicted_AddAnchor.setEnabled(True)

def addNewAnchor(self):
    '''
    function change cursor and disable button of remove anchors
    :param self:
    :return: void
    '''
    if (self.Predicted_AddAnchor.isChecked()):
        self.Predicted_img.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.Predicted_RemoveAnchor.setEnabled(False)
    else:
        self.Predicted_img.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Predicted_RemoveAnchor.setEnabled(True)

def Predicted_img_mousePress(self, event):
    '''
    function get mouse press position, run remove anchor functions if remove anchor button pressed, save coordinates in case of add anchor
    :param self:
    :param event: mouse event
    :return: void
    '''
    global predictedCurrentSize, predictedDefaultSize

    x = event.pos().x() * (predictedDefaultSize[0] / predictedCurrentSize[0])
    y = event.pos().y() * (predictedDefaultSize[1] / predictedCurrentSize[1])

    if (self.Predicted_RemoveAnchor.isChecked()):
        element_name, remove_header, remove_element=image_operations.get_element_with_x_and_y(x,y)
        if remove_element== None:
            pass
        else:
            reply=QMessageBox.question(MainWindow, 'message', "are you sure you want remove "+element_name, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if int(reply)==16384:
                #yes equal to 16384
                text = (image_operations.remove_element(remove_header, remove_element))
                self.textEdit.setText(self.textEdit.toPlainText() + text)
                self.textEdit.moveCursor(QtGui.QTextCursor.End)
                self.GenerateVerilog.setEnabled(False)
            self.set_Predicted_img()

    if (self.Predicted_AddAnchor.isChecked()):
        self.initial_X = x
        self.initial_Y = y


def Predicted_img_mouseRelease(self, event):
    '''
    function get mouse press position, run add anchor functions if add anchor button pressed
    :param self:
    :param event: mouse event
    :return: void
    '''
    global predictedCurrentSize, predictedDefaultSize

    if (self.Predicted_AddAnchor.isChecked()):
        x = event.pos().x() * (predictedDefaultSize[0] / predictedCurrentSize[0])
        y = event.pos().y() * (predictedDefaultSize[1] / predictedCurrentSize[1])

        Dialog = QtWidgets.QDialog()
        ui3 = addAnchorDialog.Ui_Dialog()
        ui3.setupUi(Dialog)
        Dialog.exec()


        if (int(self.initial_X) < int(x)):
            minX = int(self.initial_X)
            maxX = int(x)
        else:
            minX = int(x)
            maxX = int(self.initial_X)

        if (int(self.initial_Y) < int(y)):
            minY = int(self.initial_Y)
            maxY = int(y)
        else:
            minY = int(y)
            maxY = int(self.initial_Y)

        if (object_file.anchorDialogResult == 1):
            text=""
            if (object_file.anchorDialogChoice == "State"):
                text=image_operations.add_element(minX, minY, maxX, maxY, "state")
            elif (object_file.anchorDialogChoice == "State Condition"):
                text=image_operations.add_element(minX, minY, maxX, maxY, "state condition")
            elif (object_file.anchorDialogChoice == "Arrow"):
                text=image_operations.add_element(minX, minY, maxX, maxY, "curved arrow")
            elif (object_file.anchorDialogChoice == "Arrow Head"):
                text=image_operations.add_element(minX, minY, maxX, maxY, "arrow head")
            elif (object_file.anchorDialogChoice == "Loop Back Arrow"):
                text=image_operations.add_element(minX, minY, maxX, maxY, "loop back arrow")
            else:
                text=image_operations.add_element(minX, minY, maxX, maxY, object_file.anchorDialogChoice)

            self.textEdit.setText(self.textEdit.toPlainText() + text)
            self.textEdit.moveCursor(QtGui.QTextCursor.End)
            self.set_Predicted_img()
            self.GenerateVerilog.setEnabled(False)

def set_Predicted_img(self):
    '''
    function load predicted image into GUI
    :param self:
    :return: void
    '''
    global predictedCurrentSize, predictedDefaultSize

    height, width, channel = object_file.image.shape
    bytesPerLine = 3 * width
    _img = QImage(object_file.image.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped().copy()
    setPredictedImage(_img)
    predictedPixImage = QPixmap.fromImage(getPredictedImage())
    predictedPixImage = predictedPixImage.scaled(predictedCurrentSize[0], predictedCurrentSize[1], Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
    self.Predicted_img.setFixedSize(predictedPixImage.size())
    self.Predicted_img.setPixmap(predictedPixImage)


def originalZoomIn(self):
    '''
    zoom in original image
    :param self:
    :return: void
    '''
    global originalImage, originalCurrentSize
    originalCurrentSize[0] = (int)(originalCurrentSize[0] * 1.15)
    originalCurrentSize[1] = (int)(originalCurrentSize[1] * 1.15)
    originalPixImage = QPixmap.fromImage(originalImage)
    originalPixImage = originalPixImage.scaled(originalCurrentSize[0], originalCurrentSize[1], Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
    self.Original_img.setFixedSize(originalPixImage.size())
    self.Original_img.setPixmap(originalPixImage)


def originalZoomOut(self):
    '''
    zoom out original image
    :param self: 
    :return: void
    '''
    global originalImage, originalCurrentSize
    originalCurrentSize[0] = (int)(originalCurrentSize[0] * 0.9)
    originalCurrentSize[1] = (int)(originalCurrentSize[1] * 0.9)
    originalPixImage = QPixmap.fromImage(originalImage)
    originalPixImage = originalPixImage.scaled(originalCurrentSize[0], originalCurrentSize[1], Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
    self.Original_img.setFixedSize(originalPixImage.size())
    self.Original_img.setPixmap(originalPixImage)


def originalNormalSize(self):
    '''
    set original image to normal size
    :param self: 
    :return: void
    '''
    global originalImage, originalCurrentSize, originalDefaultSize
    originalCurrentSize = originalDefaultSize.copy()
    originalPixImage = QPixmap.fromImage(originalImage)
    self.Original_img.setFixedSize(originalPixImage.size())
    self.Original_img.setPixmap(originalPixImage)

def originalAutoFit(self):
    '''
    fit original image to window size
    :param self: 
    :return: void
    '''
    global originalImage, originalCurrentSize
    originalCurrentSize[0] = self.scrollArea.width() - 22
    originalCurrentSize[1] = self.scrollArea.height() - 22
    originalPixImage = QPixmap.fromImage(originalImage)
    originalPixImage = originalPixImage.scaled(originalCurrentSize[0], originalCurrentSize[1], Qt.IgnoreAspectRatio,
                                               Qt.SmoothTransformation)
    self.Original_img.setFixedSize(originalPixImage.size())
    self.Original_img.setPixmap(originalPixImage)




def predictedZoomIn(self):
    '''
    zoom in predicted image
    :param self: 
    :return: void
    '''
    global  predictedCurrentSize
    predictedCurrentSize[0] = (int)(predictedCurrentSize[0] * 1.15)
    predictedCurrentSize[1] = (int)(predictedCurrentSize[1] * 1.15)
    predictedPixImage = QPixmap.fromImage(getPredictedImage())
    predictedPixImage = predictedPixImage.scaled(predictedCurrentSize[0], predictedCurrentSize[1], Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
    self.Predicted_img.setFixedSize(predictedPixImage.size())
    self.Predicted_img.setPixmap(predictedPixImage)

def predictedZoomOut(self):
    '''
    zoom out predicted image
    :param self: 
    :return: void
    '''
    global predictedCurrentSize
    predictedCurrentSize[0] = (int)(predictedCurrentSize[0] * 0.9)
    predictedCurrentSize[1] = (int)(predictedCurrentSize[1] * 0.9)
    predictedPixImage = QPixmap.fromImage(getPredictedImage())
    predictedPixImage = predictedPixImage.scaled(predictedCurrentSize[0], predictedCurrentSize[1], Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
    self.Predicted_img.setFixedSize(predictedPixImage.size())
    self.Predicted_img.setPixmap(predictedPixImage)

def predictedNormalSize(self):
    '''
    set predicted image to normal size
    :param self: 
    :return: void
    '''
    global predictedCurrentSize, predictedDefaultSize
    predictedCurrentSize = predictedDefaultSize.copy()
    predictedPixImage = QPixmap.fromImage(getPredictedImage())
    self.Predicted_img.setFixedSize(predictedPixImage.size())
    self.Predicted_img.setPixmap(predictedPixImage)


def predictedAutoFit(self):
    '''
    fit predicted image to window size
    :param self: 
    :return: void
    '''
    global predictedCurrentSize
    predictedCurrentSize[0] = self.scrollArea_2.width() - 22
    predictedCurrentSize[1] = self.scrollArea_2.height() - 22
    predictedPixImage = QPixmap.fromImage(getPredictedImage())
    predictedPixImage = predictedPixImage.scaled(predictedCurrentSize[0], predictedCurrentSize[1], Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
    self.Predicted_img.setFixedSize(predictedPixImage.size())
    self.Predicted_img.setPixmap(predictedPixImage)


def Generate_VeriLog_Code(self):
    '''
    runs generate verilog functions
    :param self: 
    :return: void
    '''
    text=transactionToVerilog.transactionToVerilog("Module_0",object_file.transaction)
    self.textEdit.setText(self.textEdit.toPlainText() + text)
    self.textEdit.moveCursor(QtGui.QTextCursor.End)
















# def openImg(self):
#     options = QFileDialog.Options()
#     # fileName = QFileDialog.getOpenFileName(self, "Open File", QDir.currentPath())
#     fileName, _ = QFileDialog.getOpenFileName(MainWindow, 'QFileDialog.getOpenFileName()', '',
#                                               'Images (*.png *.jpeg *.jpg)', options=options)
#     if fileName:
#         global predictedImage, originalDefaultSize, predictedCurrentSize
#         predictedImage = QImage(fileName)
#         if predictedImage.isNull():
#             QMessageBox.information(self, "Image Viewer", "Cannot load %s." % fileName)
#             return
#
#
#         originalPixImage = QPixmap.fromImage(predictedImage)
#         originalDefaultSize = [originalPixImage.size().width() , originalPixImage.size().height()]
#         predictedCurrentSize = originalDefaultSize.copy()
#         print(predictedCurrentSize)
#         self.Predicted_img.setFixedSize(originalPixImage.size())
#         self.Predicted_img.setPixmap(originalPixImage)


'''
set function to be part of GUI_Design file
'''
Ui_MainWindow.signals = signals

Ui_MainWindow.start = start
Ui_MainWindow.setAllDisabled = setAllDisabled

Ui_MainWindow.setPredictedImage = setPredictedImage
Ui_MainWindow.getPredictedImage = getPredictedImage


Ui_MainWindow.loadOriginalImage = loadOriginalImage
Ui_MainWindow.loadComputrized = loadComputrized
Ui_MainWindow.loadHandWritten = loadHandWritten
Ui_MainWindow.predictObjects = predictObjects
Ui_MainWindow.exportPredictedImage = exportPredictedImage
Ui_MainWindow.set_Predicted_img = set_Predicted_img
Ui_MainWindow.CheckConnectionValidation = CheckConnectionValidation

Ui_MainWindow.Generate_VeriLog_Code = Generate_VeriLog_Code

Ui_MainWindow.addNewAnchor = addNewAnchor
Ui_MainWindow.deleteAnchor = deleteAnchor

Ui_MainWindow.Predicted_img_mousePress = Predicted_img_mousePress
Ui_MainWindow.Predicted_img_mouseRelease = Predicted_img_mouseRelease

#Ui_MainWindow.openImg = openImg


Ui_MainWindow.originalZoomIn = originalZoomIn
Ui_MainWindow.originalZoomOut = originalZoomOut
Ui_MainWindow.originalNormalSize = originalNormalSize
Ui_MainWindow.originalAutoFit = originalAutoFit

Ui_MainWindow.predictedZoomIn = predictedZoomIn
Ui_MainWindow.predictedZoomOut = predictedZoomOut
Ui_MainWindow.predictedNormalSize = predictedNormalSize
Ui_MainWindow.predictedAutoFit = predictedAutoFit

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    start(ui)
    MainWindow.show()

    #openImg(ui)

    sys.exit(app.exec_())
