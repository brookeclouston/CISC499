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
    
    """
    for course in candidate_solution:
        #print(course)
        if course == 'Fitness':
            exit
        else:
            #print(candidate_solution[course],'->',candidate_solution[course]['time'])
            new_hc = candidate_solution[course]['time']
            hc += new_hc
            #print(hc)
    if hc > 100:
        print("neg")
        return 1
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
        if course != "Fitness":
            sections_rooms = [attrs["time"], attrs["room"]]
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
        if course != "Fitness":
            sections_profs = [attrs["time"], attrs["prof"]]
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
    #print("here", config.config_rooms())
    #class_capacities = list(config.config_rooms().values())
    for course, attrs in candidate_solution.items():
        if course != "Fitness":
            print(attrs)
            enrollment = attrs["enrolment"] #enrollment is not included in here??
            room = attrs["room"]
            print("class cap  ", class_capacities)
            print("candidate_sol  ", candidate_solution)
            if enrollment > class_capacities[room]:
                return False
    return True




Candidate_solution =  [
    {'CISC 101': {'time': 3, 'room': 1, 'prof': 'Dr. Hu'}, 
    'CISC 102': {'time': 0, 'room': 4, 'prof': 'Dr. Blostein'}, 
    'CISC 103': {'time': 1, 'room': 0, 'prof': 'Prof. Dove'}, "Fitness": 0
    }, 
    {'CISC 101': {'time': 0, 'room': 0, 'prof': 'Dr. Hu'}, 
    'CISC 102': {'time': 3, 'room': 0, 'prof': 'Dr. Blostein'}, 
    'CISC 103': {'time': 2, 'room': 4, 'prof': 'Prof. Dove'}, "Fitness": 0
    }, 
    {'CISC 101': {'time': 2, 'room': 3, 'prof': 'Dr. Hu'}, 
    'CISC 102': {'time': 3, 'room': 4, 'prof': 'Dr. Blostein'}, 
    'CISC 103': {'time': 0, 'room': 1, 'prof': 'Prof. Dove'}, "Fitness": 0
    }, 
    {'CISC 101': {'time': 0, 'room': 0, 'prof': 'Dr. Hu'}, 
    'CISC 102': {'time': 0, 'room': 0, 'prof': 'Dr. Blostein'}, 
    'CISC 103': {'time': 1, 'room': 2, 'prof': 'Prof. Dove'}, "Fitness": 0
    }, 
    {'CISC 101': {'time': 0, 'room': 1, 'prof': 'Dr. Hu'}, 
    'CISC 102': {'time': 3, 'room': 1, 'prof': 'Dr. Blostein'}, 
    'CISC 103': {'time': 2, 'room': 2, 'prof': 'Prof. Dove'}, "Fitness": 0}
    ]

for candidate in Candidate_solution:
    print()
    print("candidate  ", candidate)
    x = calc_fitness(candidate) 
    print(x)
    print()