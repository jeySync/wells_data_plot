# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQT_RasterDraw\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RasterEditorWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionRectangle = QtWidgets.QAction(MainWindow)
        self.actionRectangle.setCheckable(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/tool_bar/tool_rectangle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/tool_bar/tool_rectangle.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/tool_bar/tool_rectangle.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/tool_bar/tool_rectangle.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/tool_bar/tool_rectangle.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/tool_bar/tool_rectangle.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/tool_bar/tool_rectangle.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/tool_bar/tool_rectangle.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.actionRectangle.setIcon(icon)
        self.actionRectangle.setObjectName("actionRectangle")
        self.actionEllipse = QtWidgets.QAction(MainWindow)
        self.actionEllipse.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/tool_bar/tool_ellipse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEllipse.setIcon(icon1)
        self.actionEllipse.setObjectName("actionEllipse")
        self.actionChangeColor = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/tool_bar/tool_collor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionChangeColor.setIcon(icon2)
        self.actionChangeColor.setObjectName("actionChangeColor")
        self.actionLine = QtWidgets.QAction(MainWindow)
        self.actionLine.setCheckable(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/tool_bar/tool_line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLine.setIcon(icon3)
        self.actionLine.setObjectName("actionLine")
        self.actionPoint = QtWidgets.QAction(MainWindow)
        self.actionPoint.setCheckable(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/tool_bar/tool_point.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPoint.setIcon(icon4)
        self.actionPoint.setObjectName("actionPoint")
        self.actionFill = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/tool_bar/tool_fill.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFill.setIcon(icon5)
        self.actionFill.setObjectName("actionFill")
        self.actionSelect = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/tool_bar/tool_select.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSelect.setIcon(icon6)
        self.actionSelect.setObjectName("actionSelect")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/tool_bar/tool_copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon7)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/tool_bar/tool_paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon8)
        self.actionPaste.setObjectName("actionPaste")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/tool_bar/tool_undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon9)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/tool_bar/tool_redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon10)
        self.actionRedo.setObjectName("actionRedo")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/tool_bar/tool_delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon11)
        self.actionDelete.setObjectName("actionDelete")
        self.actionCut = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/tool_bar/tool_cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon12)
        self.actionCut.setObjectName("actionCut")
        self.actionChangeSize = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/tool_bar/tool_change_size.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionChangeSize.setIcon(icon13)
        self.actionChangeSize.setObjectName("actionChangeSize")
        self.actionFileOpen = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/tool_bar/tool_open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFileOpen.setIcon(icon14)
        self.actionFileOpen.setObjectName("actionFileOpen")
        self.actionFileSave = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/tool_bar/tool_save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFileSave.setIcon(icon15)
        self.actionFileSave.setObjectName("actionFileSave")
        self.actionFileSaveAs = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/tool_bar/tool_save_as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFileSaveAs.setIcon(icon16)
        self.actionFileSaveAs.setObjectName("actionFileSaveAs")
        self.toolBar.addAction(self.actionFileOpen)
        self.toolBar.addAction(self.actionFileSave)
        self.toolBar.addAction(self.actionFileSaveAs)
        self.toolBar.addAction(self.actionChangeSize)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSelect)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRectangle)
        self.toolBar.addAction(self.actionEllipse)
        self.toolBar.addAction(self.actionLine)
        self.toolBar.addAction(self.actionPoint)
        self.toolBar.addAction(self.actionFill)
        self.toolBar.addAction(self.actionDelete)
        self.toolBar.addAction(self.actionChangeColor)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionRectangle.setText(_translate("MainWindow", "Rectangle"))
        self.actionRectangle.setToolTip(_translate("MainWindow", "Рисует прямоугольник"))
        self.actionEllipse.setText(_translate("MainWindow", "Ellipse"))
        self.actionEllipse.setToolTip(_translate("MainWindow", "Рисует эллипс"))
        self.actionChangeColor.setText(_translate("MainWindow", "ChangeColor"))
        self.actionChangeColor.setToolTip(_translate("MainWindow", "Нажмите сюда для выбора цвета"))
        self.actionLine.setText(_translate("MainWindow", "Line"))
        self.actionLine.setToolTip(_translate("MainWindow", "Рисует линию"))
        self.actionPoint.setText(_translate("MainWindow", "Point"))
        self.actionPoint.setToolTip(_translate("MainWindow", "Карандаш"))
        self.actionFill.setText(_translate("MainWindow", "Fill"))
        self.actionFill.setToolTip(_translate("MainWindow", "Заливка"))
        self.actionSelect.setText(_translate("MainWindow", "Select"))
        self.actionSelect.setToolTip(_translate("MainWindow", "Выделение"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setToolTip(_translate("MainWindow", "Копирует выделенный участок в буфер обмена"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setToolTip(_translate("MainWindow", "Вставляет изображение из буфера обмена"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setToolTip(_translate("MainWindow", "Отменяет дествие"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setToolTip(_translate("MainWindow", "Отменяет отмену дествия"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionDelete.setToolTip(_translate("MainWindow", "Стирает нарисованные пиксели"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setToolTip(_translate("MainWindow", "Вырезает выбранный участок"))
        self.actionChangeSize.setText(_translate("MainWindow", "ChangeSize"))
        self.actionChangeSize.setToolTip(_translate("MainWindow", "Изменяет размер изображения"))
        self.actionFileOpen.setText(_translate("MainWindow", "FileOpen"))
        self.actionFileOpen.setToolTip(_translate("MainWindow", "Открывает изображение для редактирования"))
        self.actionFileSave.setText(_translate("MainWindow", "FileSave"))
        self.actionFileSave.setToolTip(_translate("MainWindow", "Сохраняет изображение"))
        self.actionFileSaveAs.setText(_translate("MainWindow", "FileSaveAs"))
        self.actionFileSaveAs.setToolTip(_translate("MainWindow", "Сохраняет изображение в указанную папку"))
from .Graphics.Icons.icons_rc import *
