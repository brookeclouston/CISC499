"""
This script contains constraint information to be used by the genetic algorithm 
"""

numgenmax = 500 # maximum number of generations (avoid infinite loop)

pop_size = 100 # population size
parents = pop_size // 5 # 20% of the population each generation becomes parents
retirees = pop_size // 5 # 20% of the population each generation 'retires' and leaves the population
parent_selection = 'tournament'
#tournament_y = parents // 2 # half of the parents will enter each tournament 'round'
tournament_y = 3 # unit testing
recombtype = 'crossover'
children = pop_size // 5 # 20% of the population is created as children of the previous gen
mutate_chance = 0.2 # percent chance of a mutation in a given child

filesize = 'reg'