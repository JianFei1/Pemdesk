import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class HomePage(QWidget):
    def __init__(self, parent=None):
        super(HomePage, self).__init__(parent)
        self.box = QVBoxLayout()
        self.judul = QLabel("Tools Hitungan Sederhana")
        self.kata = QLabel("\" silahkan klik di tulisannya\"")
        self.box.addWidget(self.judul)
        self.box.addWidget(self.kata)
        self.btn1 = QPushButton("1. Luas   ")
        self.btn2 = QPushButton("2. Keliling")
        self.btn1.setFlat(True)
        self.btn2.setFlat(True)
        self.layout1= QGridLayout()
        self.layout1.addLayout(self.box, 0, 1)
        self.layout1.addWidget(self.btn1, 2, 0)
        self.layout1.addWidget(self.btn2, 3, 0)
        self.layout1.addWidget(QLabel(""),0,3)
        self.layout1.addWidget(QLabel(""),1,0)
        self.layout1.setRowStretch(4,1)
        self.setLayout(self.layout1)

        


class HalamanLuas(QWidget):
    def setupPage(self,Window_go):
        self.box = QVBoxLayout()
        self.judul = QLabel("Luas Bangun Datar")
        self.box.addWidget(self.judul)
        self.btn1 = QPushButton("1. Persegi               ")
        self.btn2 = QPushButton("2. Persegi Panjang")
        self.btn1.setFlat(True)
        self.btn2.setFlat(True)
        self.kembali = QPushButton("<< kembali")
        self.layout1= QGridLayout()
        self.layout1.addLayout(self.box, 0, 1)
        self.layout1.addWidget(self.btn1, 2, 0)
        self.layout1.addWidget(self.btn2, 3, 0)
        self.layout1.addWidget(QLabel(""),0,3)
        self.layout1.addWidget(QLabel(""),1,0)
        self.layout1.addWidget(self.kembali,5,0)
        self.layout1.setRowStretch(4,1)
        self.layout1.setRowStretch(6,0)

        self.setLayout(self.layout1)


class HalamanKeliling(QWidget):
    def setupPage(self,Window_go):
        self.box = QVBoxLayout()
        self.judul = QLabel("Keliling Bangun Datar")
        self.box.addWidget(self.judul)
        self.btn1 = QPushButton("1. Persegi               ")
        self.btn2 = QPushButton("2. Persegi Panjang")
        self.btn1.setFlat(True)
        self.btn2.setFlat(True)
        self.kembali = QPushButton("<< kembali")
        self.layout1= QGridLayout()
        self.layout1.addLayout(self.box, 0, 1)
        self.layout1.addWidget(self.btn1, 2, 0)
        self.layout1.addWidget(self.btn2, 3, 0)
        self.layout1.addWidget(QLabel(""),0,3)
        self.layout1.addWidget(QLabel(""),1,0)
        self.layout1.addWidget(self.kembali,5,0)
        self.layout1.setRowStretch(4,1)
        self.layout1.setRowStretch(6,0)

        self.setLayout(self.layout1)


class HalamanLuasPersegiPanjang(QWidget):
    def setupPage(self,Window_go):
        self.box = QVBoxLayout()
        self.judul = QLabel("Luas Persegi Panjang")
        self.judul.setAlignment(Qt.AlignCenter)
        self.box.addWidget(self.judul)

        # panjang
        self.hboxP = QHBoxLayout()
        self.pjg = QLabel("panjang :")
        self.pjgss = QLineEdit()
        self.hboxP.addWidget(self.pjg)
        self.hboxP.addWidget(self.pjgss)

        # lebar
        self.hboxL = QHBoxLayout()
        self.lbr = QLabel("lebar      :")
        self.lbrss = QLineEdit()
        self.hboxL.addWidget(self.lbr)
        self.hboxL.addWidget(self.lbrss)

        # btn hitung
        self.hboxBTN = QHBoxLayout()
        self.submit = QPushButton("Hitung !!")
        self.submit.clicked.connect(self.hitungan)
        self.hboxBTN.addWidget(self.submit)
        self.hboxBTN.addStretch(1)

        # hasil
        self.hboxHasil = QHBoxLayout()
        self.hasil = QLabel("Luas Persegi Panjang =")
        self.itung = QLabel()
        self.hboxHasil.addWidget(self.hasil)
        self.hboxHasil.addWidget(self.itung)

        # btn kembali
        self.hboxKembali = QHBoxLayout()
        self.kembali = QPushButton("<< kembali")
        self.hboxKembali.addWidget(self.kembali)
        self.hboxKembali.addStretch(1)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.box)
        self.vbox.addWidget(QLabel())
        self.vbox.addLayout(self.hboxP)
        self.vbox.addLayout(self.hboxL)
        self.vbox.addLayout(self.hboxBTN)
        self.vbox.addWidget(QLabel())
        self.vbox.addLayout(self.hboxHasil)
        self.vbox.addWidget(QLabel())
        self.vbox.addLayout(self.hboxKembali)
        self.vbox.addStretch(1)
        self.setLayout(self.vbox)

    def hitungan(self):
        try:
            panjang = float(self.pjgss.text())
            lebar = float(self.lbrss.text())
            luas = panjang*lebar
            self.itung.setText(str(luas))

        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Alert")
            msg.setText("sepertinya ada yang belum terisi")
            msg.exec_()

