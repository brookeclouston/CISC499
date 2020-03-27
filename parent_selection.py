"""
Implements multiple types of parent selection 
"""
import constraints 
import numpy
from numpy.random import seed
from numpy.random import randint


def select_parents(num_parents, fitnesses):
    """
    Function: select_parents
    Selects a number of parents using fitness scores.  Reads global variable to determine
    selection type, then calls sub-function. Returns a list of index values
    :param num_parents: Number of parent indexes to return
    :param fitnesses:   Indexed list of fitness values for current population
    :returns:           List containing indexes of selected parents
    """
    parent_list = [0] * num_parents
    if constraints.parent_selection == "random":
        return select_parents_random(num_parents, fitnesses)
    if constraints.parent_selection == "roulette":
        return select_parents_roulette(num_parents, fitnesses)
    if constraints.parent_selection == "rank":
        return select_parents_rank(num_parents, fitnesses)
    for parent in range(num_parents):
        if constraints.parent_selection == "tournament":
            parent_list[parent] = select_parents_tournament(constraints.tournament_y, fitnesses)
    return parent_list


def select_parents_tournament(y_parents, fitnesses):
    """
    Function: select_parents_tournament
    Selects parents based off of a tournament style: A subset of size y_parents is created
    consisting of randomly chosen parents, and the index of the parent with the max fitness
    is returned.
    :param y_parents: Number of parents to use in tournament round
    :param fitnesses: Fitness values of current population
    :returns:         List containing indexes of selected parents
    """
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


def select_parents_random(num_parents, fitnesses):
    """
    Function: select_parents_random
    Selects parents randomly based off of index positions. Does not allow for duplicate parent
    values.
    :param num_parents: Number of parents to randomly choose
    :param fitnesses:   List of fitnesses (used to calculate possible range of solutions)
    :returns:           List of indexes of randomly selected parents
    """
    parents = []
    for i in range(num_parents):
        rand_parent = randint(0, len(fitnesses))
        if rand_parent not in parents:
            parents.append(rand_parent)
            break 
    return parents
    

def select_parents_roulette(num_parents, fitness):
    """
    Function: select_parents_roulette
    Selects parents based on a "roulette-wheel" style: the fitness list is sorted then a random
    integer between 0 and sum(fitnesses) if selected (roulette_value). The fitness list is iterated
    over and each fitness is added to the partial sum counter, while counter < roulette_value. When
    this constraint is violated, the index of the parent that violated it is added to the parent
    sublist. NOTE: this method allows for duplicate parents
    :param num_parents: Number of parents to choose
    :param fitnesses:   List of fitnesses (used to calculate possible range of solutions)
    :returns:           List of indexes of selected parents
    """
    parent_sublist = [] 
    sum_fitnesses = sum(fitness)
    fitness_dict = {}
    for position, value in enumerate(fitness):
        fitness_dict[position] = value
    sorted_fitness = {k: v for k, v in sorted(fitness_dict.items(), key=lambda item: item[1])}
    while len(parent_sublist) < num_parents:
        counter = 0
        roulette_value = randint(0, sum_fitnesses)
        for original_index, fitness in sorted_fitness.items():
            counter += fitness
            if counter < roulette_value:
                continue
            else:
                parent_sublist.append(original_index)
                break
    return parent_sublist


def select_parents_rank(num_parents, fitness):
    """
    Function: select_parents_rank
    Selects parents by ranking them in order of fitness and selecting the top n parents where
    n = number of parents required.
    :param num_parents: Number of parents to choose
    :param fitnesses:   List of fitnesses (used to calculate possible range of solutions)
    :returns:           List of indexes of selected parents
    """
    parent_sublist = [] 
    fitness_dict = {}
    for position, value in enumerate(fitness):
        fitness_dict[position] = value
    sorted_fitness = {k: v for k, v in sorted(fitness_dict.items(), key=lambda item: item[1], reverse=True)}
    sorted_fitness_list = list(sorted_fitness)
    for pair in range(0, num_parents):
        parent_sublist.append(sorted_fitness_list[pair])
    return parent_sublist
