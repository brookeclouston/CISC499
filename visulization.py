"""
This script handles the visualization for the algorithm 
"""
import webbrowser
import os
import config
from jinja2 import Environment, FileSystemLoader


file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)


class Visulization:
    def __init__(self, solution):
        self.candidate_solution = solution
        self.template = env.get_template('table_template.txt')
        self.filepath = "file://" + os.path.realpath("schedule.html")
        self.generation = "0"
        self.times = config.config_times()
        self.classrooms = config.config_rooms()
        self.render_temp()
        webbrowser.register('mychrome', None, webbrowser.MacOSXOSAScript('Google Chrome'), -1) # NOTE: might be different on msft
        webbrowser.get('mychrome').open(self.filepath)
    
    def render_temp(self):
        if self.candidate_solution != "":
            clean = self.format_data()
            output = self.template.render(GENERATION=self.generation, FILEPATH=self.filepath, 
                                        TIMES=self.times, CLASSROOMS=self.classrooms, DATA=clean)
            f = open('schedule.html','w')
            f.write(output)
            f.close()

    def format_data(self):
        clean = []
        for x in range(len(self.classrooms)):
            new = []
            for y in range(len(self.times)):
                new.append({"error": "", "class": "", "prof": "", "room": list(self.classrooms.keys())[x], "time": self.times[y]["Name"]})
            clean.append(new)
        clean = self.check_rooms(clean)
        clean = self.check_profs(clean)
        clean = self.check_capacity(clean)
        return clean

    def check_rooms(self, clean):
        rooms = []
        for course, attrs in self.candidate_solution.items():
            if course != "Fitness":
                sections_rooms = [attrs["time"], attrs["room"]]
                if sections_rooms in rooms:
                    # conflict                                       
                    clean[attrs["room"]][attrs["time"]]["error"] = "ERROR"
                else:
                    clean[attrs["room"]][attrs["time"]]["class"] = course
                rooms.append(sections_rooms)
        return clean

    def check_profs(self, clean):
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

                
