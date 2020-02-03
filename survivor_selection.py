""" Survivor selection script to identify the lowest fitness scores within a population and return the corresponding index values.

This module contains a simple function 'cull', which is used to find the lowest fitness scores as part of a Genetic Algorithm (GA).
There are other more advanced methods of implementing selective pressure, which may be implemented later.


"""

def cull(num_retirees, fitnesses):
    """
    Function: cull
    Selects which candidates to retiree based on their fitness. The first n candidates with the
    lowest fitnesses are selected as candidates to be removed, list of their indexes returned.
    
    :param num_retirees: Number of candidates to "retire"
    :param fitnesses:    List of current population fitnesses 
    :returns:            List of indexes of candidates to retire 
    """
    retiree_list = [0] * num_retirees
    for retiree in range(num_retirees):
        min = 99999
        for j, value in enumerate(fitnesses):
            if value < min:
                min = value
                index = j
        retiree_list[retiree] = index
        fitnesses[index] = 99999
    return retiree_list
