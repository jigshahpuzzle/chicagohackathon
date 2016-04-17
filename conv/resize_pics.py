# Requires pip install Pillow
import PIL
from PIL import Image

def resizeToSquare(path):
	img = Image.open(path)
	imgW = float(img.size[0])
	imgH = float(img.size[1])
	imgRatio = imgH / imgW
	if imgW == imgH:
		img = img.resize((512,512), PIL.Image.ANTIALIAS)
		img.save('output' + path)
	elif imgW > imgH: 
		widthRatio = 512 / float(imgW)
		img = img.resize(widthRatio * imgW, widthRatio * imgH), PIL.Image.ANTIALIAS)
		img.save('output' + path)
		img_size = img.size
		new_size = (512, 512)
		new_im = Image.new("RGB", new_size)   ## luckily, this is already black!
		new_im.paste(img, ((new_size[0]-img_size[0])/2,
		                      (new_size[1]-img_size[1])/2))
		new_im.save('output' + path)
	elif imgW < imgH: 
		heighRatio = 512 / float(imgH)
		img = img.resize(heighRatio * imgW, heighRatio * imgH), PIL.Image.ANTIALIAS)
		img_size = img.size

		new_size = (512, 512)
		new_im = Image.new("RGB", new_size)   ## luckily, this is already black!
		new_im.paste(img, ((new_size[0]-img_size[0])/2,
		                      (new_size[1]-img_size[1])/2))


		new_im.save('output' + path)




