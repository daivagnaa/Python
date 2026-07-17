# Automatic QR Code Generator for a URL

import qrcode
url = input("Enter Your URL")
filename = input("Filename you wanna save it as")
if not (filename.endswith('.png')):
    filename = filename + '.png'

img = qrcode.make(url)
img.save(filename)