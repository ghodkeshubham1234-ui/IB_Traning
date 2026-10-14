import qrcode  #pip install qrcode[pil]
qr=qrcode.make("www.linkedin.com/in/shubham-ghodke-05517a27a")
qr=qr.resize((200,200))
qr.save('qr.png')
