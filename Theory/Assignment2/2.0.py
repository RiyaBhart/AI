import random 
import numpy as np

tasktimes=[5,8,4,7,6,3,9]
facility_cap = [24,30,28]
costmatris = [
    [10, 12, 9],
    [15, 14, 16],
    [8, 9, 7],
    [12, 10, 13],
    [14, 13, 12],
    [9, 8, 10],
    [11, 12, 13]
]

numtask = len(tasktimes)
numfacilities = len(facility_cap)
populationsize = 6
crossover_rate = 0.8
mutation_rate = 0.2
generations = 5

def cal_fitness(chromosomes):
    facility_times = [0] * numfacilities
    totalcost = 0
    for task, facility in enumerate(chromosomes):
        facility_times[facility-1]+=tasktimes[task]
        totalcost+=tasktimes[task]*costmatris[task][facility-1]
        
    penalty = 0
    for f in range(numfacilities):
        if facility_times[f]>facility_cap[f]:
            penalty+=1000*(facility_times[f]-facility_cap[f])
    return totalcost+penalty

population = [[random.randint(1,numfacilities) for _ in range(numtask)] for _ in range(populationsize)]


for generation in range(numfacilities):
    fitness_score = [cal_fitness(chromos) for chromos in population]
    
    totalfitness = sum(1/f for f in fitness_score)
    probabilities = [(1/f)/totalfitness for f in fitness_score]
    new_pop = []
    
    for _ in range(populationsize // 2):
        parents = random.choices(population,weights=probabilities,k=2)
        parent1, parent2 = parents[0],parents[1]
        
        if random.random()<crossover_rate:
            point = random.randint(1,numtask-2)
            child1=parent1[:point]+parent2[point:]
            child2 = parent1[:point]+parent2[point:]  
        else:  
            child1, child2 = parent1[:], parent2[:]
        
        for child in [child1,child2]:
            if random.random()<mutation_rate:
                pos1,pos2 = random.sample(range(numtask),2)
                child[pos1],child[pos2]=child[pos2],child[pos1]
        new_pop.extend([child1,child2])
    population = new_pop
    
fitness_scores = [cal_fitness(chrom) for chrom in population]
best_idx = fitness_scores.index(min(fitness_scores))       
bestchrom = population[best_idx]
bestcost = min(fitness_scores)

print("Best Assignment:", bestchrom)
print("Best Cost:", bestcost)