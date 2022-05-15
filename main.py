import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QLineEdit
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

#QMainWindow
class Example(QWidget):

    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 350, 250)

        lbl1 = QLabel('Login', self)

        line = QLineEdit(self)

        layoutGrid = QGridLayout()
        self.setLayout(layoutGrid)


        line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layoutGrid.setColumnStretch(0, 1)
        layoutGrid.setColumnStretch(3, 1)
        layoutGrid.setRowStretch(0, 1)
        layoutGrid.setRowStretch(3, 1)

        layoutGrid.addWidget(line, 2, 2 , 1, 1)
        layoutGrid.addWidget(lbl1, 1, 2, 1, 1)



        self.showMaximized()

        



def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()