""" 
Recombination script to generate children and apply mutation within a Genetic Algorithm.
"""

import numpy as np
from numpy.random import seed
from numpy.random import randint
import constraints
import copy
import evaluation
import collections
import config

# Remove the comment from the line below to make sure the 'random'
# numbers are generated the same each time by fixing the seed.
# seed(1)

def create_children(num_rooms, num_times, parents, fitnesses, num_children, populationcopy):
    """Function: create_children
    Creates children timetable solutions from parent generation. Checks a global to see what type
    of crossover scheme should be used. Current options are:
    clone: Select a parent at random and copy it to the child.  Apply mutation to introduce
           variance. Repeat until num_children children have been created
    :param: num_rooms:      Number of rooms available for scheduling. Used by mutate
    :param: num_times:      Number of timeslots available for scheduling. Used by mutate.
    :param: parents:        Index values within populationcopy, that have been selected as parents.
    :param: fitnesses:      Fitness values of each candidate solution within populationcopy.
    :param: num_children:   Number of children that should be returned.
    :param: populationcopy: All candidate solutions within current generation.
    return:                 List of children solutions, created from parents.  Each child is
                            represented by a dictionary with keys that are course names, and
                            values that are another dictionary.  Within the nested dictionary, keys
                            are time, room, and prof.  
    """
    children = []
    for j in range(num_children):
        if constraints.recombtype == "clone":
            # Clone selects a parent at random, and returns a copy of that parent as a child
            parent_key = randint(0,len(parents))
            newpop = populationcopy[:]
            newchild = newpop[parents[parent_key]].copy()     
            # Mutates the child to introduce random variance in the subsequent population
            mutechild = mutate(newchild, num_rooms, num_times, constraints.mutate_chance)            
            children.append(mutechild)
       
        elif constraints.recombtype == "crossover":
            # Selects two parents at random. counts the number of 'genes' N in the first parent
            # then a random integer X(1..N) to use as a splitpoint.  Genes (courses) 1..X are
            # taken from parent A, while genes X+1..N are taken from parent B
            parent_a_key = 0
            parent_b_key = 1
            while (parent_a_key != parent_b_key):
                parent_a_key = randint(0,len(parents))
                parent_b_key = randint(0,len(parents))
            
            # Create slice of population and copies of the two new parents 
            newpop = populationcopy[:]
            parent_a = newpop[parents[parent_a_key]].copy()
            parent_b = newpop[parents[parent_b_key]].copy()
            # reinitialize list of courses
            courses = config.config_courses()

            # Initialize dictionary for new child. For each course in the list of courses, select
            # the value at random from one of the parents.  This conveniently handles parents who
            # list courses in different order (python dictionaries are inherently unordered)
            newchild = {}
            for x in courses:
                if np.random.rand() < .5:
                    newchild[x] = parent_a[x]
                else:
                    newchild[x] = parent_b[x]

            # Evaluate fitness for the new child timetable
            new_fitness = evaluation.calc_fitness(newchild)[0]
            newchild['Fitness'] = new_fitness
            
            # Mutate the child to introduce random variance in the subsequent population,
            # then calculate the fitness after mutation
            mutechild = mutate(newchild, num_rooms, num_times, constraints.mutate_chance)
            mute_fitness = evaluation.calc_fitness(mutechild)[0]
            mutechild['Fitness'] = mute_fitness     
            children.append(mutechild)

    return children


def mutate(child_param, num_rooms, num_times, mutatechance):
    """
    Function: mutate
    Mutates a given timetable solutions, to introduce variance within a Genetic Algorithm.
    Applies a mutation scheme. For each course in the timetable, the mutation chance is applied
    to both the room and time.  If mutation is indicated, there is a 50% chance of the index in
    question (room or time) going up or down. This will not cause the index to exceed the minimum
    and maximum allowable values.
    :param: child_param:  Candidate solution, often a child created within this module
    :param: num_rooms:    Number of rooms available for scheduling
    :param: num_times:    Number of timeslots available for scheduling. 
    :param: mutatechance: Percentage chance that a given 'gene' (course) will be mutated.
    :return:              Single children solutions, created as a result of mutation calculations.
                          Each child is represented by a dictionary with keys that are course names, and
                          values that are another dictionary.  Within the nested dictionary, keys are
                          time, room, and prof. 
    """
    child = copy.deepcopy(child_param)
    for course in child:
        # This makes sure we ignore the Fitness key within a solution, as it is calculated and
        #  should not be mutated
        if course == 'Fitness':
            exit
        else:
            # Apply room mutation
            if np.random.rand() < mutatechance:
                # 50% chance of mutation going up or down.  If max/min value is already reached,
                # do nothing
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
