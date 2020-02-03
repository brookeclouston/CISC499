"""
Config file to parse data from csv files
"""
import csv



def config_courses(course_file="data/courses.csv"):
    """ Function: config_courses 
    Reads in courses and attributes (name, enrollment, etc.) from config file
    :returns: List of dictionaries.  Each list item is a course, and each dictionary includes key/value pair attributes from config file
    """
    reader = csv.DictReader(open(course_file))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    return dict_list


def config_rooms(room_file="data/rooms.csv"):
    """ Function: config_rooms 
    Reads in rooms and attributes (name, room capacity, etc.) from config file
    :returns: List of dictionaries.  Each list item is a room, and each dictionary includes key/value pair attributes from config file
    """
    return config_courses(room_file)

def config_profs(prof_file="data/profs.csv"):
    """ Function: config_profs 
    Reads in instructors and attributes (name, etc.) from config file
    :returns: List of dictionaries.  Each list item is a prof, and each dictionary includes key/value pair attributes from config file
    """
    return config_courses(prof_file)

def config_times(time_file="data/sections.csv"):
    """ Function: config_times 
    Reads in time slots and attributes (name, etc.) from config file
    :returns: List of dictionaries.  Each list item is a time slot, and each dictionary includes key/value pair attributes from config file
    """
    return config_courses(time_file)

def config_profcourselinks(profcourse_file="data/profcourse.csv"):
    """ Function: config_profcourselinks 
    Reads in instructor/course pairings config file
    :returns: List of dictionaries.  Each list item is a prof/course combination, represented as a dictionary with keys Prof and Course 
    """
    return config_courses(profcourse_file)