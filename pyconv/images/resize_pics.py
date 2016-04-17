# Requires pip install Pillow
import PIL
from PIL import Image
import numpy as np
from six.moves import cPickle
import os

def resizeToSquare(path, output):
	print("resizing")
	img = Image.open(path)
	imgW = float(img.size[0])
	imgH = float(img.size[1])
	imgRatio = imgH / imgW
	if imgW == imgH:
		img = img.resize((512,512), PIL.Image.ANTIALIAS)
		img.save('output' + path)
		img.convert("LA")
		result = np.array(img)
		result = result.flatten()
		file = open(os.path.realpath('../pyconv/images/image.pkl'), 'wb')
		cPickle.dump(result, file)
		file.close()
	elif imgW > imgH: 
		widthRatio = 512 / float(imgW)
		img = img.resize((int(widthRatio * imgW), int(widthRatio * imgH)), PIL.Image.ANTIALIAS)
		img.save(output)
		img_size = img.size
		new_size = (512, 512)
		new_im = Image.new("L", new_size) 
		new_im.paste(img, ((new_size[0]-img_size[0])/2,
		                      (new_size[1]-img_size[1])/2))
		new_im.save(output)
		result = np.array(new_im)
		result = result.flatten()
		file = open(os.path.realpath('../pyconv/images/image.pkl'), 'wb')
		cPickle.dump(result, file)
		file.close()
	elif imgW < imgH: 
		heighRatio = 512 / float(imgH)
		img = img.resize((int(heighRatio * imgW), int(heighRatio * imgH)), PIL.Image.ANTIALIAS)
		img_size = img.size

		new_size = (512, 512)
		new_im = Image.new("L", new_size)  
		new_im.paste(img, ((new_size[0]-img_size[0])/2,
		                      (new_size[1]-img_size[1])/2))

		new_im.save(output)
		result = np.array(new_im)
		result = result.flatten()
		file = open(os.path.realpath('../pyconv/images/image.pkl'), 'wb')
		cPickle.dump(result, file)
		file.close()



if __name__ == "__main__":
	pathlist = []
	fo = open("names.txt", "r")
	pathlist = fo.read().split("\n")
	for x, item in enumerate(pathlist):
		resizeToSquare("skin_data/notmelanoma/dermquest/" + item, "cleaned" + str(x) + ".jpg")

