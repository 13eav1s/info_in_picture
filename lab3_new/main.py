from PIL import Image

from design import *


# Фукнция перевод строку в последовательность битов
def text_to_binary(value):
    return ''.join(f'{ord(i):08b}' for i in value)


def extract():
    image_path = ui.path_to_pic_label.text()
    if image_path == "Текущий путь к картинке":
        message = QtWidgets.QMessageBox()
        message.setText("Choose the picture!")
        message.exec()
        return 0
    flag = 0
    stop = '@'
    img = Image.open(image_path)
    width, height = img.size
    last_bits = ''
    secret_message = []
    for x in range(0, width):
        for y in range(0, height):
            pixel = list(img.getpixel((x, y)))
            for n in range(0, 3):
                last_bits += bin(pixel[n])[-1]
                secret_bits = [last_bits[i:i + 8] for i in range(0, len(last_bits), 8)]
                secret_message = [chr(int(secret_bits[i], 2)) for i in range(len(secret_bits))]

                if stop in secret_message:
                    flag = 1
        if flag:
            secret_text = ""
            i = 0
            while secret_message[i] != stop:
                secret_text += secret_message[i]
                i += 1
            message = QtWidgets.QMessageBox()
            message.setText(secret_text)
            message.exec()
            # print(secret_message[:secret_message.index(stop)])
            break
        else:
            message = QtWidgets.QMessageBox()
            message.setText("No secret message")
            message.exec()
            break


def encode():
    image_path = ui.path_to_pic_label.text()
    if image_path == "Текущий путь к картинке":
        message = QtWidgets.QMessageBox()
        message.setText("Choose the picture!")
        message.exec()
        return 0
    if ui.ascii_string.text() == "":
        message = QtWidgets.QMessageBox()
        message.setText("Type the string!")
        message.exec()
        return 0
    message_bin = text_to_binary(ui.ascii_string.text() + '@')

    try:
        img = Image.open(image_path)
        width, height = img.size
        index = 0
        for x in range(0, width):
            for y in range(0, height):
                pixel = list(img.getpixel((x, y)))
                for n in range(0, 3):
                    if index < len(message_bin):
                        pixel_bin = list(bin(pixel[n]))[2:]
                        while len(pixel_bin) < 8:
                            pixel_bin += ['0']
                        pixel_bin[-1] = message_bin[index]
                        pixel_bin = ''.join(pixel_bin)
                        pixel[n] = int(pixel_bin, 2)
                        index += 1
                img.putpixel((x, y), tuple(pixel))
        img.save('source_secret.bmp', 'BMP')

    except NameError:
        print("ERROR!")


def add_functions():
    ui.path.clicked.connect(lambda: ChoiceImages())
    ui.concealment.clicked.connect(lambda: encode())
    ui.string_extraction.clicked.connect(lambda: extract())


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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    add_functions()
    sys.exit(app.exec())
