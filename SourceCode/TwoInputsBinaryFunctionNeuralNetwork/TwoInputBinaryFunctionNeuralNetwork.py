#!/usr/bin/env python

import numpy as np
from tqdm import tqdm

# we have only one neuron
LAYERS = 1 

# learning rate
LEARNING_RATE = 0.01

# number of iterations
NUM_OF_ITERS = 100000

# small difference to be able to approximately calculcate derivative
EPSILON = 0.01


class TwoInputBinaryFunctionNeuralNetwork:
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
        #  - l columns: the number of layers
        self.W = np.random.rand(self.m, LAYERS)

        # y and output are column vectors of size n
        self.y      = y
        self.output = np.zeros(self.y.shape)


    def feedforward(self):
        #self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.input, self.W))


    def J(self, W):
        x1w = np.dot(np.array(self.input[0]),W.T[0])
        x2w = np.dot(np.array(self.input[1]),W.T[0])
        x3w = np.dot(np.array(self.input[2]),W.T[0])
        x4w = np.dot(np.array(self.input[3]),W.T[0])

        g_xw = sigmoid(np.array([x1w, x2w, x3w, x4w]))
        err_diff = self.y - g_xw

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

    nn = TwoInputBinaryFunctionNeuralNetwork(x,y)
    
    pbar = tqdm(total = NUM_OF_ITERS)

    for i in range(0, NUM_OF_ITERS):
        nn.feedforward()
        nn.backprop()
        pbar.update(1)

    print("Weights (W0, W1, ... Wm):\n{}".format(nn.W))
    print("Output (h_W(x)_0, h_W(x)_1, ... h_W(x)_n):\n{}".format(nn.output))

