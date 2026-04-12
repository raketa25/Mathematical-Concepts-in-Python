from functools import reduce
from math import exp
"""
This code defines a simple implementation of a neural network in Python. It consists of two classes: Neuron and NeuralNetwork.

The Neuron class represents a single neuron in the network. It has a name, a list of weights, an activation function, and methods to calculate the output based on the input entry. The output is calculated as the weighted sum of the inputs passed through the activation function.

The NeuralNetwork class represents the entire neural network. It takes a list of layers, where each layer is a list of neurons. The output method processes the input entry through each layer of the network, updating the entry with the outputs of the neurons in each layer. The final output is the output of the last neuron in the last layer. The class also includes two activation functions: sigmoid and relu, which can be used as the activation function for the neurons in the network.

"""

# The neuron class creation
class Neuron:
    def __init__(self, name, weights, activation):
        self.name = name
        self.weights = weights
        self.activation = activation
        self.sum = 0
        self.entry = 0
    # the output of the neuron is the activation function applied to the weighted sum of the inputs
    def output(self, entry):
        self.entry = entry
        sum = reduce(lambda a, b : a + b,
                     [self.weights[i] * entry[i] for i in range(0, len(self.weights))])
        self.sum = sum
        return self.activation(sum)


# Let's create a simple neural network and test it    
class NeuralNetwork:
    def __init__(self, layers):
        self.layers = layers

    # the output of the network is the output of the last neuron in the last layer
    def output(self, entry):
        for layer in self.layers:
            new_entry = [1.]            # bias term
            # entry = [neuron.output(entry) for neuron in layer]
            for neuron in layer:
                out = neuron.output(entry)
                new_entry.append(out)
            entry = new_entry
        return out                            # the output of the last neuron in the last layer is the output of the network
    
    # activation function
    def sigmoid(x):
        result = 1 / (1 + exp(-x))
        return result
    
    # activation function
    def relu(x):
        result = max(0, x)
        return result

# Let's create a simple neural network and test it

# Neuron definition
n1_l1 = Neuron("n1_l1", [-4, 10, 10], NeuralNetwork.sigmoid)    # or
n2_l1 = Neuron("n2_l1", [9, -6, -6], NeuralNetwork.sigmoid)     # nand

n1_l2 = Neuron("n1_l2", [-16, 10, 10], NeuralNetwork.sigmoid)    # and

# Layers definitions   
layer1 = [n1_l1, n2_l1]
layer2 = [n1_l2]

# Instance of the network class
nn = NeuralNetwork([layer1, layer2])

# Output visualization
print(nn.output([1, 0, 1]))
print("\n")
print(nn.output([1, 1, 0]))
print("\n")
print(nn.output([1, 0, 0]))
print("\n")
print(nn.output([1, 1, 1]))
# print("\n")