class HalamanKelilingPersegiPanjang(QWidget):
    def setupPage(self,Window_go):
        self.box = QVBoxLayout()
        self.judul = QLabel("Keliling Persegi Panjang")
        self.judul.setAlignment(Qt.AlignCenter)
        self.box.addWidget(self.judul)

        # panjang
        self.hboxP = QHBoxLayout()
        self.pjg = QLabel("panjang :")
        self.pjgss = QLineEdit()
        self.hboxP.addWidget(self.pjg)
        self.hboxP.addWidget(self.pjgss)

        # lebar
        self.hboxL = QHBoxLayout()
        self.lbr = QLabel("lebar      :")
        self.lbrss = QLineEdit()
        self.hboxL.addWidget(self.lbr)
        self.hboxL.addWidget(self.lbrss)

        # btn hitung
        self.hboxBTN = QHBoxLayout()
        self.submit = QPushButton("Hitung !!")
        self.submit.clicked.connect(self.hitungan)
        self.hboxBTN.addWidget(self.submit)
        self.hboxBTN.addStretch(1)

        # hasil
        self.hboxHasil = QHBoxLayout()
        self.hasil = QLabel("Keliling Persegi Panjang =")
        self.itung = QLabel()
        self.hboxHasil.addWidget(self.hasil)
        self.hboxHasil.addWidget(self.itung)

        # btn kembali
        self.hboxKembali = QHBoxLayout()
        self.kembali = QPushButton("<< kembali")
        self.hboxKembali.addWidget(self.kembali)
        self.hboxKembali.addStretch(1)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.box)
        self.vbox.addWidget(QLabel())
        self.vbox.addLayout(self.hboxP)
        self.vbox.addLayout(self.hboxL)
        self.vbox.addLayout(self.hboxBTN)
        self.vbox.addWidget(QLabel())
        self.vbox.addLayout(self.hboxHasil)
        self.vbox.addWidget(QLabel())
        self.vbox.addLayout(self.hboxKembali)
        self.vbox.addStretch(1)
        self.setLayout(self.vbox)

    def hitungan(self):
        try:
            panjang = float(self.pjgss.text())
            lebar = float(self.lbrss.text())
            keliling = (panjang+lebar)*2
            self.itung.setText(str(keliling))

        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Alert")
            msg.setText("sepertinya ada yang belum terisi")
            msg.exec_()

class HalamanKelilingPersegi(QWidget):
    def setupPage(self,Window_go):
        self.box = QVBoxLayout()
        self.judul = QLabel("Keliling Persegi")
        self.judul.setAlignment(Qt.AlignCenter)
        self.box.addWidget(self.judul)

        # panjang
        self.hboxP = QHBoxLayout()
        self.pjg = QLabel("Sisi :")
        self.pjgss = QLineEdit()
        self.hboxP.addWidget(self.pjg)
        self.hboxP.addWidget(self.pjgss)

        # btn hitung
        self.hboxBTN = QHBoxLayout()
        self.submit = QPushButton("Hitung !!")
        self.submit.clicked.connect(self.hitungan)
        self.hboxBTN.addWidget(self.submit)
        self.hboxBTN.addStretch(1)

        # hasil
        self.hboxHasil = QHBoxLayout()
        self.hasil = QLabel("Keliling persegi =")
        self.itung = QLabel()
        self.hboxHasil.addWidget(self.hasil)
        self.hboxHasil.addWidget(self.itung)

        # btn kembali
        self.hboxKembali = QHBoxLayout()
        self.kembali = QPushButton("<< kembali")
        self.hboxKembali.addWidget(self.kembali)
        self.hboxKembali.addStretch(1)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.box)
        self.vbox.addWidget(QLabel())
        self.vbox.addLayout(self.hboxP)
        self.vbox.addLayout(self.hboxBTN)
        self.vbox.addWidget(QLabel())
        self.vbox.addLayout(self.hboxHasil)
        self.vbox.addWidget(QLabel())
        self.vbox.addLayout(self.hboxKembali)
        self.vbox.addStretch(1)
        self.setLayout(self.vbox)

    def hitungan(self):
        try:
            panjang = float(self.pjgss.text())
            keliling = (panjang)*4
            self.itung.setText(str(keliling))

        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Alert")
            msg.setText("sepertinya ada yang belum terisi")
            msg.exec_()

