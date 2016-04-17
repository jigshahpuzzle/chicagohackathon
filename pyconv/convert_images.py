import cPickle
from PIL import Image
import numpy
import theano


if __name__ == "__main__":


	with open("groups.txt", "r") as f:
		names = f.read()
		names = names.split("*")
		train = []
		test = []
		validate = []
		for n, item in enumerate(names):
			if n == 0:
				train = item.split("\n")
			if n == 1:
				test = item.split("\n")
			if n == 2:
				validate = item.split("\n")
		print train
		print test
		print validate


	my_x = []
	my_y = []
	for item in train:
		if item:
			im = Image.open("skin_data/" + item).convert('L')
			pixels = list(im.getdata())
			width, height = im.size
			pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
			pixels2 = []
			for lst in pixels:
				for num in lst:
					pixels2.append(float(num))

			my_x.append(pixels2)
			if "mmdermis" in item or "mmdermquest" in item:
				my_y.append([0])
			else:
				my_y.append([1])


	train_set_x = theano.shared(numpy.array(my_x, dtype='float64'))
	train_set_y = theano.shared(numpy.array(my_y, dtype='float64'))

	f = file('train_set.pkl', 'wb')
	cPickle.dump((train_set_x, train_set_y), f, protocol=cPickle.HIGHEST_PROTOCOL)
	f.close()


	my_x = []
	my_y = []
	for item in validate:
		if item:
			im = Image.open("skin_data/" + item).convert('L')
			pixels = list(im.getdata())
			width, height = im.size
			pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
			pixels2 = []
			for lst in pixels:
				for num in lst:
					pixels2.append(float(num))
			print(len(pixels2))

			my_x.append(pixels2)
			if "mmdermis" in item or "mmdermquest" in item:
				my_y.append([0])
			else:
				my_y.append([1])
		print(len(my_x))
		print(len(my_y))

	valid_set_x = theano.shared(numpy.array(my_x, dtype='float64'))
	valid_set_y = theano.shared(numpy.array(my_y, dtype='float64'))

	f = file('valid_set.pkl', 'wb')
	cPickle.dump((valid_set_x, valid_set_y), f, protocol=cPickle.HIGHEST_PROTOCOL)
	f.close()


	my_x = []
	my_y = []
	for item in test:
		if item:
			im = Image.open("skin_data/" + item).convert('L')
			pixels = list(im.getdata())
			width, height = im.size
			pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
			pixels2 = []
			for lst in pixels:
				for num in lst:
					pixels2.append(float(num))

			my_x.append(pixels2)
			if "mmdermis" in item or "mmdermquest" in item:
				my_y.append([0])
			else:
				my_y.append([1])
			print(len(my_x))
			print(len(my_y))

	test_set_x = theano.shared(numpy.array(my_x, dtype='float64'))
	test_set_y = theano.shared(numpy.array(my_y, dtype='float64'))


	f = file('test_set.pkl', 'wb')
	cPickle.dump((test_set_x, test_set_y), f, protocol=cPickle.HIGHEST_PROTOCOL)
	f.close()
	f = file('my_data.pkl', 'wb')
	cPickle.dump(((train_set_x, train_set_y), (valid_set_x, valid_set_y), (test_set_x, test_set_y)), f, protocol=cPickle.HIGHEST_PROTOCOL)
	f.close()
