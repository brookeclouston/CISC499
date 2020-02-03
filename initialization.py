"""
Initialization script to be written by Rick

This script will create an initial population of candidate timetables.
Each timetable will be represented as an array of values.
Each value will represent a timeslot/room pairing for one of the courses
to be timetabled.
Input values will include the number of courses, number of entries
in the timeslot/room grid, and population size.
Return value will be list of the following:
[0] - Population.  List of candidate solutions.  Each candidate solution is a dict, with key=course name and value=dict (keys: time, room, prof; 
values: assigned timeslot index, assigned room index, assigned prof index).
[1] - Courses.  Dictionary of courses, with keys and values based on config file.
[2] - Rooms.  Dictionary of rooms, with keys and values based on config file.
[3] - Profs.  Dictionary of instructors, with keys and values based on config file.
[4] - Times.  Dictionary of timeslots, with keys and values based on config file.
[5] - Prof/Course Links.  Dictionary of prof/course pairings, keys and values based on config file.
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
    times = config.config_times()
    profcourses = config.config_profcourselinks()
    population = []
    while popsize != 0:
        candidate = {}
        for course in enumerate(x['Course'] for x in courses):
            this_course = course[1]
            timeslot = randint(0, len(times))
            room = randint(0, len(rooms))
            prof = randint(0, len(profs))
            candidate[this_course] = {"time": timeslot, "room": room, "prof": prof}
        population.append(candidate)
        popsize -= 1
    return [population, courses, rooms, profs, times, profcourses]


# UNCOMMENT TO SEE EXAMPLE
"""
solutions = (init(5))
print("Solutions: ",solutions)

for i, solution in enumerate(solutions):
    print()
    if i == 0:
        print(solution)
        for j, candidate in enumerate(solution):
            print("candidate",j,":",candidate)
    else:
        print(solution)
    print()
"""
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
