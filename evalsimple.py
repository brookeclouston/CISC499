# simple version of the fitness function, for testing other functions

import numpy

def fitness(solution):
    """This function evaluates the fitness of a candidate solution"""
    fitvalue = -1
    for i in range(len(solution)):
        fitvalue += solution[i]
    return fitvalue

# print(fitness([0,1,2,3,4,5]))