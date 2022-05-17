from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QLineEdit
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


    def connexion(self):
        print("test")
        login = self.loginInput.text()
        password = self.passwordInput.text()
        if controller.verifConnexion(login, password):
            if self.root == None:
                print("pas de root")
            else:
                self.root.changeDisplay(1)
            

#ecran du poste d'entrée     
class EntreeDisplay(QWidget):

    def __init__(self):
        super().__init__()

        refInput = QLineEdit(self)
        refInput.setPlaceholderText("Référence")
        refInput.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        layoutGrid = QGridLayout()

        layoutGrid.setRowStretch(0, 1)
        layoutGrid.addWidget(refInput, 1, 1, 1, 1)
        layoutGrid.setRowStretch(2, 1)
        layoutGrid.setColumnStretch(2, 1)

        self.setLayout(layoutGrid)

        self.showMaximized()
    

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()



class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.layout = QVBoxLayout()

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(LoginDisplay(self)) #index 0
        self.stackedWidget.addWidget(EntreeDisplay()) #index 1

        self.layout.addWidget(self.stackedWidget)
        self.setLayout(self.layout)
        self.showMaximized()
    
    def changeDisplay(self, index):
        self.stackedWidget.setCurrentIndex(index)


def initGUI():
    app = QApplication(sys.argv)
    ex = MainApp()
    sys.exit(app.exec())