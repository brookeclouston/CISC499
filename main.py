import initialization
import evaluation
import survivor_selection
import parent_selection

numgenmax = 5 # maximum number of generations (avoid infinite loop)
numcourses = 3 # genes
numslots = 9 # chromosomes
numpop = 10 # population size
parents = numpop // 5 # 20% of the population each generation becomes parents
retirees = numpop // 5 # 20% of the population each generation 'retires' and leaves the population

# Call the initialization script to build the population for generation 0
pop = initialization.init(numcourses, numslots, numpop)
best_fitness = 0
generation = numgenmax

while generation > 0 and best_fitness < 100:
    print("GENERATION: ", abs(generation-numgenmax))

    # Initialize the population fitness values to zero
    popfit = [0] * numpop
    print("STARTING POPULATION: ", pop)
    
    # Calculate fitness scores for each gene in population
    for gene in range(numpop):
        popfit[gene] = (evaluation.fitness(pop[gene]))
    print("FITNESS VALUES: ", popfit)
    best_fitness = max(popfit)
    print("BEST FITTNESS:   ", best_fitness)

    survivor_index = survivor_selection.cull(retirees, fitnesses=popfit.copy())
    print("RETIREES: ", survivor_index)
    pop_copy = pop.copy()
    for retiree in survivor_index:
        pop.remove(pop_copy[retiree])
    
    # Choose parents
    parent_index = parent_selection.select_parents_tournament(parents, fitnesses=popfit.copy())
    print("PARENTS: ", parent_index)
    for parent in parent_index:
        children = pop[parent]# this should call recombination
        pop.append(children) 
    
    print("FINAL POPULATION: ", pop)
    generation -= 1
