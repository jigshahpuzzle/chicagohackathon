import PIL
from PIL import Image

def resizeToSquare(path):
	img = Image.open(path)
	imgW = float(img.size[0])
	imgH = float(img.size[1])
	imgRatio = imgH / imgW
	if imgRatio > 0.7 or imgRatio < 1.3
	img = img.resize((500,500), PIL.Image.ANTIALIAS)
	img.save('output' + path)
