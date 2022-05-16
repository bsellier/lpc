import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QLineEdit
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import controller



#QMainWindow
class LoginDisplay(QWidget):

    def __init__(self):
        super().__init__()
        
        #self.setGeometry(300, 300, 350, 250)
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
        login = self.loginInput.text()
        password = self.passwordInput.text()
        controller.verifConnexion(login, password)

        
class EntreeDisplay(QMainWindow):

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



        


def changeDisplay(display):
    if display == 'entree':
        print("entree")


def main():
    app = QApplication(sys.argv)
    ex = LoginDisplay()
    sys.exit(app.exec())
    
    


if __name__ == '__main__':
    main()