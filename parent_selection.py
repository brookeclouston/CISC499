"""
Function: select_parents_tournament
Selects parents based off of a tournament style where those with the highest fitnes
are selected, returns index of parents.
:param num_parents: Number of parent indexes to return
:param fitnesses:   Fitness values of current population
:returns:           List containing indexes of selected parents
"""
def select_parents_tournament(num_parents, fitnesses):
    parent_list = [0] * num_parents
    for parent in range(num_parents):
        max = 0
        for j, value in enumerate(fitnesses):
            if value > max:
                max = value
                index = j
        parent_list[parent] = index
        fitnesses[index] = 0
    return parent_list


#TODO: Brooke implement different versions of parent selection -> random, weighted sum (roulette)