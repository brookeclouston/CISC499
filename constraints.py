"""
This script contains constraint information to be used by the genetic algorithm 
"""

numgenmax = 10 # maximum number of generations (avoid infinite loop)

pop_size = 10 # population size
parents = max(1,pop_size // 5) # 20% of the population each generation becomes parents
retirees = max(1,pop_size // 5) # 20% of the population each generation 'retires' and leaves the population
#parent_selection = 'tournament'
parent_selection = "rank"
#tournament_y = parents // 2 # half of the parents will enter each tournament 'round'
tournament_y = 3 # unit testing
#recombtype = 'clone'
recombtype = 'crossover'
children = max(1,pop_size // 5) # 20% of the population is created as children of the previous gen
mutate_chance = 0.00 # percent chance of a mutation in a given child


filesize = 'reg' # use regular input files. options include 'small'
