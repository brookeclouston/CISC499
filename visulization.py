"""
This script handles the visualization for the algorithm using Jinja templating and an HTML
webpage to continuously update visulization.
"""
import webbrowser
import os
import config
import sys
from jinja2 import Environment, FileSystemLoader


file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"

class Visulization:
    def __init__(self, solution):
        self.candidate_solution = solution
        self.template = env.get_template('table_template.txt')
        self.filepath = "file://" + os.path.realpath("schedule.html")
        self.generation = "0"
        self.times = config.config_times()
        self.classrooms = config.config_rooms()
        self.render_temp()
        
        if sys.platform[:3] == "win":
            webbrowser.register('mychrome', None, webbrowser.BackgroundBrowser(browser_path))
        elif sys.platform == 'darwin':
            webbrowser.register('mychrome', None, webbrowser.MacOSXOSAScript('Google Chrome'), -1) # NOTE: might be different on msft
        webbrowser.get('mychrome').open(self.filepath)
        
    def render_temp(self):
        """
        Function: render_temp
        Renders the template using Jinja2 templates
        """
        if self.candidate_solution != "":
            clean = self.format_data()
            output = self.template.render(GENERATION=self.generation, FILEPATH=self.filepath, 
                                        TIMES=self.times, CLASSROOMS=self.classrooms, DATA=clean)
            f = open('schedule.html','w')
            f.write(output)
            f.close()

    def format_data(self):
        """
        Function: format_data
        Formats the data to be easily loaded into the template.
        :return: Data that has been "cleaned" 
        """
        clean = []
        for x in range(len(self.classrooms)):
            new = []
            for y in range(len(self.times)):
                new.append({"warning": "","error": "", "class": "", "prof": "",
                            "room": list(self.classrooms.keys())[x], 
                            "time": self.times[y]["Name"]})
            clean.append(new)
        clean = self.check_rooms(clean)
        clean = self.check_profs(clean)
        clean = self.check_capacity(clean)
        clean = self.check_prof_back_to_back(clean)
        clean = self.check_course_back_to_back(clean)
        clean = self.check_course_years(clean)
        return clean

    def check_rooms(self, clean):
        """
        Function: check_rooms
        Checks for constraint violations in rooms and returns data reflecting conflict status.
        """
        rooms = []
        for course, attrs in self.candidate_solution.items():
            if course != "Fitness":
                sections_rooms = [attrs["time"], attrs["room"]]
                if sections_rooms in rooms:
                    # Conflict found                                    
                    clean[attrs["room"]][attrs["time"]]["error"] = "ERROR"
                else:
                    clean[attrs["room"]][attrs["time"]]["class"] = course
                rooms.append(sections_rooms)
        return clean

    def check_profs(self, clean):
        """
        Function: check_profs
        Checks for constraint violations in profs and returns data reflecting conflict status.
        """
        profs = []
        for course, attrs in self.candidate_solution.items():
            if course != "Fitness":
                sections_profs = [attrs["time"], attrs["prof"]]
                if sections_profs in profs:
                    clean[attrs["room"]][attrs["time"]]["error"] = "ERROR"
                else:
                    clean[attrs["room"]][attrs["time"]]["prof"] = attrs["prof"]
            profs.append(sections_profs)           
        return clean
    
    def check_capacity(self, clean):
        """
        Function: check_capacity
        Checks for constraint violations in rooms and returns data reflecting conflict status.
        """
        room_capacities = list(config.config_rooms().values())
        enrolments = config.config_courses()
        for course, attrs in self.candidate_solution.items():
            if course != "Fitness":
                class_enrolment = enrolments[course]["Enrolment"] 
                room = attrs["room"]
                room_cap = room_capacities[room]["Capacity"]
                if class_enrolment > room_cap:
                    clean[attrs["room"]][attrs["time"]]["error"] = "ERROR"
        return clean

    def check_prof_back_to_back(self, clean):
        """
        Function: check_prof_back_to_back
        Checks for constraint violations in profs and returns data reflecting conflict status.
        """
        prof_dict = {}
        for course, data in self.candidate_solution.items():
            if course == "Fitness":
                continue
            if data["prof"] not in prof_dict.keys():
                prof_dict[data["prof"]] = [int(data["time"])]
            else:
                prof_dict[data["prof"]].append(int(data["time"]))
            for time1 in prof_dict[data["prof"]]:
                for time2 in prof_dict[data["prof"]]:
                    if time1 != time2:
                        if ((time1 + 1) == time2) or ((time1 - 1) == time2):
                            clean[data["room"]][data["time"]]["warning"] = "WARNING"
        return clean

    def check_course_back_to_back(self, clean):
        """
        Function: check_course_back_to_back
        Checks for constraint violations in courses and returns data reflecting conflict status.
        """
        for course1, data1 in self.candidate_solution.items():
            if course1 != "Fitness":
                for course2, data2 in self.candidate_solution.items():
                    if course2 != "Fitness":
                        if (course1[0:4] == course2[0:4]) and (course1 != course2):
                            if ((int(course1[5:8]) + 1) == int(course2[5:8])) or \
                               ((int(course1[5:8]) - 1) == int(course2[5:8])):
                                # courses are consecutive in codes
                                if ((int(data1["time"]) + 1) == int(data2["time"])) or \
                                   ((int(data1["time"]) - 1) == int(data2["time"])):
                                    clean[data1["room"]][data1["time"]]["warning"] = "WARNING"
                                    clean[data2["room"]][data2["time"]]["warning"] = "WARNING"
        return clean

    def check_course_years(self, clean):
        """
        Function: check_course_years
        Checks for constraint violations in courses and returns data reflecting conflict status.
        """
        course_dict = {}
        for course, data in self.candidate_solution.items():
            if course == "Fitness":
                continue
            if course[0:6] not in course_dict.keys():
                course_dict[course[0:6]] = [int(data["time"])]
            else:
                if int(data["time"]) in course_dict[course[0:6]]:
                    clean[data["room"]][data["time"]]["warning"] = "WARNING"
                course_dict[course[0:6]].append(int(data["time"]))
        return clean

