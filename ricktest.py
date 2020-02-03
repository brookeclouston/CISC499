profcourses = [
    {'Prof': 'Dr. Hu', 'Course': 'CISC 101'}, 
    {'Prof': 'Dr. Blostein', 'Course': 'CISC 102'}, 
    {'Prof': 'Prof. Dove', 'Course': 'CISC 103'}
]
output = next(item for item in profcourses if item["Course"] == "CISC 101")
print(output)