import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

#membuat fungsi utk menentukan layout window
def window_go():
    #inisialisasi pyqt
    app = QApplication(sys.argv)
    window = QWidget()

    #menyiapkan label, menempelkan label ke window
    #settext, dan posisi
    a = 10
    for i in range(10):
        textLabel = QLabel(window)
        kata = "Hello World! ke-{}".format(i+1)
        textLabel.setText(kata)
        textLabel.move(110,a)
        a += 15

    #menentukan ukuran window, + title dan menampilkan
    window.setGeometry(50,50,320,200)
    window.setWindowTitle("PyQt5 contoh")
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window_go()
