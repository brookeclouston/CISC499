import initialization
import evalsimple
import survivor_selection
import parent_simple

numgenmax = 5 # maximum number of generations (avoid infinite loop)
numcourses = 3 # genes
numslots = 9 # chromosomes
numpop = 10 # population size
parents = numpop // 5 # 20% of the population each generation becomes parents
retirees = numpop // 5 # 20% of the population each generation 'retires' and leaves the population

# call the initialization script to build the population for generation 1
pop = initialization.init(numcourses, numslots, numpop)

for generation in range(numgenmax):
    print("GENERATION: ", generation)

    # Initialize the population fitness values to zero
    popfit = [0] * numpop
    print("POPULATION: ",pop)
    
    # Calculate fitness scores for each gene in population
    for gene in range(numpop):
        popfit[gene]=(evalsimple.fitness(pop[gene]))
    print("FITNESS VALUES: ", popfit)
    print("BEST FITTNESS:   ", min(popfit))

    # Choose parents
    parentindex = parent_simple.selectparents(parents, fitnesses = popfit.copy())
    print("PARENTS: ", parentindex)
    for parent_num in range(parents):
        pop.append(pop[parentindex[parent_num]]) # this should call recombination
    print(pop)

    survivorindex = survivor_selection.select_survivor(retirees, fitnesses = popfit.copy())
    print("RETIREES: ", survivorindex)
    for retiree in range(retirees):
        pop.pop(survivorindex[retiree])
    print(pop)

    # needs code here to decide whether to break loop