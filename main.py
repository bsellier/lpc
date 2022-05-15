import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QLineEdit
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

#QMainWindow
class LoginDisplay(QWidget):

    def __init__(self):
        super().__init__()
        
        #self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("LPC")

        loginInput = QLineEdit(self)
        loginInput.setPlaceholderText("Identifiant")
        loginInput.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        passwordInput = QLineEdit(self)
        passwordInput.setPlaceholderText("Mot de passe")
        passwordInput.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        layoutGrid = QGridLayout()
        self.setLayout(layoutGrid)


        layoutGrid.setColumnStretch(0, 1)
        layoutGrid.setColumnStretch(3, 1)
        layoutGrid.setRowStretch(0, 1)
        layoutGrid.setRowStretch(4, 1)

        layoutGrid.addWidget(loginInput, 2, 2 , 1, 1)
        layoutGrid.addWidget(passwordInput, 3, 2, 1, 1)



        self.showMaximized()

        
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



def main():
    app = QApplication(sys.argv)
    ex = EntreeDisplay()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()