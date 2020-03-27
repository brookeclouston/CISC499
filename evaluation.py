"""
This module contains the hard and soft constraints to check a candidate solution and return
a fitness value for it. 
"""
import config


def calc_fitness(candidate_solution):
    """
    Function: calc_fitness
    Calculates a fitness value for a candidate solution based on number of conflicts
    :param candidate_solution: Proposed solution to calculate fitness for
    :returns:                  Integer representing computed fitness where perfect solution is 100
    """
    fitness = 100
    hc = hard_constraints(candidate_solution)
    sc = soft_constraints(candidate_solution)

    return [max(fitness - hc - sc,1),sc]


def hard_constraints(candidate_solution):
    """
    Function: hard_constraints
    Checks a candidate solution for hard constraints, returns the number violated. Hard constraints
    include room capacity conflicts, room schedule conflicts and prof conflicts.
    :param candidate_solution: Proposed solution to calculate fitness for
    :returns:                  A cumulative sum of hard constraints that were violated, otherwise 0. 
    """
    hc = 0
    hc += check_rooms(candidate_solution)
    hc += check_profs(candidate_solution)
    hc += check_capacity(candidate_solution)
    return hc


def soft_constraints(candidate_solution):
    """
    Function: soft_constraints
    Checks a candidate solution for soft constraints, returns the number violated.
    :param candidate_solution: Proposed solution to calculate fitness for
    :returns:                  A cumulative sum of soft constraints that were violated, otherwise 0. 
    """
    sc = 0
    sc += check_prof_back_to_back(candidate_solution)
    sc += check_course_back_to_back(candidate_solution)
    sc += check_course_years(candidate_solution)
    return sc 


def check_rooms(candidate_solution):
    """ 
    Function: check_rooms
    Checks to make sure there are no duplicate room and section times (ie. no two classes are
    scheduled in the same room at the same time).
    :param candidate_solution: Proposed solution to check rooms and sections
    :returns:                  Number of conflicts found
    """
    rooms = []
    returnval = 0
    for course, attrs in candidate_solution.items():
        if course != "Fitness":
            sections_rooms = [attrs["time"], attrs["room"]]
            if sections_rooms in rooms:
                returnval += 5
            rooms.append(sections_rooms)
    return returnval


def check_profs(candidate_solution):
    """ 
    Function: check_profs
    Checks to make sure there are no duplicate prof and section times (ie. no prof can 
    be in two places at once).
    :param candidate_solution: Proposed solution to check profs and sections
    :returns:                  Number of conflicts found
    """
    profs = []
    returnval = 0
    for course, attrs in candidate_solution.items():
        if course != "Fitness":
            sections_profs = [attrs["time"], attrs["prof"]]
            if sections_profs in profs:
                returnval += 5
            profs.append(sections_profs)           
    return returnval


def check_capacity(candidate_solution):
    """ 
    Function: check_capacity
    Checks to make sure there a classes enrollment can fit in the selected room.
    :param candidate_solution: Proposed solution to check enrollment and room capacity for
    :returns:                  Number of conflicts found
    """
    room_capacities = list(config.config_rooms().values())
    enrolments = config.config_courses()
    returnval = 0
    for course, attrs in candidate_solution.items():
        if course != "Fitness":
            class_enrolment = enrolments[course]["Enrolment"] 
            room = attrs["room"]
            room_cap = room_capacities[room]["Capacity"]
            if class_enrolment > room_cap:
                returnval += 5
    return returnval


def check_prof_back_to_back(candidate_solution):
    """ 
    Function: check_prof_back_to_back
    Checks soft constraint of a prof having to teach a class back to back 
    :param candidate_solution: Proposed solution to check enrollment and room capacity for
    :returns:                  Number of conflicts found
    """
    returnval = 0
    prof_dict = {}
    for course, data in candidate_solution.items():
        if course == "Fitness":
            continue
        if data["prof"] not in prof_dict.keys():
            prof_dict[data["prof"]] = [int(data["time"])]
        else:
            prof_dict[data["prof"]].append(int(data["time"]))
        sc = 0
        for time1 in prof_dict[data["prof"]]:
            for time2 in prof_dict[data["prof"]]:
                if time1 != time2:
                    if ((time1 + 1) == time2) or ((time1 - 1) == time2):
                        sc += 1
        returnval += (sc//2)
    return returnval


def check_course_back_to_back(candidate_solution):
    """ 
    Function: check_course_back_to_back
    Checks soft constraint of consecutive courses being scheduled back to back 
    :param candidate_solution: Proposed solution to check enrollment and room capacity for
    :returns:                  Number of conflicts found
    """
    returnval = 0
    for course1, data1 in candidate_solution.items():
        if course1 != "Fitness":
            for course2, data2 in candidate_solution.items():
                if course2 != "Fitness":
                    if (course1[0:4] == course2[0:4]) and (course1 != course2):
                        if ((int(course1[5:8]) + 1) == int(course2[5:8])) or \
                           ((int(course1[5:8]) - 1) == int(course2[5:8])):
                            if ((int(data1["time"]) + 1) == int(data2["time"])) or \
                               ((int(data1["time"]) - 1) == int(data2["time"])):
                                returnval += 1
    return (returnval//2)


def check_course_years(candidate_solution):
    """ 
    Function: check_course_years
    Checks soft constraint of courses of the same year scheduled back to back.
    :param candidate_solution: Proposed solution to check enrollment and room capacity for
    :returns:                  Number of conflicts found
    """
    returnval = 0
    course_dict = {}
    for course, data in candidate_solution.items():
        if course == "Fitness":
            continue
        if course[0:6] not in course_dict.keys():
            course_dict[course[0:6]] = [int(data["time"])]
        else:
            if int(data["time"]) in course_dict[course[0:6]]:
                returnval += 1
            course_dict[course[0:6]].append(int(data["time"]))
    return returnval

