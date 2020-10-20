import sys
from PyQt5.QtWidgets import *

def window():
   app = QApplication(sys.argv)
   win = QWidget()
	
   b1 = QPushButton("Button1")
   b2 = QPushButton("Button2")

   #layout baru : hbox, horizontal
   ln1 = QLineEdit("trunojoyo")
   ln2 = QLineEdit("Madura")
   hbox = QHBoxLayout()
   hbox.addWidget(ln1)
   hbox.addWidget(ln2)

   #tulisan
   txt1 = QLabel("belajar pyqt")

   vbox = QVBoxLayout()
   vbox.addWidget(b1)
   vbox.addLayout(hbox)
   vbox.addWidget(txt1)
   vbox.addWidget(b2)   
   
   win.setLayout(vbox)

   win.setWindowTitle("PyQt")
   win.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   window()
