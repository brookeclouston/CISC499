import config

"""
Function: calc_fitness
Calculates a fitness value for a candidate solution based on number of conflicts
:param candidate_solution: Proposed solution to calculate fitness for
:returns:                  Integer representing computed fitness where perfect solution is 100
"""
def calc_fitness(candidate_solution):
    fitness = 100
    hc = hard_constraints(candidate_solution[0])
    sc = 0
    return fitness - hc - sc

"""
Function: hard_constraints
Checks a candidate solution for hard constraints, returns 100 if any are violated. Hard constraints
include room capacity conflicts, room schedule conflicts and prof conflicts.
:param candidate_solution: Proposed solution to calculate fitness for
:returns:                  100 if any hard constraint was violated, otherwise 0
"""
def hard_constraints(candidate_solution):
    if not check_rooms(candidate_solution):
        return 100
    if not check_profs(candidate_solution):
        return 100
    if not check_capacity(candidate_solution):
        return 100
    return 0

""" 
Function: check_rooms
Checks to make sure there are no duplicate room and section times (ie. no two classes are
scheduled in the same room at the same time).
:param candidate_solution: Proposed solution to check rooms and sections
:returns:                  False if conflict found, True otherwise
"""
def check_rooms(candidate_solution):
    rooms = []
    for course, attrs in candidate_solution.items():
        sections_rooms = [attrs["section"], attrs["room"]]
        if sections_rooms in rooms:
            return False
        rooms.append(sections_rooms)
    return True

""" 
Function: check_profs
Checks to make sure there are no duplicate prof and section times (ie. no prof can 
be in two places at once).
:param candidate_solution: Proposed solution to check profs and sections
:returns:                  False if conflict found, True otherwise
"""
def check_profs(candidate_solution):
    profs = []
    for course, attrs in candidate_solution.items():
        sections_profs = [attrs["section"], attrs["prof"]]
        if sections_profs in profs:
            return False
        profs.append(sections_profs)
    return True

""" 
Function: check_capacity
Checks to make sure there a classes enrollment can fit in the selected room.
:param candidate_solution: Proposed solution to check enrollment and room capacity for
:returns:                  False if conflict found, True otherwise
"""
def check_capacity(candidate_solution):
    class_capacities = list(config.config_rooms().values())
    for course, attrs in candidate_solution.items():
        enrollment = attrs["enrollment"]
        room = attrs["room"]
        print("class cap  ", class_capacities)
        print("candidate_sol  ", candidate_solution)
        if enrollment > class_capacities[room]:
            return False
    return True
