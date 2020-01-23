# simple version of the fitness function, for testing other functions
# input is a 'solution', represented as a 1xn array
# the function currently adds the values together and returns the sum
#TODO: Brooke to write

import numpy

def fitness(solution):
    """This function evaluates the fitness of a candidate solution"""
    fitvalue = 0
    for i in range(len(solution)):
        fitvalue += solution[i]
    return fitvalue
