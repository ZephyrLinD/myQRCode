import qrcode
import time
from PIL import Image
import matplotlib.pyplot as plt

def getSSRCode(self, parameter_list):
    pass

def getName():
    timeNow = time.strftime("%Y-%m-%d", time.localtime())
    nameStr = timeNow + '_QRCode.png'
    return nameStr

def getQR(str):
    qrImgInfo = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4
    )
    dataInfo = input("Please enter the data to be converted to QR code: ")
    qrImgInfo.add_data(dataInfo)
    qrImgInfo.make(fit = True)
    img = qrImgInfo.make_image()

    img.save(str)

    print("\033[0;36m\n-----------------------------------------------------------------------------------\033[0m")
    print("\033[32mThe QRCode image has been saved in this direction. \nName as: ", str, "\033[0m")
    print("\033[0;36m-----------------------------------------------------------------------------------\n\033[0m")

if __name__ == "__main__":
    getQR(getName())