""" Recombination script to be written by Rick
Takes parameters:
populationcopy - copy of the entire population for this gen
num_rooms - the number of rooms available
num_times - the number of timeslots available
parents - an list of parent indexes that have been selected previously for recombination
fitnesses - an indexed list of fitness scores for every solution within the population
num_children - a number of children to be returned

Returns a list of children.  Each child takes the form of a dictionary, with the same keys as the parent and same or different values
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
    children = []
    for j in range(num_children):
        if constraints.recombtype == "clone":
            # clone simply selects a parent at random, and returns a copy of that parent as a child
            parent_key = randint(0,len(parents))
            #print(parent_key)
            newpop = populationcopy[:]
            #print("population copy",populationcopy)
            #print("newpop",newpop)
            newchild = newpop[parents[parent_key]].copy()
            print("new child:",newchild)
            # now mutate the child to introduce random variance in the subsequent population

            mutechild = mutate(newchild, num_rooms, num_times, constraints.mutate_chance)
            print("after mutation:",mutechild)            
            children.append(mutechild)
            print("Child",j,children)

    return children

import numpy as np

def mutate(child_param, num_rooms, num_times, mutatechance):
    """
    Takes a child solution (dict of dicts), number of rooms, number of times, and chance for mutation
    """
    #print(child_param)
    child = copy.deepcopy(child_param)
    for course in child:
        if course == 'Fitness':
            exit
        #print(course, '->',child[course])
        #print("Room:",child[course]['room'])
        #print("Time:",child[course]['time'])
# Room mutation?
        else:
            if np.random.rand() < mutatechance:
                #print("Room mutation time!")
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
                #print("No room change")
# Time mutation?
            if np.random.rand() < mutatechance:
                #print("Time mutation time!")
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
                #print("No time change")
    #print("new child (mut):",child)
    return child
