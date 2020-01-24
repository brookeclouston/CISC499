""" Recombination script to be written by Rick"""
# Takes list of solutions (parents), list of fitness scores, and recombination type (clone, ) as input
# Returns list of children
import numpy as np
from numpy.random import seed
from numpy.random import randint

# Remove the comment from the line below to make sure the 'random'
# numbers are generated the same each time by fixing the seed.

# seed(1)

def createchildren(populationcopy, parents, recombtype, maxvalue, fitnesses):
    children = []
    if recombtype == "clone":
        for i in range(len(parents)):
            newchild = populationcopy[parents[i]].copy()
#            print(newchild)
            mutate(newchild, .4, maxvalue)
            children.append(newchild)
#    print("f child: ",children)
    return children

import numpy as np

def mutate(child, mutatechance, maxvalue):
    for i in range(len(child)):
        if np.random.rand() < mutatechance:
#            print("Mutation time!")
            if np.random.rand() < .5:
                if child[i] >= maxvalue:
                    pass
                else:
                    child[i] += 1
            else:
                if child[i] < 1:
                    pass
                else:
                    child[i] -= 1
        else:
            pass
#            print("Not today")
#    print(child)
