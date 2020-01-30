import initialization
import evaluation
import survivor_selection
import parent_selection
import constraints


# Call the initialization script to build the population for generation 0
pop = initialization.init(constraints.pop_size)
best_fitness = 0
generation = constraints.numgenmax

while generation > 0 and best_fitness < 100:
    print("GENERATION: ", abs(generation-constraints.numgenmax))

    print("STARTING POPULATION: ", pop)
    
    # Calculate fitness scores for each gene in population
    for candidate_solution in range(constraints.pop_size):
        pop[candidate_solution].append(evaluation.basic_fitness(pop[candidate_solution]))
   
    fitnesses = [x[1] for x in pop]
    print("FITNESS VALUES: ", fitnesses)
    best_fitness = max(fitness)
    print("BEST FITTNESS:   ", best_fitnesses)
    
    exit() # Place holder, below has not been re modelled 


    # Choose parents
    parent_index = parent_selection.select_parents_tournament(constraints.parents, fitnesses=pop_fit.copy())
    print("PARENTS: ", parent_index)
    for parent in parent_index:
        children = pop[parent]# this should call recombination
        pop.append(children) 

    survivor_index = survivor_selection.cull(constraints.retirees, fitnesses=pop_fit.copy())
    print("RETIREES: ", survivor_index)
    pop_copy = pop.copy()
    for retiree in survivor_index:
        pop.remove(pop_copy[retiree])

    # updating generation
    generation -= 1

print("FINAL POPULATION: ", pop)
