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
import config
# Remove the comment from the line below to make sure the 'random'
# numbers are generated the same each time by fixing the seed.

#seed(1)

"""
Function: init
Creats inital population randomly
:param popsize: Size of inital population
:returns:       List containing inital population of candidate solutions in the form of dictionaries
"""
def init(popsize):
    courses = config.config_courses()
    rooms = len(config.config_rooms())
    profs = len(config.config_profs())
    sections = len(config.config_sections())
    population = []
    while popsize != 0:
        candidate = {}
        for course, enrollment in courses.items():
            section = randint(1, sections+1)
            room = randint(1, rooms+1)
            prof = randint(1, profs+1)
            candidate[course] = {"enrollment": enrollment, "section": section, "room": room, "prof": prof}
        population.append([candidate])
        popsize -= 1
    return population

"""
#UNCOMMENT TO SEE EXAMPLE
solutions = (init(5))
print(solutions)
for solution in solutions:
    print()
    for key, value in solution.items():
        print(key, value)
    print()
"""




"""
New method of representation: 
solution = [{"CISC101": {"enrolments":100, "section":1, "room": 1, "prof": 1}}]

lookup tables that are constructed in config.py:
RoomName: ["Miller 101", "Jeffrey 102", "Kingston 103", "Watson 104", "BioSci 105", ...]
RoomCap: [25, 40, 100, 65, 15]
SlotTimes: ["Monday 9am", "Monday 11am", "Monday 1pm", "Monday 3pm", ...]
ProfNames: ["Dr. Hu", "Dr. Blostein", "Prof. Dove"] 
"""
