import pyqrcode
import png
from pyqrcode import QRCode

# Saving your QR Code in .png format
def savePng(uid):
    url = pyqrcode.create(uid)
    url.png('{0}.png'.format(uid), scale=6)

# Saving your QR Code in .svg format
def saveSvg(uid):
    url = pyqrcode.create(uid)
    url.svg("{0}.svg".format(uid), scale=8)