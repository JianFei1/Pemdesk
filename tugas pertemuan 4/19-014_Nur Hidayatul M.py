import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Window_go(QWidget):

    #menentukan ukuran window, + title dan menampilkan 
    def __init__(self): 
        super().__init__() 

        self.setWindowTitle("Pemdesk") 
        self.setGeometry(300, 100, 500, 400)
        self.createLayout()
        self.show()
    
    def createLayout(self):

        window = QWidget()

        # layout induk

        self.induk = QGridLayout()
        
        # label dan combo box bagian atas
        self.lb1 = QLabel("Style :")
        self.option = QComboBox()
        self.option.addItems([
            "Klasik",
            "Woodie's",
            "Camarilla",
            "De Mark"
        ]) 

        #  check box atas

        cekk = QCheckBox("Use Style Standard Pallets")
        cekk.setChecked(True)
        cek1 = QCheckBox("Disable widgets")
        cek1.setChecked(False)

        # add widget
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.lb1)
        self.hbox.addWidget(self.option)
        self.hbox.addStretch(1)
        self.hbox.addWidget(cekk)
        self.hbox.addWidget(cek1)


        # group 1 

        radiobutton1 = QRadioButton("radio button 1")
        radiobutton1.setChecked(True)
        radiobutton2 = QRadioButton("radio button 2")
        radiobutton2.setChecked(False)
        radiobutton3 = QRadioButton("radio button 3")
        radiobutton3.setChecked(False)
        checkbox = QCheckBox(" tristate radio button ")
        checkbox.setTristate(True)
        checkbox.setCheckState(Qt.PartiallyChecked)

        self.formGroupBox1 = QGroupBox()
        vbox1 = QVBoxLayout()
        vbox1.addWidget(radiobutton1)
        vbox1.addWidget(radiobutton2)
        vbox1.addWidget(radiobutton3)
        vbox1.addWidget(checkbox)
        vbox1.addStretch(1)
        self.formGroupBox1.setLayout(vbox1)

        # group 2

        pushButton = QPushButton("Default Push Button")
        pushButton.setStyleSheet("background-color : lightblue")
        self.pushButtonToogle = QPushButton("Toogle Push Button")
        self.pushButtonToogle.setCheckable(True)
        self.pushButtonToogle.setStyleSheet("background-color : lightgrey")
        self.pushButtonToogle.clicked.connect(self.gantiWarnaButton)
        self.pushButtonFlat = QPushButton("flat push button")
        self.pushButtonFlat.setFlat(True)
        self.formGroupBox2 = QGroupBox()
        vbox2 = QVBoxLayout()
        vbox2.addWidget(pushButton)
        vbox2.addWidget(self.pushButtonToogle)
        vbox2.addWidget(self.pushButtonFlat)
        vbox2.addStretch(1)
        self.formGroupBox2.setLayout(vbox2)

        # group 3

        tab = QTabWidget()
        table = QTableWidget(4,3)

        tab1 = QWidget()
        tab2 = QWidget()
        hbox = QHBoxLayout()
        hbox.setContentsMargins(5, 5, 5, 5)
        hbox.addWidget(table)
        tab1.setLayout(hbox)

        textEdit = QTextEdit(window)
        hbox2 = QHBoxLayout()
        hbox2.setContentsMargins(5, 5, 5, 5)
        hbox2.addWidget(textEdit)
        tab2.setLayout(hbox2)

        tab.addTab(tab1,"Table")
        tab.addTab(tab2,"Text Edit")


        # group 4

        pasw = QLineEdit("kang mustafit")
        pasw.setEchoMode(QLineEdit.Password)

        spn = QSpinBox()
        spn.setValue(50)

        tanggal = QDateTimeEdit(window)
        tanggal.setDateTime(QDateTime.currentDateTime())

        slider = QSlider(Qt.Horizontal,window)
        slider.setValue(50)
        
        scrollBar = QScrollBar(Qt.Horizontal, window)
        scrollBar.setValue(60)

        dial = QDial(window)
        dial.setValue(30)
        dial.setNotchesVisible(True)

        grid = QGridLayout()
        grid.addWidget(slider,1,0)
        grid.addWidget(scrollBar,2,0)
        grid.addWidget(dial,1,1,2,1)


        self.formGroupBox4 = QGroupBox()
        groupG4 = QVBoxLayout()
        groupG4.addWidget(pasw)
        groupG4.addWidget(spn)
        groupG4.addWidget(tanggal)
        groupG4.addLayout(grid)
        self.formGroupBox4.setLayout(groupG4)

        # group 5

        progressbar = QProgressBar()
        progressbar.setRange(0,100)
        progressbar.setValue(22)


        # set widget dan layout

        g1 = QLabel("Group 1")
        bok1=QVBoxLayout()
        bok1.addWidget(g1)
        bok1.addWidget(self.formGroupBox1)

        g2 = QLabel("Group 2")
        bok2=QVBoxLayout()
        bok2.addWidget(g2)
        bok2.addWidget(self.formGroupBox2)

        bok3=QVBoxLayout()
        bok3.addWidget(tab)

        g4 = QCheckBox("Group 4")
        g4.setChecked(True)
        bok4=QVBoxLayout()
        bok4.addWidget(g4)
        bok4.addWidget(self.formGroupBox4)

        bok5 = QVBoxLayout()
        bok5.addWidget(progressbar)


        self.induk.addLayout(self.hbox,0,0,1,2)
        self.induk.addLayout(bok1,1,0)
        self.induk.addLayout(bok2,1,1)
        self.induk.addLayout(bok3,2,0)
        self.induk.addLayout(bok4,2,1)
        self.induk.addLayout(bok5,3,0,1,2)
        self.induk.setRowStretch(1, 1)
        self.induk.setRowStretch(2, 1)
        self.induk.setColumnStretch(0, 1)
        self.induk.setColumnStretch(1, 1)

        self.setLayout(self.induk)


    def gantiWarnaButton(self):
        if self.pushButtonToogle.isChecked():
            self.pushButtonToogle.setStyleSheet("background-color : lightblue")
        else:
            self.pushButtonToogle.setStyleSheet("background-color : lightgrey")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window_go()
    sys.exit(app.exec_())
