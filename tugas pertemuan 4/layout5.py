import sys
from PyQt5.QtWidgets import *

def window():
   app = QApplication(sys.argv)
   win = QWidget()
   
   #baris1
   l1 = QLabel("Name")
   nm = QLineEdit()
   
   #baris2
   l2 = QLabel("Address")
   add1 = QLineEdit()

   fbox = QFormLayout()
   fbox.addRow(l1,nm)
   fbox.addRow(l2,add1)

   #span, mengisi 1 baris full
   btn1 = QPushButton("tutup")
   fbox.addRow(btn1)

   #layout baru, vertical
   l3 = QLabel("Hobby")
   lay1 = QVBoxLayout()
   chk1 = QCheckBox("Makan")
   chk2 = QCheckBox("Tidur")
   chk3 = QCheckBox("Main")
   lay1.addWidget(chk1)   
   lay1.addWidget(chk2)   
   lay1.addWidget(chk3)
   #fbox.addRow(l3, lay1)   

   win.setLayout(fbox)
   
   win.setWindowTitle("PyQt")
   win.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   window()
