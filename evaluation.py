import config

"""
Function: calc_fitness
Calculates a fitness value for a candidate solution based on number of conflicts
:param candidate_solution: Proposed solution to calculate fitness for
:returns:                  Integer representing computed fitness where perfect solution is 100
"""
def calc_fitness(candidate_solution):
    fitness = 100
    hc = hard_constraints(candidate_solution)
    sc = 0
    return fitness - hc - sc

"""
Function: hard_constraints
Checks a candidate solution for hard constraints, returns 100 if any are violated. Hard constraints
include room capacity conflicts, room schedule conflicts and prof conflicts.
:param candidate_solution: Proposed solution to calculate fitness for
:returns:                  A cumulative sum of hard constraints that were violated, otherwise 0.
FIXME: currently every hard constraint that has been violated counts as 5 "points" - this should
change in the future. 
"""
def hard_constraints(candidate_solution):
    hc = 0
    hc += check_rooms(candidate_solution)
    hc += check_profs(candidate_solution)
    hc += check_capacity(candidate_solution)
    return hc

""" 
Function: check_rooms
Checks to make sure there are no duplicate room and section times (ie. no two classes are
scheduled in the same room at the same time).
:param candidate_solution: Proposed solution to check rooms and sections
:returns:                  False if conflict found, True otherwise
"""
def check_rooms(candidate_solution):
    rooms = []
    returnval = 0
    for course, attrs in candidate_solution.items():
        if course != "Fitness":
            sections_rooms = [attrs["time"], attrs["room"]]
            if sections_rooms in rooms:
                #print("room conflict for",course)
                returnval += 1
            rooms.append(sections_rooms)
    #print("total room conflicts:",returnval)
    return returnval

""" 
Function: check_profs
Checks to make sure there are no duplicate prof and section times (ie. no prof can 
be in two places at once).
:param candidate_solution: Proposed solution to check profs and sections
:returns:                  False if conflict found, True otherwise
"""
def check_profs(candidate_solution):
    profs = []
    returnval = 0
    for course, attrs in candidate_solution.items():
        if course != "Fitness":
            sections_profs = [attrs["time"], attrs["prof"]]
            if sections_profs in profs:
                #print("prof conflict for",course)
                returnval += 1
            profs.append(sections_profs)
    #print("total prof conflicts:",returnval)            
    return returnval

""" 
Function: check_capacity
Checks to make sure there a classes enrollment can fit in the selected room.
:param candidate_solution: Proposed solution to check enrollment and room capacity for
:returns:                  False if conflict found, True otherwise
"""
def check_capacity(candidate_solution):
    room_capacities = list(config.config_rooms().values())
    enrolments = config.config_courses()
    returnval = 0
    for course, attrs in candidate_solution.items():
        if course != "Fitness":
            class_enrolment = enrolments[course]["Enrolment"] 
            room = attrs["room"]
            room_cap = room_capacities[room]["Capacity"]
            if class_enrolment > room_cap:
                #print("room capacity exceeded for", course)
                returnval += 1
    #print("total capacity conflicts:",returnval)
    return returnval
