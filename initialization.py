# Initialization script to be written by Rick

# This script will create an initial population of candidate timetables.
# Each timetable will be represented as an array of values.
# Each value will represent a timeslot/room pairing for one of the courses
# to be timetabled.
# Input values will include the number of courses, number of entries
# in the timeslot/room grid, and population size.
# Return value will be a 2d array, with a list of candidate timetables,
# each with a list of course assignments to a time/room slot.

import numpy
from numpy.random import seed
from numpy.random import randint

# Remove the comment from the line below to make sure the 'random'
# numbers are generated the same each time by fixing the seed.

# seed(1)

def init(courses, slots, popsize):
    """This function creates the initial population for GA"""

    population = [[0]*courses for i in range(popsize)]
    for i in range(popsize):
        for j in range(courses):
            population[i][j] = randint(1,slots+1)
    return population

# Print the output for unit testing

print(init(10,100,3))
