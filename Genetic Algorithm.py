import random
#The Genes, Target and Input
print ("Overview")
print ("This genetic algorithm generates your desired word/phrase from, basically nonsense")
INPUT = str(input("What would you like this genetic algorithm to find? "))
#The gene set with all our characters
geneSet = "QWERTYUIOPASDFGHJKLZXCVBNM_qwertyuiopasdfghjklzxcvbnm1234567890"
#Our target is the input
target = INPUT

#Random Gene sequence from the gene set
def generateParent(length):
  genes = list ("")#Creates empty string
  for i in range (0, length):
    geneIndex = random.randint(0, len(geneSet) - 1);#Fetches a random number from the given range (it will be used to fetch our random character)
    genes.append(geneSet[geneIndex])#Adds the random character to the emprty string
    #Stops when the required string is full
    #
    #Below the string is join by the thing in '' format ie no spaces in between
  return (''.join(genes))

#just some vars
generation = 0
startTime = '0:00:00'

#The fitness function is defined by the number of characters same
def getFitness(candidate, target):
  fitness = 0
  for i in range (0, len(candidate)):
    #If the characters in the corresponding places(that's why there is a for loop) are same
    if target[i] == candidate[i]:#string[1] basically mean the character at postion 'i'
      #Increase fitness by 1
      fitness += 1
  return (fitness)

#The mutatation function changes one character of the string 'randomly'
def mutate(parent):
  geneIndex = random.randint(0, len(geneSet) - 1)#Fetches a random number to place a mutation (random character from geneSet)
  index = random.randint(0, len(parent) - 1)#Fetches a random number (this will be the place for the mutation to occur)
  genes = list(parent)#Creates a new list with the all the characters of the parent
  #The mutation is made, by changing the characters and certain random places
  genes[index] = geneSet[geneIndex]
  return (''.join(genes))#Returns the newly made string


def display(candidate):
  fitness = getFitness(bestParent, target)
  print ("%s\t%i" % (candidate, fitness))# fancy string formatting

bestParent = generateParent(len(target))#Generates the first random string
firstGen = bestParent#Done this for end summary

bestFitness = getFitness(bestParent, target)#Finds the fitness of the parent

display(bestParent)#Displays the all the stuff for the parent
losers = []

# While the number of the similar characters are less than the number of characters 
while bestFitness < len(bestParent):
  child = mutate(bestParent)
  childFitness = getFitness(child, target)

  if childFitness < bestFitness:
    losers.append(child)
  #Change the value of the fitness etc with the latest values of the children
  if childFitness > bestFitness:
    bestFitness = childFitness
    bestParent = child
    generation += 1
    display(bestParent)
#Displays the summary of the GA
if bestFitness == len(bestParent):
  print ()
  print ('Summary >>')
  print ("It took", generation, "generations to reach the word '",target, "' from '",firstGen,"'. ")
  print (losers)
  print (len(losers))
