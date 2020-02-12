import constraints # bring in global variables
import numpy
from numpy.random import seed
from numpy.random import randint

"""
Function: select_parents
Selects a number of parents using fitness scores.  Reads global variable to determine selection type,
then calls sub-function. Returns a list of index values
:param num_parents: Number of parent indexes to return
:param fitnesses:   Indexed list of fitness values for current population
:returns:           List containing indexes of selected parents
"""
def select_parents(num_parents, fitnesses):
    parent_list = [0] * num_parents
    if constraints.parent_selection == "random":
        return select_parents_random(num_parents, fitnesses)
    for parent in range(num_parents):
        if constraints.parent_selection == "tournament":
            parent_list[parent] = select_parents_tournament(constraints.tournament_y, fitnesses)
    return parent_list

"""
Function: select_parents_tournament
Selects parents based off of a tournament style: A subset of size y_parents is created consisting of
randomly chosen parents, and the index of the parent with the max fitness is returned.
:param y_parents: Number of parents to use in tournament round
:param fitnesses: Fitness values of current population
:returns:         List containing indexes of selected parents
"""
def select_parents_tournament(y_parents, fitnesses):
    parent_sublist = [0] * y_parents
    index = 0
    for i in range(y_parents):
        parent_sublist[i] = randint(0,len(fitnesses))
    max = 0
    for j in parent_sublist:
        if fitnesses[j] > max:
            max = fitnesses[j]
            index = j
    return index


"""
Function: select_parents_random
Selects parents randomly based off of index positions. Does not allow for duplicate parent values.
:param num_parents: Number of parents to randomly choose
:param fitnesses:   List of fitnesses (used to calculate possible range of solutions)
:returns:           List of indexes of randomly selected parents
"""
def select_parents_random(num_parents, fitnesses):
    parents = []
    for i in range(num_parents):
        rand_parent = randint(0, len(fitnesses))
        if rand_parent not in parents:
            parents.append(rand_parent)
            break 
    return parents
    
    

#TODO: Brooke implement different versions of parent selection -> random, weighted sum (roulette)