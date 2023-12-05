import numpy as np
from random import random

def normalize(out_values):
    return out_values

def mix(mat1, mat2, coef):
    res = np.array([[0] * len(mat1[0]) for _ in range(len(mat1))])

    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            res[i][j] = mat1[i][j] * coef + mat2[i][j] * (1 - coef)
    
    return res

class NN:

    def __init__(self, shape) -> None:
        self.shape = shape
        self.create_matrix()
    
    def create_matrix(self):
        self.hidden_matrix = np.random.rand(self.shape[1], self.shape[0])
        self.hidden_bias = np.random.rand(self.shape[1], 1)
        self.out_matrix = np.random.rand(self.shape[2], self.shape[1])
        self.out_bias = np.random.rand(self.shape[2], 1)
    
    def predict(self, input):
        self.hidden_values = self.hidden_matrix.dot(input) + self.hidden_bias
        self.out_values = self.out_matrix.dot(self.hidden_values) + self.out_bias
        return np.argmax(self.out_values)
    
    def cross(self, nn):
        r = random()
        child1 = NN(self.shape)
        child2 = NN(self.shape)
        print(1, self.hidden_bias)
        print(2, child1.hidden_bias)
        child1.hidden_matrix = mix(self.hidden_matrix, nn.hidden_matrix, r)
        child2.hidden_matrix = mix(self.hidden_matrix, nn.hidden_matrix, 1-r)

        child1.hidden_bias = mix(self.hidden_bias, nn.hidden_bias, r)
        child2.hidden_bias = mix(self.hidden_bias, nn.hidden_bias, 1-r)

        child1.out_matrix = mix(self.out_matrix, nn.out_matrix, r)
        child2.out_matrix = mix(self.out_matrix, nn.out_matrix, 1-r)

        child1.out_bias = mix(self.out_bias, nn.out_bias, r)
        child2.out_bias = mix(self.out_bias, nn.out_bias, 1-r)

        return child1, child2