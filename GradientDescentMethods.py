import readMnist
import numpy as np





"""
data- a n ˆ d matrix, where n is the amount of samples, and d is the dimension
of each sample
labels- a n ˆ 1 matrix with the labels of each sample
iters - an integer that will define the amount of iterations.
eta - a positive number that will define the learning rate.

:returna  d * iters matrix, where in its i-th column it will contain
the output of the sub-gradient descent algorithm over i iterations.
"""
def GD(data, label, iter, eta):
    #use the whole data here.

    dim = len(data[0])
    w = np.zeros(dim)
    out = np.array([w])

    for i in range(iter):
        v_t = grad_f(w)
        w = w - (eta * v_t)
        np.vstack((out,w))

    return out


""""
batch- The amount of samples that the algorithm would draw and use at each
iteration.
"""
def SGD(data, label, iters, eta, batch):
    pass


def testError(w, testData, testLabels):
    pass

