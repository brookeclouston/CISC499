"""
Initialization script to be written by Rick

This script will create an initial population of candidate timetables.
Each timetable will be represented as an array of values.
Each value will represent a timeslot/room pairing for one of the courses
to be timetabled.
Input values will include the number of courses, number of entries
in the timeslot/room grid, and population size.
Return value will be list of the following:
[0] - Population.  List of courses.  Each course is dict, with key=name and value=dict (keys: enrolment, time, room, prof; 
values: enrolment, assigned timeslot index, assigned room name, prof index).
[1] - Courses.  Dict of courses, with key=name and value=enrolment.
[2] - Rooms.  Dict of rooms, with key=name and value=capacity.
[3] - Profs.  List of instructors.
[4] - Times.  List of timeslots 
"""

import numpy
from numpy.random import seed
from numpy.random import randint
import config

# Remove the comment from the line below to make sure the 'random'
# numbers are generated the same each time by fixing the seed.

# seed(1)

"""
Function: init
Creats inital population randomly
:param popsize: Size of inital population
:returns:       List containing inital population of candidate solutions in the form of dictionaries
"""
def init(popsize):
    courses = config.config_courses()
    rooms = config.config_rooms()
    profs = config.config_profs()
    times = config.config_sections()
    population = []
    while popsize != 0:
        candidate = {}
        for course, enrollment in courses.items():
            timeslot = randint(0, len(times))
            room = randint(0, len(rooms))
            prof = randint(0, len(profs))
            candidate[course] = {"enrollment": enrollment, "time": timeslot, "room": room, "prof": prof}
        population.append(candidate)
        popsize -= 1
    return [population, courses, rooms, profs, times]


# UNCOMMENT TO SEE EXAMPLE
solutions = (init(5))
print(solutions)

for solution in solutions:
    print()
    print(solution)
    print()
"""
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
