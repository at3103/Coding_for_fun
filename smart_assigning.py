def smartAssigning(names, statuses, projects, tasks):
    if statuses.count(False) == 1:
        return names[statuses.index(False)]
    min = ["",1000,1000]
    for i in range(len(statuses)):
        if tasks[i] < min[1]:
            min=[names[i],tasks[i],projects[i]]
            
        elif tasks[i] == min[1]:
            if projects[i] < min[2]:
                min=[names[i],tasks[i],projects[i]]
            
    return min[0]


names = ["John", 
 "Martin"]
statuses= [False, False]
projects= [20, 1]
tasks= [16, 5]

print smartAssigning(names, statuses, projects, tasks)