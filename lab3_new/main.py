from PIL import Image
from PyQt6.QtCore import Qt
import numpy as np

from design import *


def get8bits(num):
    base = 2
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    n = 8 - len(newNum)
    newNum = "0" * n + newNum
    return newNum


def getdata():
    path = ui.path_to_pic_label.text()
    if path != "Текущий путь к картинке":
        image = Image.open(path)
        pixels = image.load()
        print(pixels[1, 1])


def getstring():
    string = ui.ascii_string.text()
    a = []
    for i in string:
        a.append(ord(i))
    return a


def getscratch(pixels, h, w):
    dst = np.zeros((h, w, 3))
    for i in range(h):
        for j in range(w):
            p = pixels[j, i]
            dst[i, j] = p
    return dst


def conceal():
    a = getstring()
    path = ui.path_to_pic_label.text()
    image = Image.open(path)
    pixels = image.load()
    i1 = 0
    flag = 0
    dst = getscratch(pixels, image.height, image.width)
    i = 0
    j = 0
    while True:
        bitstring = get8bits(a[i1])
        bits = []
        index = 0
        for h in range(8):
            bits.append(bitstring[h])
        p1 = (int(bits[index + 7]), int(bits[index + 6]), int(bits[index + 5]))
        p2 = (int(bits[index + 4]), int(bits[index + 3]), int(bits[index + 2]))
        tempi = i
        tempj = j
        if j + 2 >= image.width:
            tempi += 1
            tempj -= 2
            j
        p3 = (int(bits[index + 1]), int(bits[index]), dst[tempi, tempj][2])
        index += 8
        i1 += 1

        if j == image.width:
            j = 0
            i += 1
            if i == image.height:
                break
        dst[i, j] = p1
        j += 1

        if j == image.width:
            j = 0
            i += 1
            if i == image.height:
                break
        dst[i, j] = p2
        j += 1

        if j == image.width:
            j = 0
            i += 1
            if i == image.height:
                break
        dst[i, j] = p3
        j += 1

        if j == image.width:
            j = 0
            i += 1
            if i == image.height:
                break

        if i1 + 1 > len(a):
            break
    print("i = ", i, " j = ", j)
    print(image.width, len(dst[0]))
    img2 = Image.fromarray(np.uint8(dst))
    img2.save("3.bmp", "bmp")


def add_functions(ui):
    ui.path.clicked.connect(lambda: ChoiceImages())
    ui.concealment.clicked.connect(lambda: conceal())



def ChoiceImages():
    Image_path = QtWidgets.QFileDialog.getOpenFileNames(MainWindow, "Выберите картинку", None, "*.bmp")
    if len(Image_path[0]) != 0:
        path = str(Image_path[0])
        path = path.replace('[', '')
        path = path.replace(']', '')
        path = path.replace("'", '')
        ui.path_to_pic_label.setText(path)
        pixmap = QtGui.QPixmap(path)
        aspectRatio = pixmap.width() / pixmap.height()
        pixmap.scaled(int(280 * aspectRatio), 280)
        ui.image.setPixmap(pixmap.scaled(int(280 * aspectRatio), 280))
        getdata()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    add_functions(ui)
    sys.exit(app.exec())
