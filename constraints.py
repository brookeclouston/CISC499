"""
This script contains constraint information to be used by the genetic algorithm 
"""

numgenmax = 5 # maximum number of generations (avoid infinite loop)
#profs_num = 3 # number of profs 
#courses_num = 10 # genes / number of courses
#sections = ["Monday 9am", "Monday 11am", "Monday 1pm", "Monday 3pm"] # chromosomes / number of time sections
pop_size = 100 # population size
parents = pop_size // 5 # 20% of the population each generation becomes parents
retirees = pop_size // 5 # 20% of the population each generation 'retires' and leaves the population
