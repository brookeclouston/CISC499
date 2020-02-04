import config

courses = config.config_courses()
profs = config.config_profs()
rooms = config.config_rooms()
times = config.config_times()
profdel = config.config_profcourselinks()
print("Courses:",courses)
print("Profs:",profs)
print("Rooms:",rooms)
print("Times:",times)
print("Links:",profdel)