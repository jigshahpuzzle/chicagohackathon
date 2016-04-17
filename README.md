# chicagohackathon
Melanoma Detection Neural Net

Original convolutional neural network code from here: https://github.com/nicholas-leonard/dp/blob/master/examples/convolutionneuralnetwork.lua

Source code for our convolutional neural network:
http://deeplearning.net/tutorial/code/convolutional_mlp.py

Our project involved using a Flask web frontend along with the twilio API to enable users to send pictures to a server.

Said server contains a Theano-based, CUDA-accelerated (pyconv/theanorc.txt) convolutional neural network (pyconv/convolutional_mlp.py) which outputs the post-training neural net to a .pkl file (pyconv/net.pkl). The machine learning algorithm would return a 'score' corresponding to its confidence in categorizing the image as containing a melanoma, which pyconv/predict.py would use to make a recommendation, which it would pass back to the Flask frontend.

The neural network was trained using the University of Waterloo's melanoma cancer image data set. We regularized the images (see pyconv/images) to the same aspect ratio and size, to enable proper training of a convolutional neural network for feature extraction.

As was the case with the MNIST and CFAR datasets (both of which we used to check that the convolutional net trained properly), we needed to serialize the dataset to the .pkl file format (pyconv/my_data.pkl), as well as the images that we received from the end user.

Proper serialization to the .pkl file format is the main remaining issue.
