import initialization
import evalsimple
import survivor_selection
import parent_simple
import recombination

numgenmax = 50 # maximum number of generations (avoid infinite loop)
numcourses = 3 # chromosomes
numslots = 9 # chromosome options
numpop = 10 # population size
parents = numpop // 5 # 20% of the population each generation becomes parents
retirees = numpop // 5 # 20% of the population each generation 'retires' and leaves the population

# call the initialization script to build the population for generation 1
population = initialization.init(numcourses, numslots, numpop)
for j in range(numgenmax):
    print("GENERATION: ",j)
    # initialize the population fitness values to zero
    popfit = [0]*numpop
    print("population: ",population)
# calculate fitness scores for each gene in population
    for i in range(numpop):
        popfit[i]=(evalsimple.fitness(population[i]))
        if popfit[i] >= numcourses * numslots:
            print("Solution reached!!!!!!!!!!!")
            print("Solution: ",population[i])
            quit()
    print("fitness values:",popfit)


# call the selectparents function to determine which genes will become parents
    parentindex = parent_simple.selectparents(parents, fitnesses = popfit.copy())
    print("parents: ",parentindex)
# time to make children
    population2 = population.copy()
    newchildren = recombination.createchildren(population2, parentindex, "clone", numslots, fitnesses = popfit.copy())
#    print(population)
    print("New children: ",newchildren)
    population.extend(newchildren)
#    for i in range(parents):
#        population.append(population[parentindex[i]]) # this should call recombination instead of just a clone
#    print(population)

# call the cull function to identify low-fitness solutions within the population
    survivorindex = survivor_selection.cull(retirees, fitnesses = popfit.copy())
    print("retirees: ",survivorindex)
# remove the solutions returned by cull
    for i in range(retirees):
        population.pop(survivorindex[i])
#    print(population)
    # needs code here to decide whether to break loop