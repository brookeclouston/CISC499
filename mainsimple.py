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
for j in range(numgenmax):
    print("GENERATION: ",j)
    # initialize the population fitness values to zero
    popfit = [0]*numpop
    print("population: ",pop)
# calculate fitness scores for each gene in population
    for i in range(numpop):
        popfit[i]=(evalsimple.fitness(pop[i]))
    print("fitness values:",popfit)

    parentindex = parent_simple.selectparents(parents, fitnesses = popfit.copy())
    print("parents: ",parentindex)
    for i in range(parents):
        pop.append(pop[parentindex[i]]) # this should call recombination
    print(pop)

    survivorindex = survivor_selection.cull(retirees, fitnesses = popfit.copy())
    print("retirees: ",survivorindex)
    for i in range(retirees):
        pop.pop(survivorindex[i])
    print(pop)
    # needs code here to decide whether to break loop