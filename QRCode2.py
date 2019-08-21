# -*- coding: utf-8 -*-
import qrcode
import time
from PIL import Image
import matplotlib.pyplot as plt

def getName():
    timeNow = time.strftime("%Y-%m-%d", time.localtime())
    nameStr = timeNow + '_QRCode.png'
    return nameStr

def getQR(fileName):
    dataStr = input("Please enter the data to be converted to QR code:")
    qrImgInfo = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 10,
        border = 4
    )
    qrImgInfo.add_data(dataStr)
    qrImgInfo.make(fit = True)
    
    # Process image
    img = qrImgInfo.make_image()
    img = img.convert("RGBA")

    icon = Image.open("logo.JPG")

    img_w, img_h = img.size
    factor = 4
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)

    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    icon = icon.convert("RGBA")
    img.paste(icon, (w, h), icon)

    img.save(fileName)

    print("\033[0;36m\n-----------------------------------------------------------------------------------\033[0m")
    print("\033[32mThe QRCode image has been saved in this direction. \nName as: ", fileName, "\033[0m")
    print("\033[0;36m-----------------------------------------------------------------------------------\n\033[0m")

if __name__ == "__main__":
    getQR(getName())