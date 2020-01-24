"""
hard constarints 
- no conflicts between classes
"""



"""
Function: basic_fitness
Calculates a basic fitness value for a candidate solution based on 100 - number of conflicts
:param candidate_solution: Proposed soltion to calculate fitness for
:param time_table:         Existing time table (not currently used, but could be interesting to play with)
:returns:                  Integer representing computed fitness
"""
def basic_fitness(candidate_solution, time_table):
    duplicates = set([x for x in candidate_solution if candidate_solution.count(x) > 1])
    return 100 - len(duplicates)

