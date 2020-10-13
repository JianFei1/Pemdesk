import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Window_go(QWidget):

    #menentukan ukuran window, + title dan menampilkan 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("Pemdesk") 
        self.setGeometry(300, 100, 400, 300)
        self.createForm()
        self.show()
    
    def createForm(self):
        layout = QFormLayout()

        #berisi tulisan "input biodata" diletakkan di kolom pertama
        self.label_2 = QLabel("Input Biodata", self)
        self.label_2.setStyleSheet("font-size : 30px; background-color : #7cb8fd; color : red; font-weight: bold;")
        layout.addRow(self.label_2)

        #ini line edit ini berisi kotak kosong 
        layout.addRow(QLabel("Name:"), QLineEdit())
        layout.addRow(QLabel("Address:"), QLineEdit())
        layout.addRow(QLabel(""), QLineEdit())

        #ini check box, untuk membuat checkbox ini menggunakan "QCheckBox"
        #lalu setChecked ini untuk membuat awalan box apakah tercentang atau tidak
        #fung addrow ini untuk mengatur checkbox ini sesuai pada baris, jadi tidak perlu repot memindahkan secara manual
        checkBox1 = QCheckBox("Makan")
        checkBox1.setChecked(False)
        layout.addRow(QLabel("Hobby"), checkBox1)

        checkBox1 = QCheckBox("Tidur")
        checkBox1.setChecked(False)
        layout.addRow(QLabel(""), checkBox1)

        checkBox1 = QCheckBox("Main")
        checkBox1.setChecked(False)
        layout.addRow(QLabel(""), checkBox1)
        

        #ini radio btn, untuk membuat radiobutton ini menggunakan "QRadioButton"
        #lalu setChecked ini untuk membuat awalan radiobutton apakah tercentang atau tidak
        #fung addrow ini untuk mengatur radiobutton ini sesuai pada baris, jadi tidak perlu repot memindahkan secara manual
        radiobutton1 = QRadioButton("Pelajar")
        radiobutton1.setChecked(False)
        layout.addRow(QLabel("Status"), radiobutton1)

        radiobutton2 = QRadioButton("Pegawai")
        radiobutton2.setChecked(False)
        layout.addRow(QLabel(""), radiobutton2)

        radiobutton3 = QRadioButton("Wiraswasta")
        radiobutton3.setChecked(False)
        layout.addRow(QLabel(""), radiobutton3)

        #set layoutnya kegunaannya untuk menerapkan layout yang kita gunakan
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window_go()
    sys.exit(app.exec_())
