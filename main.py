import initialization
import evaluation
import survivor_selection
import parent_selection
import recombination
import constraints


# Call the initialization script to build the population for generation 0
init_items = initialization.init(constraints.pop_size)
pop = init_items[0]
courses = init_items[1]
rooms = init_items[2]
profs = init_items[3]
times = init_items[4]

best_fitness = 0
generation = constraints.numgenmax

while generation > 0 and best_fitness < 100:
    print("GENERATION: ", abs(generation-constraints.numgenmax))
    print("STARTING POPULATION: ", pop)
    
    # Calculate fitness scores for each gene in population
    for candidate_solution in range(constraints.pop_size):
        pop[candidate_solution]['Fitness'] = evaluation.calc_fitness(pop[candidate_solution])
#        pop[candidate_solution].append(evaluation.calc_fitness(pop[candidate_solution]))
   
    fitnesses = [x['Fitness'] for x in pop]
    print("FITNESS VALUES: ", fitnesses)
    best_fitness = max(fitnesses)
    print("BEST FITNESS:   ", best_fitness)
    if best_fitness >= 100:
        print("Optimal solution has been identified!")
        exit()
    
 #   exit() # Place holder, below has not been re modelled 


    # Choose parent solutions.  Sends the number of parents to select, and indexed list of fitness scores
    parent_index = parent_selection.select_parents(constraints.parents, fitnesses=fitnesses.copy())
    print("PARENTS: ", parent_index)
    for i in parent_index:
        print(pop[i])
    #print("FITNESS VALUES after parent selection: ", fitnesses)

    # Create children.  Sends the indexed list of parents, and number of children to be returned.  
    # Extend returned list of children to the population.
    pop2 = pop[:]
    print("POPULATION BEFORE NEW CHILDREN:",pop)
    pop.extend(recombination.create_children(len(rooms), len(times), parent_index, fitnesses, constraints.children, pop2))
    print("POPULATION AFTER NEW CHILDREN:",pop)
# Feb 2 - Haven't touched this but it somehow seems to still work.  It should remove X solutions from the population, where X is a constant
# and it should remove those with the lowest fitness scores.
    survivor_index = survivor_selection.cull(constraints.retirees, fitnesses=fitnesses.copy())
    print("RETIREES: ", survivor_index)
    pop_copy = pop.copy()
    for retiree in survivor_index:
        pop.remove(pop_copy[retiree])

    # updating generation
    generation -= 1

print("FINAL POPULATION: ", pop)
