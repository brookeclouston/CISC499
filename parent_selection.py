import constraints # bring in global variables
import numpy
from numpy.random import seed
from numpy.random import randint

"""
Function: select_parents
Selects a number of parents using fitness scores.  Reads global variable to determine selection type, then calls sub-function
Returns a list of index values
are selected, returns index of parents.
:param num_parents: Number of parent indexes to return
:param fitnesses:   Indexed list of fitness values for current population
:returns:           List containing indexes of selected parents
"""
def select_parents(num_parents, fitnesses):
    parent_list = [0] * num_parents
    for parent in range(num_parents):
        if constraints.parent_selection == 'tournament':
            parent_list[parent] = select_parents_tournament(constraints.tournament_y, fitnesses)
        """
        max = 0
        for j, value in enumerate(fitnesses):
            if value > max:
                max = value
                index = j
        parent_list[parent] = index
        fitnesses[index] = 0
        """
    return parent_list

"""
Function: select_parents_tournament
Selects parents based off of a tournament style where those with the highest fitnes
are selected, returns index of parents.
:param y_parents: Number of parents to use in tournament round
:param fitnesses:   Fitness values of current population
:returns:           List containing indexes of selected parents
"""
def select_parents_tournament(y_parents, fitnesses):
    #print(y_parents)
    parent_sublist = [0] * y_parents
    #print(parent_sublist)
    index = []
    for i in range(y_parents):
        parent_sublist[i] = randint(0,len(fitnesses))
    #print(parent_sublist)
# parent_sublist[] now has randomly selected index values from the master parent list
# loop through these and find the highest fitness
    max = 0
    for j in parent_sublist:
        if fitnesses[j] > max:
            max = fitnesses[j]
            index = j
    return index


#TODO: Brooke implement different versions of parent selection -> random, weighted sum (roulette)