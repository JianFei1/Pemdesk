import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Window_go(QMainWindow):

    #menentukan ukuran window, + title dan menampilkan 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("Pemdesk") 
        self.setGeometry(100, 100, 600, 500) 
        self.UiComponents() 
        self.tulisan() 
        self.show() 

    #membuat teks
    def tulisan(self):
        self.label_2 = QLabel("kotak angka", self)
        self.label_2.setStyleSheet("font-size : 15px")
        self.label_2.move(30, 5) 

  
    # method untuk button
    def UiComponents(self):

        letak = 30 
        tulis = 1

        for i in range(5):
            
            tulisKotak = str(tulis)
            # membuat push button
            button = QPushButton(tulisKotak, self) 
            button.setStyleSheet("background-color: #87b4e7 ; color : red ; font-size : 40px; font-weight: bold;")

            # setting geometry button 
            button.setGeometry(letak, 40, 50, 50)
            tulis += 1
            letak += 60

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window_go()
    sys.exit(app.exec_())