#!/usr/bin/env python

import numpy as np
from tqdm import tqdm

# we have only one neuron
NEURONS = 1 

# learning rate
LEARNING_RATE = 0.01

# number of iterations
NUM_OF_ITERS = 100000

# small difference to be able to approximately calculcate derivative
EPSILON = 0.01


class TwoVariablesBooleanFunctionNeuralNetwork:
    def __init__(self, x, y):
        #  - n rows: the number of samples
        self.n = x.shape[0]

        #  - m columns: the number of input variables
        self.m = x.shape[1]

        # x is a np.array which is a n x m matrix. It has:
        #  - n rows: the number of samples
        #  - m columns: the number of input variables
        self.input = x 
        
        # np.shape returns a tuple: (n,m)
        # W is a matrix of m x l:
        #  - m rows: the number of input variables
        #  - l columns: the number of neurons
        self.W = np.random.rand(self.m, NEURONS)

        # y and output are column vectors of size n
        self.y      = y
        self.output = np.zeros(self.y.shape)


    def feedforward(self):
        self.output = sigmoid(np.dot(self.input, self.W))


    def J(self, W):
        # here the np.dot multiplication will give back
        # a column vector, which we reshape (so that it will
        # be transposed to a row vector), and then squeeze (to
        # get rid of the extra dimension)
        g_xw = np.array(sigmoid(np.dot(self.input, W))).reshape(1,-1).squeeze()

        # calculate the difference between our hypothesis and 
        # the desired values
        err_diff = self.y - g_xw

        # return the error as sum of squared difference
        return (1 / self.n) * np.sum(np.square(err_diff))


    def W_i_plus(self, i):
        W_copy = self.W.copy()
        W_copy[i][0] = W_copy[i][0] + EPSILON
        return W_copy


    def W_i_minus(self, i):
        W_copy = self.W.copy()
        W_copy[i][0] = W_copy[i][0] - EPSILON
        return W_copy


    def delta_J_i(self, i):
        return (
            (self.J(self.W_i_plus(i)) - self.J(self.W_i_minus(i))) / (2*EPSILON)
        )


    def backprop(self):
        delta_J = []

        for i in range(0,self.m):
            delta_J += [self.delta_J_i(i)]

        delta_J = np.array(delta_J).reshape(-1,1)

        self.W -= LEARNING_RATE * delta_J


def sigmoid(x):
    return 1/(1+np.exp(-x))


if __name__ == "__main__":
    x = np.array([[1,0,0],
                  [1,0,1],
                  [1,1,0],
                  [1,1,1]])

    y = np.array([0,0,0,1])

    nn = TwoVariablesBooleanFunctionNeuralNetwork(x,y)
    
    pbar = tqdm(total = NUM_OF_ITERS)

    for i in range(0, NUM_OF_ITERS):
        nn.feedforward()
        nn.backprop()
        pbar.update(1)

    print("Number of iterations: {}".format(NUM_OF_ITERS))
    print("Weights (W0, W1, ... Wm):\n{}".format(nn.W))
    print("Output (h_W(x)_0, h_W(x)_1, ... h_W(x)_n):\n{}".format(nn.output))
