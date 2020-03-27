"""
This script creates an initial population of candidate timetables.
Each timetable will be represented as an array of values.
Each value will represent a timeslot/room pairing for one of the courses
to be timetabled.
Input values will include the number of courses, number of entries in the timeslot/room grid,
 and population size.
Return value will be list of the following:
[0] - Population.  List of candidate solutions.  Each candidate solution is a dict, with
 key=course name and value=dict (keys: time, room, prof; 
values: assigned timeslot index, assigned room index, assigned prof index). e.g. for popsize = 5:
"""
import numpy
from numpy.random import seed
from numpy.random import randint
import config
import operator
from operator import getitem
import random

# Remove the comment from the line below to make sure the 'random'
# numbers are generated the same each time by fixing the seed.

# seed(1)


def init(popsize):
    """
    Function: init
    Creates initial population: times and rooms assigned randomly, profs read from configuration
     file
    :param popsize: Size of initial population
    :returns:       List containing initial population of candidate solutions (dictionary)

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

        # loop through the courses, assign largest first
        for x in range(len(courses)):
            # find the next course to schedule
            this_course = next_tourn_schedule(courses)
            timeslot = ""
            room = ""
            room, timeslot, del_slot = schedule_it(this_course, courses, time_room_slots)
            time_room_slots.remove((room, timeslot, del_slot))
            prof = ""
            # Find instructor for each course
            for item in profcourses:
                if item['Course'] == this_course:
                    prof = item['Prof']

            candidate[this_course] = {"room": room, "time": timeslot, "prof": prof}
            del courses[this_course]
        candidate["Fitness"] = 0
        population.append(candidate)
        popsize -= 1

    return [population, courses, rooms, profs, times]


def next_to_schedule(course_list):
    """
    Function: next_to_schedule
    Takes a list of courses, finds the one with highest enrolment.
    :param course_list: List of courses, each is a dictionary
    :returns:           One course entry from the list.

    """
    return max(course_list, key=lambda v: course_list[v]['Enrolment'])
    

def next_tourn_schedule(course_list):
    """
    Function: next_tourn_schedule
    Variation of next_to_schedule. Takes a list of courses, finds the top X with highest enrolment
    Selects one of the top X at random and returns that as the next course to be scheduled.
    :param course_list: List of courses, each is a dictionary 
    :returns:       One course entry from the list.
    """
    tourn_set = dict(sorted(course_list.items(), key=lambda item: item[1]['Enrolment'])[-5:])
    win_course, enrol = random.choice(list(tourn_set.items()))
    return win_course


def schedule_it(course_tbs, course_list, slot_list):
    """
    Function: schedule_it
    Schedules a single course. Takes a course name (as an index from a list of courses), 
    schedules it to the first available room that has sufficient capacity to meet the course
    enrolment.
    :param course_tbs:  Course 'to be scheduled'. Integer index referring to course_list
    :param course_list: List of courses, each is a dictionary
    :param slot_list:   List of slots which a given course can be scheduled. Each slot is a tuple
    :returns:           A slot from a list of slot options
    """
    for slot in slot_list:
        if slot[2] > course_list[course_tbs]['Enrolment']:
            return slot
