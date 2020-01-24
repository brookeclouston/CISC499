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

#seed(1)

"""
Function: create_time_table
Creats inital time table to keep track of profs and time sections.
:param profs:    Number of profs
:param sections: Number of time sections
:returns:        Nested matrix of numberd prof vs time slot
"""
def create_time_table(profs, sections):
    time_table = [[0] * sections for i in range(profs)] 
    counter = 1
    for i, row in enumerate(time_table):
        for j, col in enumerate(row):
            time_table[i][j] = counter
            counter += 1
    return time_table


"""
Function: init
Creats inital population randomly
:param courses:         Number of courses
:param popsize:         Size of inital population
:param time_table_size: Size of inital time table (upper range of possible slot value)
:returns:               List containing inital population of candidate solutions
"""
def init(courses, popsize, time_table_size):
    population = [[0] * courses for i in range(popsize)]
    for i in range(popsize):
        for j in range(courses):
            population[i][j] = randint(1, time_table_size+1)
    return population


