import sys
from PyQt5.QtWidgets import *

def window():
   app = QApplication(sys.argv)
   win = QWidget()
	
   parent1 = QHBoxLayout()

   #layout baru : hbox, horizontal
   ln1 = QLineEdit("trunojoyo")
   ln2 = QLineEdit("Madura")
   hbox = QHBoxLayout()
   hbox.addWidget(ln1)
   hbox.addWidget(ln2)

   #ini di vbox
   b1 = QPushButton("Button1")
   b2 = QPushButton("Button2")
   #tulisan
   txt1 = QLabel("belajar pyqt")
   vbox = QVBoxLayout()
   vbox.addWidget(b1)
   vbox.addWidget(txt1)
   vbox.addWidget(b2)   
   
   #set layout
   parent1.addLayout(vbox)
   parent1.addLayout(hbox)
   
   win.setLayout(parent1)

   win.setWindowTitle("PyQt")
   win.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   window()
