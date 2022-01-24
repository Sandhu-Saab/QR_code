import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "DAKU SANDHU"
a = "https://www.youtube.com/channel/UCYlF1FEQxeWxqoLzJBLBKCw"
  
# Generate QR code 
url = pyqrcode.create(s)
url1 = pyqrcode.create(a) 
  
# Create and save the png file naming "myqr.png" 
url.svg("myQR.svg", scale = 8) 
url1.svg("myQR1.svg", scale = 8)