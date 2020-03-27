"""
Driver script for program, handles flow of execution and visualization.
"""
import initialization
import evaluation
import survivor_selection
import parent_selection
import recombination
import constraints
from visulization import Visulization
import matplotlib.pyplot as plt
import time
import os
import random
 
# Call the initialization script to collect configuration data from csv files and build the
# population for generation 0
init_items = initialization.init(constraints.pop_size)
pop = init_items[0]
courses = init_items[1]
rooms = init_items[2]
profs = init_items[3]
times = init_items[4]

best_fitness = 0
generation = constraints.numgenmax
viable_gen = -1
record_fitness = 0
fit_log = []

# Visualization setup 
plt.show()
axes = plt.gca()
axes.set_xlim(0, generation)
axes.set_ylim(0, 100) # set to 90 initially to make things more interesting 
gen_data, avg_data, best_data = [], [], []
avg_line, = axes.plot(gen_data, avg_data, color='red', label="Average Fitness")
best_line = axes.plot(gen_data, best_data, color='blue', label="Best Fitness")
plt.legend(loc="lower right")
plt.title("Average Fitness", fontsize=20)
plt.xlabel('Generation')
plt.ylabel('Fitness Value')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
V = Visulization("")

# while loop with two exit criteria: optimal solution found or ran out of generations
while generation > -1 and best_fitness < 101:
    # Calculate fitness scores for each gene in population.  Send each solution by itself and get
    # a fitness score back. Higher is better
    fitsoft = []
    for candidate_solution in range(constraints.pop_size):
        pop[candidate_solution]['Fitness'] = evaluation.calc_fitness(pop[candidate_solution])[0]
        fitsoft.append(evaluation.calc_fitness(pop[candidate_solution])[1])
        
    # Creates list of fitness scores
    fitnesses = [x['Fitness'] for x in pop]
    # store average and best fitness scores within the population
    avg_fitness = sum(fitnesses) / len(fitnesses)
    best_fitness = max(fitnesses)
    if best_fitness > record_fitness:
        fit_log.append((best_fitness, abs(generation-constraints.numgenmax)))
        record_fitness = best_fitness
    
    gen_data.append(abs(generation-constraints.numgenmax))
    avg_data.append(avg_fitness)
    best_data.append(best_fitness)
    
    avg_line, = axes.plot(gen_data, avg_data, color='red', label="Average Fitness")
    best_line = axes.plot(gen_data, best_data, color='blue', label="Best Fitness")
    plt.draw()
    plt.pause(1e-17)
    time.sleep(0.1)
    
    for cand in pop:
        if cand["Fitness"] == best_fitness:
            # Tells solution to render solution with best fitness 
            V.generation = str(abs(generation-constraints.numgenmax))
            V.candidate_solution = cand
            V.render_temp()
            break
    time.sleep(1)
    
    # Check for first viable solution
    if viable_gen < 0:
        for i in range(len(fitnesses)):
            if fitnesses[i]+fitsoft[i] == 100:
                viable_gen = abs(generation-constraints.numgenmax)
    # Check for exit criteria: optimal solution or too many generations 
   
    # Check for optimal solution 
    if best_fitness >= 100:
        print("Optimal solution has been identified after generation", constraints.numgenmax-generation)
        exit()
    if generation <= 0:
        print("No optimal solution was found after",constraints.numgenmax,"generations.")
        print("Viable solution was found after", viable_gen, "generations.")
        print(fit_log)
        exit()

    # Choose parent solutions
    parent_index = parent_selection.select_parents(constraints.parents, fitnesses=fitnesses.copy())
    
    # Create children.  Sends the indexed list of parents, and number of children to be returned.  
    # Extend returned list of children to the population.
    pop2 = pop[:]
    pop.extend(recombination.create_children(len(rooms), len(times), parent_index, fitnesses, constraints.children, pop2))

    survivor_index = survivor_selection.cull(constraints.retirees, fitnesses=fitnesses.copy())
    
    pop_copy = pop.copy()
    for retiree in survivor_index:
        pass
        pop.remove(pop_copy[retiree])

    # updating generation
    generation -= 1
