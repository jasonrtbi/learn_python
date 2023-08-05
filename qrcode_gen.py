import pyqrcode 
from pyqrcode import QRCode 
  
s = "https://www.google.com"  # String which represent the QR code 
  
url = pyqrcode.create(s)  # Generate QR code 
  
url.svg("myyoutube.svg", scale = 8)  # Create and save the png file naming "myqr.png" 
