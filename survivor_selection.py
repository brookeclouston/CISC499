"""
Selects the surviors based off of the fitnesses of the functions, want the fitness to
be 0 so the fitness function is sorted in descending order 
:param retiree: number of retirees to removed from fitness functions
:param fitnesses: list of fitnesses 
"""
def select_survivor(retirees, fitnesses):
    to_retire = []
    sorted_fitnesses = sorted(fitnesses, reverse=True)
    for retiree in range(retirees):
        retire_index = fitnesses.index(sorted_fitnesses[retiree])
        if retire_index not in to_retire:
            to_retire.append(retire_index)
        else: 
            retiree += 1
            retire_index = fitnesses.index(sorted_fitnesses[retiree])
            to_retire.append(retire_index)
            # fixme need to make this better
    return to_retire