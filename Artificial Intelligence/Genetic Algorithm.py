import random

print("Overview")
print("This genetic algorithm generates your desired word/phrase from, basically nonsense")
INPUT = str(input("What would you like this genetic algorithm to find? "))

geneSet = "QWERTYUIOPASDFGHJKLZXCVBNM_qwertyuiopasdfghjklzxcvbnm1234567890"
target = INPUT


def generateParent(length):
    genes = list("") 
    for i in range(0, length):
      geneIndex = random.randint(0, len(geneSet) - 1)
      genes.append(geneSet[geneIndex])
    return (''.join(genes))


generation = 0
startTime = '0:00:00'

def getFitness(candidate, target):
    fitness = 0
    for i in range(0, len(candidate)):
        if target[i] == candidate[i]: 
            fitness += 1
    return (fitness)

def mutate(parent):
    geneIndex = random.randint(0, len(geneSet) - 1)
    index = random.randint(0, len(parent) - 1)
    genes = list(parent)
    genes[index] = geneSet[geneIndex]
    return (''.join(genes)) 


def display(candidate):
    fitness = getFitness(bestParent, target)
    print("%s\t%i" % (candidate, fitness)) 


bestParent = generateParent(len(target)) 
firstGen = bestParent 

bestFitness = getFitness(bestParent, target) 

display(bestParent)  
losers = []

while bestFitness < len(bestParent):
    child = mutate(bestParent)
    childFitness = getFitness(child, target)

    if childFitness < bestFitness:
        losers.append(child)
    if childFitness > bestFitness:
        bestFitness = childFitness
        bestParent = child
        generation += 1
        display(bestParent)
        
if bestFitness == len(bestParent):
    print()
    print('Summary >>')
    print("It took", generation, "generations to reach the word '",
          target, "' from '", firstGen, "'. ")
    print(losers)
    print(len(losers))
