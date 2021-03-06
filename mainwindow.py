# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("QMainWindow {background-color :qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:1, stop:0.00473934 rgba(132, 207, 0, 148), stop:0.601896 rgba(255, 255, 255, 255))}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabWidget{background:  qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:1, stop:0.00473934 rgba(132, 207, 0, 148), stop:0.601896 rgba(255, 255, 255, 255))}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setObjectName("tabWidget")
        self.tbControle = QtWidgets.QWidget()
        self.tbControle.setObjectName("tbControle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tbControle)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(30, -1, -1, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.tbControle)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.txtNumCommande_2 = QtWidgets.QComboBox(self.tbControle)
        self.txtNumCommande_2.setObjectName("txtNumCommande_2")
        self.verticalLayout_8.addWidget(self.txtNumCommande_2)
        self.label = QtWidgets.QLabel(self.tbControle)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.typeVerre = QtWidgets.QComboBox(self.tbControle)
        self.typeVerre.setObjectName("typeVerre")
        self.verticalLayout_8.addWidget(self.typeVerre)
        self.label_3 = QtWidgets.QLabel(self.tbControle)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        self.txtNumDossier = QtWidgets.QLineEdit(self.tbControle)
        self.txtNumDossier.setEnabled(False)
        self.txtNumDossier.setObjectName("txtNumDossier")
        self.verticalLayout_8.addWidget(self.txtNumDossier)
        self.label_6 = QtWidgets.QLabel(self.tbControle)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.etatSurface = QtWidgets.QComboBox(self.tbControle)
        self.etatSurface.setObjectName("etatSurface")
        self.etatSurface.addItem("")
        self.etatSurface.addItem("")
        self.etatSurface.addItem("")
        self.etatSurface.addItem("")
        self.etatSurface.addItem("")
        self.etatSurface.addItem("")
        self.etatSurface.addItem("")
        self.verticalLayout_8.addWidget(self.etatSurface)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.cmdValiderVerre = QtWidgets.QPushButton(self.tbControle)
        self.cmdValiderVerre.setCheckable(False)
        self.cmdValiderVerre.setObjectName("cmdValiderVerre")
        self.horizontalLayout_18.addWidget(self.cmdValiderVerre)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_18)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 1)
        self.verticalLayout_8.setStretch(2, 1)
        self.verticalLayout_8.setStretch(3, 1)
        self.verticalLayout_8.setStretch(4, 1)
        self.verticalLayout_8.setStretch(5, 1)
        self.verticalLayout_8.setStretch(6, 1)
        self.verticalLayout_8.setStretch(7, 1)
        self.verticalLayout_8.setStretch(9, 1)
        self.verticalLayout_8.setStretch(10, 30)
        self.horizontalLayout_17.addLayout(self.verticalLayout_8)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem3)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.SpeStand_2 = QtWidgets.QGroupBox(self.tbControle)
        self.SpeStand_2.setTitle("")
        self.SpeStand_2.setFlat(True)
        self.SpeStand_2.setObjectName("SpeStand_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.SpeStand_2)
        self.radioButton_3.setGeometry(QtCore.QRect(0, 20, 111, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.SpeStand_2)
        self.radioButton_4.setGeometry(QtCore.QRect(0, 0, 111, 20))
        self.radioButton_4.setChecked(True)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.SpeStand_2)
        self.radioButton_5.setGeometry(QtCore.QRect(0, 40, 111, 20))
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_9.addWidget(self.SpeStand_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem4)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.cmdControler = QtWidgets.QPushButton(self.tbControle)
        self.cmdControler.setCheckable(False)
        self.cmdControler.setObjectName("cmdControler")
        self.horizontalLayout_16.addWidget(self.cmdControler)
        self.verticalLayout_9.addLayout(self.horizontalLayout_16)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem5)
        self.verticalLayout_9.setStretch(0, 3)
        self.verticalLayout_9.setStretch(1, 3)
        self.verticalLayout_9.setStretch(2, 2)
        self.verticalLayout_9.setStretch(3, 10)
        self.horizontalLayout_17.addLayout(self.verticalLayout_9)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem6)
        self.line_4 = QtWidgets.QFrame(self.tbControle)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_17.addWidget(self.line_4)
        self.pdfView = QtWidgets.QHBoxLayout()
        self.pdfView.setObjectName("pdfView")
        self.horizontalLayout_17.addLayout(self.pdfView)
        self.horizontalLayout_17.setStretch(0, 4)
        self.horizontalLayout_17.setStretch(1, 1)
        self.horizontalLayout_17.setStretch(2, 3)
        self.horizontalLayout_17.setStretch(5, 6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_17)
        self.tabWidget.addTab(self.tbControle, "")
        self.tbPreparation = QtWidgets.QWidget()
        self.tbPreparation.setObjectName("tbPreparation")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tbPreparation)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tbPreparation)
        font = QtGui.QFont()
        font.setBold(False)
        self.tableWidget_3.setFont(font)
        self.tableWidget_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget_3.setLineWidth(2)
        self.tableWidget_3.setMidLineWidth(2)
        self.tableWidget_3.setDragDropOverwriteMode(False)
        self.tableWidget_3.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_3.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_3.setShowGrid(True)
        self.tableWidget_3.setWordWrap(True)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(3)
        self.tableWidget_3.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        item.setFont(font)
        self.tableWidget_3.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 2, item)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_3.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableWidget_3)
        self.label_10 = QtWidgets.QLabel(self.tbPreparation)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.tbPreparation)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.line_3 = QtWidgets.QFrame(self.tbPreparation)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tbPreparation)
        self.tableWidget_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_5.addWidget(self.tableWidget_2)
        self.label_9 = QtWidgets.QLabel(self.tbPreparation)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tbPreparation)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem12)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(4, 2)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tbPreparation, "")
        self.tbAdmin = QtWidgets.QWidget()
        self.tbAdmin.setEnabled(True)
        self.tbAdmin.setAutoFillBackground(False)
        self.tbAdmin.setStyleSheet("QtbADmin{background:  rgba(255, 255, 255, 0)}")
        self.tbAdmin.setObjectName("tbAdmin")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.tbAdmin)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem13)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.tbAdmin)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(25)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.label_13 = QtWidgets.QLabel(self.tbAdmin)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem14)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.tbAdmin)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem15)
        self.label_12 = QtWidgets.QLabel(self.tbAdmin)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_7.addWidget(self.label_12)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem16)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem17)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.dateEdit = QtWidgets.QDateEdit(self.tbAdmin)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_6.addWidget(self.dateEdit)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem18)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.tbAdmin)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout_6.addWidget(self.dateEdit_2)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem19)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem20)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalGroupBox = QtWidgets.QGroupBox(self.tbAdmin)
        self.verticalGroupBox.setFlat(True)
        self.verticalGroupBox.setCheckable(False)
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout_10.setContentsMargins(1, 9, -1, -1)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.cmdExportDonnees = QtWidgets.QPushButton(self.verticalGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.cmdExportDonnees.sizePolicy().hasHeightForWidth())
        self.cmdExportDonnees.setSizePolicy(sizePolicy)
        self.cmdExportDonnees.setMinimumSize(QtCore.QSize(0, 1))
        self.cmdExportDonnees.setObjectName("cmdExportDonnees")
        self.verticalLayout_10.addWidget(self.cmdExportDonnees)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem21)
        self.verticalLayout_10.setStretch(0, 5)
        self.horizontalLayout_9.addWidget(self.verticalGroupBox)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem22)
        self.verticalGroupBox_4 = QtWidgets.QGroupBox(self.tbAdmin)
        self.verticalGroupBox_4.setFlat(True)
        self.verticalGroupBox_4.setObjectName("verticalGroupBox_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalGroupBox_4)
        self.verticalLayout_7.setContentsMargins(1, -1, -1, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.cmdAjoutCommande = QtWidgets.QPushButton(self.verticalGroupBox_4)
        self.cmdAjoutCommande.setObjectName("cmdAjoutCommande")
        self.verticalLayout_7.addWidget(self.cmdAjoutCommande)
        self.cmdAjoutExpedition = QtWidgets.QPushButton(self.verticalGroupBox_4)
        self.cmdAjoutExpedition.setObjectName("cmdAjoutExpedition")
        self.verticalLayout_7.addWidget(self.cmdAjoutExpedition)
        self.cmdAjoutTypeVerre = QtWidgets.QPushButton(self.verticalGroupBox_4)
        self.cmdAjoutTypeVerre.setStyleSheet("")
        self.cmdAjoutTypeVerre.setObjectName("cmdAjoutTypeVerre")
        self.verticalLayout_7.addWidget(self.cmdAjoutTypeVerre)
        self.horizontalLayout_9.addWidget(self.verticalGroupBox_4)
        self.horizontalLayout_9.setStretch(1, 4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem23)
        self.verticalLayout_3.setStretch(5, 3)
        self.horizontalLayout_13.addLayout(self.verticalLayout_3)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem24)
        self.line = QtWidgets.QFrame(self.tbAdmin)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_13.addWidget(self.line)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.tbAdmin)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.lstDroit = QtWidgets.QComboBox(self.tbAdmin)
        self.lstDroit.setObjectName("lstDroit")
        self.lstDroit.addItem("")
        self.lstDroit.addItem("")
        self.verticalLayout_4.addWidget(self.lstDroit)
        self.label_5 = QtWidgets.QLabel(self.tbAdmin)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.txtIdentifiantAjout = QtWidgets.QLineEdit(self.tbAdmin)
        self.txtIdentifiantAjout.setObjectName("txtIdentifiantAjout")
        self.verticalLayout_4.addWidget(self.txtIdentifiantAjout)
        self.label_7 = QtWidgets.QLabel(self.tbAdmin)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.txtImdpAjout = QtWidgets.QLineEdit(self.tbAdmin)
        self.txtImdpAjout.setEnabled(False)
        self.txtImdpAjout.setObjectName("txtImdpAjout")
        self.verticalLayout_4.addWidget(self.txtImdpAjout)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem25)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.cmdAjoutUser = QtWidgets.QPushButton(self.tbAdmin)
        self.cmdAjoutUser.setObjectName("cmdAjoutUser")
        self.horizontalLayout_10.addWidget(self.cmdAjoutUser)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem26)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem27)
        self.line_2 = QtWidgets.QFrame(self.tbAdmin)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.label_8 = QtWidgets.QLabel(self.tbAdmin)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.lstUtilisateur = QtWidgets.QComboBox(self.tbAdmin)
        self.lstUtilisateur.setObjectName("lstUtilisateur")
        self.verticalLayout_4.addWidget(self.lstUtilisateur)
        spacerItem28 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem28)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.cmdSupprimerUser = QtWidgets.QPushButton(self.tbAdmin)
        self.cmdSupprimerUser.setObjectName("cmdSupprimerUser")
        self.horizontalLayout_11.addWidget(self.cmdSupprimerUser)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem29)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        spacerItem30 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem30)
        spacerItem31 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem31)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 2)
        self.verticalLayout_4.setStretch(2, 1)
        self.verticalLayout_4.setStretch(3, 2)
        self.verticalLayout_4.setStretch(4, 1)
        self.verticalLayout_4.setStretch(5, 2)
        self.verticalLayout_4.setStretch(6, 1)
        self.verticalLayout_4.setStretch(7, 3)
        self.verticalLayout_4.setStretch(8, 1)
        self.verticalLayout_4.setStretch(9, 2)
        self.verticalLayout_4.setStretch(10, 1)
        self.verticalLayout_4.setStretch(11, 2)
        self.verticalLayout_4.setStretch(12, 1)
        self.verticalLayout_4.setStretch(15, 4)
        self.horizontalLayout_13.addLayout(self.verticalLayout_4)
        self.horizontalLayout_13.setStretch(1, 8)
        self.horizontalLayout_13.setStretch(2, 3)
        self.horizontalLayout_13.setStretch(4, 4)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_13)
        self.tabWidget.addTab(self.tbAdmin, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuAide = QtWidgets.QMenu(self.menubar)
        self.menuAide.setObjectName("menuAide")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionChanger_mot_de_passe = QtWidgets.QAction(MainWindow)
        self.actionChanger_mot_de_passe.setObjectName("actionChanger_mot_de_passe")
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionDeconnexion = QtWidgets.QAction(MainWindow)
        self.actionDeconnexion.setObjectName("actionDeconnexion")
        self.actionA_propos = QtWidgets.QAction(MainWindow)
        self.actionA_propos.setObjectName("actionA_propos")
        self.menuMenu.addAction(self.actionChanger_mot_de_passe)
        self.menuMenu.addAction(self.actionDeconnexion)
        self.menuMenu.addAction(self.actionQuitter)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LPC"))
        self.label_2.setText(_translate("MainWindow", "Num??ro de commande"))
        self.label.setText(_translate("MainWindow", "R??f??rence"))
        self.label_3.setText(_translate("MainWindow", "Num??ro de dossier"))
        self.label_6.setText(_translate("MainWindow", "Etat de surface"))
        self.etatSurface.setItemText(0, _translate("MainWindow", "Parfait"))
        self.etatSurface.setItemText(1, _translate("MainWindow", "Rayures ratrapables"))
        self.etatSurface.setItemText(2, _translate("MainWindow", "Rayures non rattrapables"))
        self.etatSurface.setItemText(3, _translate("MainWindow", "Aiguille"))
        self.etatSurface.setItemText(4, _translate("MainWindow", "Impact"))
        self.etatSurface.setItemText(5, _translate("MainWindow", "Inclusion"))
        self.etatSurface.setItemText(6, _translate("MainWindow", "Gondolement"))
        self.cmdValiderVerre.setText(_translate("MainWindow", "Valider"))
        self.radioButton_3.setText(_translate("MainWindow", "Contr??le partiel"))
        self.radioButton_4.setText(_translate("MainWindow", "Contr??le total"))
        self.radioButton_5.setText(_translate("MainWindow", "Pas de contr??le"))
        self.cmdControler.setText(_translate("MainWindow", "Commencer le contr??le"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbControle), _translate("MainWindow", "Contr??le de verres"))
        self.tableWidget_3.setSortingEnabled(True)
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Commande"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Sp??cial?"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Termin???"))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        item = self.tableWidget_3.item(1, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_3.item(1, 1)
        item.setText(_translate("MainWindow", "Non"))
        item = self.tableWidget_3.item(1, 2)
        item.setText(_translate("MainWindow", "Non"))
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        self.label_10.setText(_translate("MainWindow", "Resum?? journalier"))
        self.pushButton.setText(_translate("MainWindow", "Preparer"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Verre"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Quantit??"))
        self.label_9.setText(_translate("MainWindow", "D??tail commande"))
        self.pushButton_2.setText(_translate("MainWindow", "Termin??"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbPreparation), _translate("MainWindow", "Pr??paration de commandes"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Variable"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Valeur"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "Nombre de verres trait??s"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "0"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "Nombre de Non Conformit??"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", "0"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "Nombre de commandes pr??par??es"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("MainWindow", "0"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "Nombre de commandes restant"))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("MainWindow", "0"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_13.setText(_translate("MainWindow", "Resum?? journalier"))
        self.label_11.setText(_translate("MainWindow", "Date de d??but"))
        self.label_12.setText(_translate("MainWindow", "Date de fin"))
        self.cmdExportDonnees.setText(_translate("MainWindow", "Exporter les op??rations "))
        self.cmdAjoutCommande.setText(_translate("MainWindow", "Ajouter les commandes"))
        self.cmdAjoutExpedition.setText(_translate("MainWindow", "Ajouter des exp??ditions"))
        self.cmdAjoutTypeVerre.setText(_translate("MainWindow", "Ajout type de verre"))
        self.label_4.setText(_translate("MainWindow", "Droit"))
        self.lstDroit.setItemText(0, _translate("MainWindow", "Op??rateur"))
        self.lstDroit.setItemText(1, _translate("MainWindow", "Administrateur"))
        self.label_5.setText(_translate("MainWindow", "Identifiant"))
        self.label_7.setText(_translate("MainWindow", "Mot de passe"))
        self.cmdAjoutUser.setText(_translate("MainWindow", "Ajouter"))
        self.label_8.setText(_translate("MainWindow", "Choisir Utilisateur"))
        self.cmdSupprimerUser.setText(_translate("MainWindow", "Supprimer l\'utilisateur"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbAdmin), _translate("MainWindow", "Admin"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuAide.setTitle(_translate("MainWindow", "Aide"))
        self.actionChanger_mot_de_passe.setText(_translate("MainWindow", "Changer mot de passe"))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))
        self.actionDeconnexion.setText(_translate("MainWindow", "Deconnexion"))
        self.actionA_propos.setText(_translate("MainWindow", "A propos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
