from PIL import Image
filename = r'ja.ico'

img = Image.open(filename)
icon_sizes = [(16,16),(32,32),(48,48),(64,64)]
img.save('ja.icns',size=icon_sizes)