class HalamanLuasPersegi(QWidget):
    def setupPage(self,Window_go):
        self.box = QVBoxLayout()
        self.judul = QLabel("Luas Persegi")
        self.judul.setAlignment(Qt.AlignCenter)
        self.box.addWidget(self.judul)

        # panjang
        self.hboxP = QHBoxLayout()
        self.pjg = QLabel("Sisi :")
        self.pjgss = QLineEdit()
        self.hboxP.addWidget(self.pjg)
        self.hboxP.addWidget(self.pjgss)

        # btn hitung
        self.hboxBTN = QHBoxLayout()
        self.submit = QPushButton("Hitung !!")
        self.submit.clicked.connect(self.hitungan)
        self.hboxBTN.addWidget(self.submit)
        self.hboxBTN.addStretch(1)

        # hasil
        self.hboxHasil = QHBoxLayout()
        self.hasil = QLabel("Luas Persegi =")
        self.itung = QLabel()
        self.hboxHasil.addWidget(self.hasil)
        self.hboxHasil.addWidget(self.itung)

        # btn kembali
        self.hboxKembali = QHBoxLayout()
        self.kembali = QPushButton("<< kembali")
        self.hboxKembali.addWidget(self.kembali)
        self.hboxKembali.addStretch(1)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.box)
        self.vbox.addWidget(QLabel())
        self.vbox.addLayout(self.hboxP)
        self.vbox.addLayout(self.hboxBTN)
        self.vbox.addWidget(QLabel())
        self.vbox.addLayout(self.hboxHasil)
        self.vbox.addWidget(QLabel())
        self.vbox.addLayout(self.hboxKembali)
        self.vbox.addStretch(1)
        self.setLayout(self.vbox)

    def hitungan(self):
        try:
            panjang = float(self.pjgss.text())
            luas = panjang*panjang
            self.itung.setText(str(luas))

        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Alert")
            msg.setText("sepertinya ada yang belum terisi")
            msg.exec_()




class Window_go(QMainWindow):

    #menentukan ukuran window, + title dan menampilkan 
    def __init__(self,parent=None): 
        super(Window_go,self).__init__(parent) 

        self.setWindowTitle("Pemdesk") 
        self.setGeometry(300, 200, 280, 200)
        self.startHomepage()

    def startHomepage(self):
        self.homepage = HomePage(self)
        self.setCentralWidget(self.homepage)
        self.homepage.btn1.clicked.connect(self.startHalamanluas)
        self.homepage.btn2.clicked.connect(self.startHalamankeliling)
        self.show()

    def startHalamanluas(self):
        self.halamanluas = HalamanLuas(self)
        self.setCentralWidget(self.halamanluas)
        self.halamanluas.setupPage(self)
        self.halamanluas.btn2.clicked.connect(self.startHalamanLuasPersegiPanjang)
        self.halamanluas.btn1.clicked.connect(self.startHalamanLuasPersegi)
        self.halamanluas.kembali.clicked.connect(self.startHomepage)
        self.show()

    def startHalamankeliling(self):
        self.halamankeliling = HalamanKeliling(self)
        self.setCentralWidget(self.halamankeliling)
        self.halamankeliling.setupPage(self)
        self.halamankeliling.btn2.clicked.connect(self.startHalamanKelilingPersegiPanjang)
        self.halamankeliling.btn1.clicked.connect(self.startHalamanKelilingPersegi)
        self.halamankeliling.kembali.clicked.connect(self.startHomepage)
        self.show()

    def startHalamanLuasPersegiPanjang(self):
        self.halamanLuasPP = HalamanLuasPersegiPanjang(self)
        self.setCentralWidget(self.halamanLuasPP)
        self.halamanLuasPP.setupPage(self)
        self.halamanLuasPP.kembali.clicked.connect(self.startHalamanluas)
        self.show()

    def startHalamanKelilingPersegiPanjang(self):
        self.halamanKelilingPP = HalamanKelilingPersegiPanjang(self)
        self.setCentralWidget(self.halamanKelilingPP)
        self.halamanKelilingPP.setupPage(self)
        self.halamanKelilingPP.kembali.clicked.connect(self.startHalamankeliling)
        self.show()

    def startHalamanKelilingPersegi(self):
        self.halamanKelilingPsg = HalamanKelilingPersegi(self)
        self.setCentralWidget(self.halamanKelilingPsg)
        self.halamanKelilingPsg.setupPage(self)
        self.halamanKelilingPsg.kembali.clicked.connect(self.startHalamankeliling)
        self.show()

    def startHalamanLuasPersegi(self):
        self.halamanLuasPsg = HalamanLuasPersegi(self)
        self.setCentralWidget(self.halamanLuasPsg)
        self.halamanLuasPsg.setupPage(self)
        self.halamanLuasPsg.kembali.clicked.connect(self.startHalamanluas)
        self.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window_go()
    sys.exit(app.exec_())
