import qrcode

url = input("Enter the URL: ")
filename = input("Enter the filename to save the content: ")
if not(filename.endswith(".png")):
    filename = f"{filename}.png"

img = qrcode.make(url)
img.save(filename)