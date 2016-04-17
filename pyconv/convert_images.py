import cPickle


my_x = []
my_y = []
with open('path_to_file', 'r') as f:
    for line in f:
        my_list = line.split(' ') # replace with your own separator instead
        my_x.append(my_list[1:-1]) # omitting identifier in [0] and target in [-1]
        my_y.append(my_list[-1])
train_set_x = theano.shared(numpy.array(my_x, dtype='float64'))
train_set_y = theano.shared(numpy.array(my_y, dtype='float64'))

f = file('train_set.pkl', 'wb')
    cPickle.dump((train_set_x, train_set_y), f, protocol=cPickle.HIGHEST_PROTOCOL)
f.close()


my_x = []
my_y = []
with open('path_to_file', 'r') as f:
    for line in f:
        my_list = line.split(' ') # replace with your own separator instead
        my_x.append(my_list[1:-1]) # omitting identifier in [0] and target in [-1]
        my_y.append(my_list[-1])
valid_set_x = theano.shared(numpy.array(my_x, dtype='float64'))
valid_set_y = theano.shared(numpy.array(my_y, dtype='float64'))

f = file('valid_set.pkl', 'wb')
    cPickle.dump((valid_set_x, valid_set_y), f, protocol=cPickle.HIGHEST_PROTOCOL)
f.close()


my_x = []
my_y = []
with open('path_to_file', 'r') as f:
    for line in f:
        my_list = line.split(' ') # replace with your own separator instead
        my_x.append(my_list[1:-1]) # omitting identifier in [0] and target in [-1]
        my_y.append(my_list[-1])
test_set_x = theano.shared(numpy.array(my_x, dtype='float64'))
test_set_y = theano.shared(numpy.array(my_y, dtype='float64'))


f = file('test_set.pkl', 'wb')
    cPickle.dump((test_set_x, test_set_y), f, protocol=cPickle.HIGHEST_PROTOCOL)
f.close()



