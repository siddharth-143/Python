"""
    Python program to implement QR code generator.

    link : https://github.com/Python-World
"""

import qrcode

input_url = "https://www.google.com/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

qr.add_data(input_url)
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="white")
img.save("url_qrcode.png")

print(qr.data_list)