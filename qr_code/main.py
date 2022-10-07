import sys

# Pre-built CPU-only OpenCV packages for Python
import cv2
# QR Code generator
# https://bit.ly/2Lqmkmn
import qrcode

# https://pypi.org/project/PyQt5/
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui


class MyGui(QMainWindow):
    def __init__(self):
        super(MyGui, self).__init__()
        uic.loadUi("qrcodegui.ui", self)
        self.show()

        self.current_file = ""
        self.actionLoad.triggered.connect(self.load_image)
        self.actionSave.triggered.connect(self.save_image)
        self.actionQuit.triggered.connect(self.quit_program)
        self.pushButton.clicked.connect(self.generate_code)
        self.pushButton_2.clicked.connect(self.read_code)

    def load_image(self):
        options = QFileDialog.Options()
        # Open a file with the specified extensions
        filename, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "PDF (*.pdf), PNG (*.png)", options=options)

        if filename != "":
            self.current_file = filename
            pixmap = QtGui.QPixmap(self.current_file)
            pixmap = pixmap.scaled(300, 300)
            self.label.setScaledContents(True)
            self.label.setPixmap(pixmap)

    def generate_code(self):
        qr = qrcode.QRCode(version=1,
                            error_correction=qrcode.constants.ERROR_CORRECT_L,
                            box_size=20, border=2)
        qr.add_data(self.textEdit.toPlainText())
        qr.make(fit=True)
        # Save the QRCode in black and white
        img = qr.make_image(fill_color=(13, 13, 13), back_color=(242, 242, 242))
        img.save("images/currentqr.png")
        # Make it appear in the gui
        pixmap = QtGui.QPixmap("images/currentqr.png")
        pixmap = pixmap.scaled(300, 300)
        self.label.setScaledContents(True)
        self.label.setPixmap(pixmap)

    def read_code(self):
        img = cv2.imread(self.current_file)
        detector = cv2.QRCodeDetector()
        data, _, _ = detector.detectAndDecode(img)
        self.textEdit.setText(data)

    def save_image(self):
        # Save a PNG file with the QRCode generated
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "PNG (*.png)",
                                                options=options)

        if filename != "":
            img = self.label.pixmap()
            img.save(filename, 'PNG')

    def quit_program(self):
        sys.exit(0)

def main():
    app = QApplication([])
    window = MyGui()
    app.exec_()


if __name__ == '__main__':
    main()
