""" Recombination script to generate children and apply mutation within a Genetic Algorithm.

This module contains two functions, which are used to create and mutate children as part of a Genetic Algorithm (GA).
The first function is called create_children, and it in turn calls the second function, mutate.  Generally an external
module need only call create_children directly.

"""

import numpy as np
from numpy.random import seed
from numpy.random import randint
import constraints
import copy

# Remove the comment from the line below to make sure the 'random'
# numbers are generated the same each time by fixing the seed.
# seed(1)

def create_children(num_rooms, num_times, parents, fitnesses, num_children, populationcopy):
    """Creates children timetable solutions from parent generation.

    Checks a global to see what type of crossover scheme should be used. Current options are:

    clone: Select a parent at random and copy it to the child.  Apply mutation to introduce variance. Repeat until num_children
        children have been created

    Future options may include:

    single-point: pairs of parents are selected at random to create children.  A random number X is selected between 1 and the number of courses N
        in each solution.  The first (1-X) set of courses are taken from parent A, then the second (X-N) set are taken from parent B.
    double-point: as single point, but two random numbers are selected, X and Y.  1-X courses from parent A, X-Y from parent B, then Y-N from parent A
    random: for each course within the solution, a 50% chance of it being selected from parent A vs B

    Args:
        num_rooms: An integer representing the number of rooms available for scheduling. Used by mutate.
        num_times: An integer representing the number of timeslots available for scheduling. Used by mutate.
        parents: A list of integers, representing the index values within populationcopy, that have been selected as parents.
        fitnesses: A list of integers, representing the fitness values of each candidate solution within populationcopy.
        num_children: An integer representing the number of children that should be returned.
        populationcopy: A complex data structure of nested lists and dictionaries, representing all candidate solutions within
            the current generation.

    Returns:
        A list of children solutions, created from parents.  Each child is represented by a dictionary with keys that are course
        names, and values that are another dictionary.  Within the nested dictionary, keys are time, room, and prof.  For
        example, a single solution may look like this:

        {'CISC101': {'time': 1, 'room': 1, 'prof': 1}, 'CISC102': {'time': 0, 'room': 4, 'prof': 1}, 'CISC103': {'time': 3, 'room': 0, 'prof': 2}}
        
        And a list of three children could therefore look like:

        [{'CISC101': {'time': 1, 'room': 1, 'prof': 1}, 'CISC102': {'time': 0, 'room': 4, 'prof': 1}, 'CISC103': {'time': 3, 'room': 0, 'prof': 3}}, 
        {'CISC101': {'time': 0, 'room': 2, 'prof': 1}, 'CISC102': {'time': 0, 'room': 1, 'prof': 2}, 'CISC103': {'time': 0, 'room': 0, 'prof': 2}}, 
        {'CISC101': {'time': 2, 'room': 1, 'prof': 3}, 'CISC102': {'time': 0, 'room': 2, 'prof': 1}, 'CISC103': {'time': 3, 'room': 2, 'prof': 2}}]

        If there is a "Fitness" key within the parent, it is returned as well.  For example a single child could also look like this:

        {'CISC101': {'time': 1, 'room': 1, 'prof': 1}, 'CISC102': {'time': 0, 'room': 4, 'prof': 1}, 
            'CISC103': {'time': 3, 'room': 0, 'prof': 2}, 'Fitness': 95}        

    """
    children = []
    for j in range(num_children):
        if constraints.recombtype == "clone":
            # clone simply selects a parent at random, and returns a copy of that parent as a child
            parent_key = randint(0,len(parents))
            newpop = populationcopy[:]
            #print("new pop", newpop)
            #print("parents", parents)
            #print("parent key", parent_key)
            #PROBLEM HERE parents is an empty list so it can not be used to index newpop
            newchild = newpop[parents[parent_key]].copy()
            #print("new child:",newchild)

            # now mutate the child to introduce random variance in the subsequent population
            mutechild = mutate(newchild, num_rooms, num_times, constraints.mutate_chance)
            #print("after mutation:",mutechild)            
            children.append(mutechild)
            #print("Child",j,children)

    return children


def mutate(child_param, num_rooms, num_times, mutatechance):
    """Mutates a given timetable solutions, to introduce variance within a Genetic Algorithm.

    Applies a mutation scheme.

    Args:
        child_param: A candidate solution for a timetable. This is often a child created within this module, but not necessarily.
        num_rooms: An integer representing the number of rooms available for scheduling. Ensures the mutation does not return an invalid value.
        num_times: An integer representing the number of timeslots available for scheduling. Ensures the mutation does not return an invalid value.
        mutatechance: A float representing the percentage chance that a given 'gene' (course) will be mutated.

    Returns:
        A single children solutions, created as a result of mutation calculations.  Each child is represented by a dictionary with 
        keys that are course names, and values that are another dictionary.  Within the nested dictionary, keys are time, room, and 
        prof. For example, a single solution may look like this:

        {'CISC101': {'time': 1, 'room': 1, 'prof': 1}, 'CISC102': {'time': 0, 'room': 4, 'prof': 1}, 'CISC103': {'time': 3, 'room': 0, 'prof': 2}}

        If there is a "Fitness" key within the solution provided, it is not mutated and returned as well.  For example a returned 
        solution could also look like this:

        {'CISC101': {'time': 1, 'room': 1, 'prof': 1}, 'CISC102': {'time': 0, 'room': 4, 'prof': 1}, 
            'CISC103': {'time': 3, 'room': 0, 'prof': 2}, 'Fitness': 95}        

    """
    child = copy.deepcopy(child_param)
    for course in child:
        # This makes sure we ignore the Fitness key within a solution, as it is calculated from other values
        if course == 'Fitness':
            exit
        else:
            # Apply room mutation
            if np.random.rand() < mutatechance:
                # 50% chance of mutation going up or down.  If max/min value is already reached, do nothing
                if np.random.rand() < .5:
                    if child[course]['room'] >= num_rooms-1:
                        pass
                    else:
                        child[course]['room'] += 1
                else:
                    if child[course]['room'] < 1:
                        pass
                    else:
                        child[course]['room'] -= 1
            else:
                pass
            # Apply time mutation
            if np.random.rand() < mutatechance:
                # 50% chance of mutation going up or down.  If max/min value is already reached, do nothing
                if np.random.rand() < .5:
                    if child[course]['time'] >= num_times-1:
                        pass
                    else:
                        child[course]['time'] += 1
                else:
                    if child[course]['time'] < 1:
                        pass
                    else:
                        child[course]['time'] -= 1
            else:
                pass
    return child
