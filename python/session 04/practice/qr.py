import qrcode
name = input("enter your name: ")
phone_number = input("enter your phone number: ")
text = "Hi "+name+" your phone number is:"+phone_number
img = qrcode.make(text)
# save img to a file
img.save("qr.png")
