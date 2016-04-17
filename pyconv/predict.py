from __future__ import print_function

import os
import sys
import timeit

import numpy

import theano
import theano.tensor as T
from theano.tensor.signal import downsample
from theano.tensor.nnet import conv2d

from logistic_sgd import LogisticRegression, load_data
from mlp import HiddenLayer


  def predict(model='./testing/model.pkl', 
            testset='./testing/testset.pkl',
            batch_size=5):

      """ Load a trained model and use it to predict labels.

      :type model: Layers to accept inputs and produce outputs.
      """

      # Load the saved model.
      classifiers = cPickle.load(model)

      # Pick out the individual layer
      layer0_input = classifiers[0]
      layer0 = classifiers[1]
      layer1 = classifiers[2]
      layer2_input = classifiers[3]
      layer2 = classifiers[4]
      layer3 = classifiers[5]

      # Apply it to our test set
      testsets = load_data(testset)
      test_set_x = testsets.get_value()

      # compile a predictor function
      index = T.lscalar()

      predict_model = theano.function(
          [layer0_input],
          layer3.y_pred,
      )

      predicted_values = predict_model(
          test_set_x[:batch_size].reshape((batch_size, 1, 28, 23))
      )

      print('Prediction complete.')
      return predicted_values
