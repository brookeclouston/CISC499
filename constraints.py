"""
This script contains constraint information to be used by the genetic algorithm, separated to make
easy modifications.  
"""

numgenmax = 500 # maximum number of generations (avoid infinite loop)
pop_size = 20 # population size

parents = max(2,pop_size // 5) # 20% of the population each generation becomes parents
retirees = max(2,pop_size // 5) # 20% of population each generation leaves the population

parent_selection = "roulette"
tournament_y = parents // 2 # half of the parents will enter each tournament 'round'

recombtype = 'crossover'  # requires at least two parents per generation
children = max(2,pop_size // 5) # 20% of the population is created as children of the previous gen
mutate_chance = 0.01 # percent chance of a mutation in a given child

filesize = 'reg' # use regular input files. options include 'small'
