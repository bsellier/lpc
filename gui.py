from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QLineEdit, QMainWindow
from PyQt5 import uic
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import controller
import sys


#Ecran de login
class LoginDisplay(QWidget):

    def __init__(self, root=None):
        super().__init__()
        
        self.root = root

        self.setWindowTitle("LPC")

        self.loginInput = QLineEdit(self)
        self.loginInput.setPlaceholderText("Identifiant")
        self.loginInput.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.passwordInput = QLineEdit(self)
        self.passwordInput.setPlaceholderText("Mot de passe")
        self.passwordInput.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.connexionButton = QPushButton(self)
        self.connexionButton.setText("Se connecter")

        self.connexionButton.clicked.connect(self.connexion)


        layoutGrid = QGridLayout()
        self.setLayout(layoutGrid)


        layoutGrid.setColumnStretch(0, 1)
        layoutGrid.setColumnStretch(2, 1)
        layoutGrid.setRowStretch(0, 1)
        layoutGrid.setRowStretch(5, 1)

        layoutGrid.addWidget(self.loginInput, 2, 1 , 1, 1)
        layoutGrid.addWidget(self.passwordInput, 3, 1, 1, 1)
        layoutGrid.addWidget(self.connexionButton, 4, 1, 1, 1)

        self.showMaximized()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return:
            self.connexion()

    def connexion(self):
        login = self.loginInput.text()
        password = self.passwordInput.text()
        if controller.verifConnexion(login, password):
            if self.root == None:
                print("pas de root")
            else:
                self.root.changeDisplay(1)
            

class InterfaceDisplay(QMainWindow):

    def __init__(self):
        super().__init__()

        uic.loadUi('mainwindow.ui', self)
        self.findChild(QPushButton, "cmdControler").hide()
        self.findChild(QPushButton, "cmdControler").clicked.connect(self.commencerControle)
    
        #self.findChild(QMenuBar, "menubar").actions()[1].triggered.connect(self.deconnecter)
        
        self.findChild(QPushButton, "cmdAjoutUser").clicked.connect(self.ajouterUtilisateur)

        self.showMaximized()
    
    def ajouterUtilisateur(self):
        login = self.findChild(QLineEdit, "txtIdentifiantAjout").text()
        #!!! A CHANGER !!! -> génération aléatoire du mot de passe
        password = 123
        admin = self.findChild(QComboBox, "lstDroit").currentText()
        isAdmin = False
        if(admin == "Administrateur"):
            isAdmin = True
        print(admin, isAdmin)
        controller.ajouterUtilisateur(login, password, isAdmin)

    def checkPermissions(self):
        if controller.isAdmin == False:
            self.findChild(QTabWidget, "tabWidget").removeTab(2)

    
    
    def commencerControle(self):
        
        print("clic")

    def deconnecter(self):
        print("deco")
        self.close()


class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.layout = QVBoxLayout()

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(LoginDisplay(self)) #index 0
        self.stackedWidget.addWidget(InterfaceDisplay()) #index 1

        self.layout.addWidget(self.stackedWidget)
        self.setLayout(self.layout)
        self.showMaximized()
    
    def changeDisplay(self, index):
        self.stackedWidget.setCurrentIndex(index)
        print(controller.isAdmin)
        if controller.isAdmin == False:
            self.stackedWidget.widget(1).findChild(QTabWidget, "tabWidget").removeTab(2)


def initGUI():
    app = QApplication(sys.argv)
    ex = MainApp()
    sys.exit(app.exec())    