import initialization
import evaluation
import survivor_selection
import parent_selection
import recombination
import constraints


# Call the initialization script to collect configuration data from csv files and build the population for generation 0
init_items = initialization.init(constraints.pop_size)
pop = init_items[0]
courses = init_items[1]
rooms = init_items[2]
profs = init_items[3]
times = init_items[4]

best_fitness = 0
generation = constraints.numgenmax

# while loop with two exit criteria: optimal solution found or ran out of generations
while generation > -1 and best_fitness < 100:
    print("GENERATION: ", abs(generation-constraints.numgenmax))
    #print("STARTING POPULATION: ", pop)
    
    # Calculate fitness scores for each gene in population.  Send each solution by itself and get
    #  a fitness score back. Higher is better
    for candidate_solution in range(constraints.pop_size):
        pop[candidate_solution]['Fitness'] = evaluation.calc_fitness(pop[candidate_solution])

    # creates list of fitness scores
    fitnesses = [x['Fitness'] for x in pop]
    print("FITNESS VALUES: ", fitnesses)
    
    best_fitness = max(fitnesses)
    print("BEST FITNESS:   ", best_fitness)
    # Check for optimal solution 
    if best_fitness >= 100:
        # FIXME: Should be extended to provide the optimal solution, not just saying it exists somewhere.
        print("Optimal solution has been identified after generation",constraints.numgenmax-generation)
        exit()
    if generation <= 0:
        # failure. sadness
        print("No optimal solution was found after",constraints.numgenmax,"generations.")
        exit()

    # Choose parent solutions
    parent_index = parent_selection.select_parents(constraints.parents, fitnesses=fitnesses.copy())
    print("PARENTS: ", parent_index)

    # Create children.  Sends the indexed list of parents, and number of children to be returned.  
    # Extend returned list of children to the population.
    pop2 = pop[:]
    pop.extend(recombination.create_children(len(rooms), len(times), parent_index, fitnesses, constraints.children, pop2))

    # FIXME: Should remove X solutions from the population, where X is a constant
    # and remove those with the lowest fitness scores.
    survivor_index = survivor_selection.cull(constraints.retirees, fitnesses=fitnesses.copy())
    print("RETIREES: ", survivor_index)
    pop_copy = pop.copy()
    for retiree in survivor_index:
        pop.remove(pop_copy[retiree])

    # updating generation
    generation -= 1


print("FINAL POPULATION: ", pop)
