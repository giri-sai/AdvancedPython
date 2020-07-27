import qrcode
st = 'Giri Sai Chandu'
qr = qrcode.main.QRCode.make(st)
qr.save('hi.png')
qr.show()



