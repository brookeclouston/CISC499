"""
Config file to parse data from csv files
"""
import csv

""" Function: config_courses 
Reads in course names and enrollment numbers from config file
:returns: Dictionary of {course_name(string): enrollemnts(int)}
"""
def config_courses(course_file="data/courses.csv"):
    courses = {}
    with open(course_file, "r") as course:
        csv_reader = csv.reader(course, delimiter=',')
        for row in csv_reader:
            courses[row[0]] = int(row[1])
    return courses

""" Function: config_rooms 
Reads in room names and room capacity from config file
:returns: Dictionary of {room_name(string): room_capacity(int)}
"""
def config_rooms(room_file="data/rooms.csv"):
    rooms = {}
    with open(room_file, "r") as room:
        csv_reader = csv.reader(room, delimiter=',')
        for row in csv_reader:
            rooms[row[0]] = int(row[1])
    return rooms

""" Function: config_profs 
Reads in prof names from config file
:returns: List of profs
"""
def config_profs(prof_file="data/profs.csv"):
    profs = []
    with open(prof_file, "r") as prof:
        csv_reader = csv.reader(prof, delimiter=',')
        for row in csv_reader:
            profs.append(row)
    return profs[0]

""" Function: config_sections 
Reads in section titles from config file
:returns: List of sections
"""
def config_sections(section_file="data/sections.csv"):
    sections = []
    with open(section_file, "r") as section:
        csv_reader = csv.reader(section, delimiter=',')
        for row in csv_reader:
            sections.append(row)
    return sections[0]
