def selectparents(numparents,fitnesses):
    parentlist=[0]*numparents
    for i in range(numparents):
        max = 0
        for j,value in enumerate(fitnesses):
            if value>max:
                max = value
                index = j
        parentlist[i]=index
        fitnesses[index]=0
#        print(fitnesses)

    return parentlist