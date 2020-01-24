import initialization
import evaluation
import survivor_selection
import parent_selection

numgenmax = 5 # maximum number of generations (avoid infinite loop)
profs_num = 3 # number of profs 
courses_num = 10 # genes / number of courses
sections_num = 4 # chromosomes / number of time sections
pop_size = 10 # population size
parents = pop_size // 5 # 20% of the population each generation becomes parents
retirees = pop_size // 5 # 20% of the population each generation 'retires' and leaves the population

# Call the initialization script to build the population for generation 0
pop = initialization.init(courses_num, pop_size, time_table_size=(profs_num*sections_num))
best_fitness = 0
generation = numgenmax

time_table = initialization.create_time_table(profs_num, sections_num)

while generation > 0 and best_fitness < 100:
    print("GENERATION: ", abs(generation-numgenmax))

    # Initialize the population fitness values to zero
    pop_fit = [0] * pop_size
    print("STARTING POPULATION: ", pop)
    
    # Calculate fitness scores for each gene in population
    for gene in range(pop_size):
        pop_fit[gene] = (evaluation.basic_fitness(pop[gene], time_table))
    print("FITNESS VALUES: ", pop_fit)
    best_fitness = max(pop_fit)
    print("BEST FITTNESS:   ", best_fitness)
    
    # Choose parents
    parent_index = parent_selection.select_parents_tournament(parents, fitnesses=pop_fit.copy())
    print("PARENTS: ", parent_index)
    for parent in parent_index:
        children = pop[parent]# this should call recombination
        pop.append(children) 

    survivor_index = survivor_selection.cull(retirees, fitnesses=pop_fit.copy())
    print("RETIREES: ", survivor_index)
    pop_copy = pop.copy()
    for retiree in survivor_index:
        pop.remove(pop_copy[retiree])

    # updating generation
    generation -= 1

print("FINAL POPULATION: ", pop)
