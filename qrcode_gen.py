import pyqrcode 
from pyqrcode import QRCode 

print('Paste your link or anything info you want to convert to QR code here')
s = input()

url = pyqrcode.create(s)  # Generate QR code 
  
url.svg("myyoutube.svg", scale = 8)  # Create and save the png file naming "myqr.png" 
