from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QLineEdit, QMainWindow
from PyQt5 import uic
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
##pip install PyQtWebEngine
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import * 
import controller
import sys
import json
from os import path


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

    def __init__(self, root=None):
        super().__init__()

        self.root = root

        uic.loadUi('mainwindow.ui', self)
        self.findChild(QPushButton, "cmdControler").hide()
        self.findChild(QPushButton, "cmdControler").clicked.connect(self.commencerControle)
    
        self.findChild(QMenu, "menuMenu").triggered.connect(self.handleMenu)
        
        self.findChild(QPushButton, "cmdValiderVerre").clicked.connect(self.commencerControle)
        self.findChild(QPushButton, "cmdAjoutUser").clicked.connect(self.ajouterUtilisateur)
        self.findChild(QPushButton, "cmdAjoutCommande").clicked.connect(self.importerCommande)
        self.findChild(QTableWidget, "tableWidget_3").verticalHeader().setVisible(False)
        self.findChild(QTableWidget, "tableWidget_3").cellClicked.connect(self.afficherInfoCommandes)
        self.findChild(QTableWidget, "tableWidget_2").verticalHeader().setVisible(False)
        self.findChild(QComboBox, "txtNumCommande_2").currentIndexChanged.connect(self.updateReference)
        self.findChild(QComboBox, "typeVerre").currentIndexChanged.connect(self.updatePdf)

        #pdf view
        self.webView = QWebEngineView()
        self.webView.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.webView.settings().setAttribute(QWebEngineSettings.PdfViewerEnabled, True)
        self.findChild(QHBoxLayout , "pdfView").addWidget(self.webView)

        self.showMaximized()

    def handleMenu(self, action):
        actionName = action.text()
        print(actionName)

        if actionName == "Deconnexion":
            controller.currentUser = ""
            controller.isAdmin = False
            self.root.changeDisplay(0)
            self.checkPermissions()

            return
        
        if actionName == "Quitter":
            self.root.close()
            return
        
        if actionName == "Changer mot de passe":
            print("C")
    
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

    def importerCommande(self):
        fname = QFileDialog.getOpenFileName(self, 'Sélectionner une commande')

        if fname[0] == None or fname[0] == "":
            return
        print(fname)
        commandes = controller.importerCommande(fname[0])
        if commandes == None:
            return

        cmdTable = self.findChild(QTableWidget, "tableWidget_3")
        comboBoxCom = self.findChild(QComboBox, "txtNumCommande_2")
        for idcommande in commandes.keys():
            verres = commandes[idcommande]
            if not isinstance(commandes[idcommande], list):
                print("erreur", type(verres))

            rowPos = cmdTable.rowCount()
            cmdTable.insertRow(rowPos)
            cmdTable.setItem(rowPos, 0, QTableWidgetItem(idcommande))
            cmdTable.setItem(rowPos, 1, QTableWidgetItem("Oui" if verres[0]["special"] == 0 else "Non"))
            cmdTable.setItem(rowPos, 2, QTableWidgetItem("Non"))
            cmdTable.takeVerticalHeaderItem(rowPos)
        
            #ajout dans controle verre
            comboBoxCom.addItem(idcommande)


    def updateReference(self, index):
        print(index)
        comboBoxRef = self.findChild(QComboBox, "typeVerre")
        idcommande = self.findChild(QComboBox, "txtNumCommande_2").itemText(index)

        verres = controller.getInfosCommande(idcommande)
        if verres == None:
            return

        comboBoxRef.clear()
        for verre in verres:
            quant = verre["quantite"]
            print(type(quant))
            while quant >= 1 :
                #ajouter le dossier client à la reference si verre spécial
                ref = verre["type"] + "_" + (str(quant) if quant >= 10 else "0" + str(quant)) + (("_" + verre["client"]) if verre["special"] == 1 else "")
                comboBoxRef.addItem(ref)
                quant -= 1

    def updatePdf(self, index):
        code = self.findChild(QComboBox, "typeVerre").itemText(index)

        #si le verre est spécial on extrait le num de dossier
        numdoss = code[code.find('_') + 1:]
        numdoss = numdoss[numdoss.find('_') + 1:]
        print(numdoss)
        if numdoss != - 1:
            self.findChild(QLineEdit, "txtNumDossier").setText(numdoss)

        #on extrait le code article
        code = code[:code.find('_')]
        infos = controller.getInfosTypeVerre(code)
        if infos == None or infos[2] == None:
            self.webView.setHtml("<h2 style=\"text-align: center; margin-top: 40%\">Il n'y a pas de plan pour ce verre dans la base de données.</h2>")
            return

        pdfbin = infos[2]
        fname = '../plans/' + infos[0] + '.pdf'
        file = open(fname, 'wb')
        file.write(pdfbin)
        file.close()
        
        wd = path.dirname(sys.argv[0])
        self.webView.setUrl(QUrl(f"file:///{wd}/" + fname))

        


    def afficherInfoCommandes(self, x, y):
        item = self.findChild(QTableWidget, "tableWidget_3").item(x, 0)
        if item == None:
            return
        
        detailTable = self.findChild(QTableWidget, "tableWidget_2")
        detailTable.clear()
        detailTable.setRowCount(0)

        print(item.text())
        infos = controller.getInfosCommande(item.text())
        
        if infos == None:
            return
        
        
        infos = str(infos)[2:-1]
        infos = json.loads(infos)
        
        for verre in infos: #infos est une liste
            rowPos = detailTable.rowCount()
            detailTable.insertRow(rowPos)
            detailTable.setItem(rowPos, 0, QTableWidgetItem(verre["type"]))
            detailTable.setItem(rowPos, 1, QTableWidgetItem(str(verre["quantite"])))

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
        self.stackedWidget.addWidget(InterfaceDisplay(self)) #index 1

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