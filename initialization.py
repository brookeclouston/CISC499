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
values: assigned timeslot index, assigned room index, assigned prof index). e.g. for popsize = 5:

[{'CISC101': {'time': 0, 'room': 0, 'prof': 1}, 'CISC102': {'time': 3, 'room': 2, 'prof': 0}, 
    'CISC103': {'time': 2, 'room': 2, 'prof': 1}}, {'CISC101': {'time': 1, 'room': 3, 'prof': 2}, 
    'CISC102': {'time': 3, 'room': 0, 'prof': 2}, 'CISC103': {'time': 2, 'room': 2, 'prof': 0}}, 
    {'CISC101': {'time': 0, 'room': 3, 'prof': 2}, 'CISC102': {'time': 0, 'room': 4, 'prof': 1}, 
    'CISC103': {'time': 3, 'room': 4, 'prof': 0}}, {'CISC101': {'time': 0, 'room': 3, 'prof': 0}, 
    'CISC102': {'time': 3, 'room': 1, 'prof': 1}, 'CISC103': {'time': 1, 'room': 1, 'prof': 2}}, 
    {'CISC101': {'time': 0, 'room': 0, 'prof': 2}, 'CISC102': {'time': 1, 'room': 2, 'prof': 2}, 
    'CISC103': {'time': 0, 'room': 1, 'prof': 1}}]

[1] - Courses.  List of courses. Each course is a dictionary, with keys and values based on config file. E.g.:

[{'Course': 'CISC101', ' Enrolment': '100'}, {'Course': 'CISC102', ' Enrolment': '50'}, {'Course': 'CISC103', ' Enrolment': '100'}]

[2] - Rooms.  List of rooms. Each room is a dictionary, with keys and values based on config file. e.g.:

[{'Room': 'Miller 101', ' Capacity': ' 25'}, {'Room': 'Jeffery 102', ' Capacity': ' 40'}, {'Room': 'Kingston 103', ' Capacity': ' 100'}, 
    {'Room': 'Watson 104', ' Capacity': ' 65'}, {'Room': 'BioSci 105', ' Capacity': ' 15'}]

[3] - Profs.  List of instructors. Each instructor is a dictionary, with keys and values based on config file. e.g.:

[{'Name': 'Dr. Hu'}, {'Name': 'Dr. Blostein'}, {'Name': 'Prof. Dove'}]

[4] - Times.  List of timeslots. Each timeslot is a dictionary, with keys and values based on config file. e.g.:

[{'Name': 'Monday 9am'}, {'Name': 'Monday 11am'}, {'Name': 'Monday 1pm'}, {'Name': 'Monday 3pm'}]

[5] - Prof/Course Links.  Dictionary of prof/course pairings, keys and values based on config file. e.g.:

[{'Prof': 'Dr. Hu', ' Course': ' CISC 101'}, {'Prof': 'Dr. Blostein', ' Course': ' CISC 102'}, {'Prof': 'Prof. Dove', ' Course': ' CISC 103'}]

"""

import numpy
from numpy.random import seed
from numpy.random import randint
import config
import operator

# Remove the comment from the line below to make sure the 'random'
# numbers are generated the same each time by fixing the seed.

# seed(1)


def init(popsize):
    """
    Function: init
    
    Creats inital population: times and rooms assigned randomly, profs read from configuration file

    :param popsize: Size of inital population
    
    :returns:       List containing inital population of candidate solutions in the form of dictionaries.

    """
    courses = config.config_courses()
    rooms = config.config_rooms()
    profs = config.config_profs()
    times = config.config_times()
    profcourses = config.config_profcourselinks()


    population = []
    while popsize != 0:
        candidate = {}
        courses = config.config_courses() # reinitialize
        time_room_slots = []
        roomindex = 0
        # Create list of tuples for each possible time/room slot option.  
        # 3-tuple contains room index, time index, room capacity 
        # e.g. (0,1,75) means room[0], time[1], room capacity = 75.
        for x, val in rooms.items():
            for y in range(len(times)):
                time_room_slots.append((roomindex,y,val['Capacity']))
            roomindex += 1
#        print(time_room_slots)

        # loop through the courses, assign largest first

        for x in range(len(courses)):
            # find the next course to schedule
            this_course = next_to_schedule(courses)
#            timeslot = randint(0, len(times))
#            room = randint(0, len(rooms))
            timeslot = ""
            room = ""
            timeslot, room, del_slot = schedule_it(this_course, courses, time_room_slots)

            time_room_slots.remove((timeslot, room, del_slot))
            prof = ""
            # Find instructor for each course
            for item in profcourses:
                if item['Course'] == this_course:
                    prof = item['Prof']

            candidate[this_course] = {"time": timeslot, "room": room, "prof": prof}
            del courses[this_course]
        candidate["Fitness"] = 0
        population.append(candidate)
        popsize -= 1
    return [population, courses, rooms, profs, times]

def next_to_schedule(course_list):
    return max(course_list, key=lambda v: course_list[v]['Enrolment'])

def schedule_it(course_tbs, course_list, slot_list):
    for slot in slot_list:
        if slot[2] > course_list[course_tbs]['Enrolment']:
            return slot


# UNCOMMENT TO SEE EXAMPLE
"""
solutions = (init(1))

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