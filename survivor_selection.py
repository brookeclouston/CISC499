def cull(numretirees, fitnesses):

    retireelist=[0]*numretirees
    for i in range(numretirees):
        min = 99999
        for j,value in enumerate(fitnesses):
            if value<min:
                min = value
                index = j
        retireelist[i]=index
        fitnesses[index]=99999
    #        print(fitnesses)

    return retireelist

# print(cull([13, 20, 14, 11, 21],1))