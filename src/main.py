import random
import copy
import sys


test1 = [
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, 00, -1, 00, 00, 00, 00, 00, 00],
        [00, -1, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, -1, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, -1, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, 00, 00, 00, 00, -1, -1, 00, 00],
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
    ]


test2 = [
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, 00, -1, 00, 00, 00, 00, 00, 00],
        [00, -1, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, -1, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, -1, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, 00, 00, -1, -1, -1, 00, 00, 00],
        [00, 00, 00, 00, 00, 00, -1, 00, -1, 00, 00, 00],
        [00, 00, 00, 00, 00, 00, -1, -1, -1, 00, 00, 00],
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
    ]


test3 = [
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, -1, -1, -1, -1, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, -1, 00, 00, 00, 00, 00, 00, 00],
        [00, -1, -1, -1, -1, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
    ]


test4 = [
        [00, 00, 00, 00, 00, 00, 00, -1, 00, -1, 00, 00],
        [00, 00, 00, 00, 00, 00, 00, -1, -1, -1, 00, 00],
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
        [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00],
    ]


class GGarden:
    def __init__(self):
        self.generateRandomMap()
        self.countrocks()
        self.fitness()

    def generateRandomMap(self):
        self.m = random.randrange(2, 11)
        self.n = random.randrange(2, 11)
        self.map = []
        for i in range(self.m):
            row = []
            for j in range(self.n):
                if random.random() < 0.1:
                    row.append(-1)
                else:
                    row.append(0)
            self.map.append(row)

    def countrocks(self):
        self.rocks = 0
        for i in self.map:
            for j in i:
                if j == -1:
                    self.rocks += 1

    def fitness(self):
        self.max_fitness = 0
        for i in self.map:
            for j in i:
                if j == 0:
                    self.max_fitness += 1


class Garden:
    def __init__(self, map):
        self.fillMap(map)
        self.countrocks()
        self.fitness()

    def fillMap(self, map):
        self.m = len(map)
        self.n = len(map[0])
        self.map = copy.deepcopy(map)

    def countrocks(self):
        self.rocks = 0
        for i in self.map:
            for j in i:
                if j == -1:
                    self.rocks += 1

    def fitness(self):
        self.max_fitness = 0
        for i in self.map:
            for j in i:
                if j == 0:
                    self.max_fitness += 1


class Gene:
    def __init__(self, garden):
        row = garden.m
        column = garden.n
        number = random.randrange((row + column) + (row + column))
        # Each direction has its own function for movement
        if number < column:                             # Down
            self.down(number)
        elif column <= number < row + column:           # Left
            self.left(column, number)
        elif row + column <= number < column + column + row: # up
            self.up(row, column, number)
        else:                                           # Right
            self.right(row, column, number)
        self.rotate()

    # Moving down
    def down(self, number):
        self.start = (0, number)
        self.goTo = '1' # Representing dow

    # Moving left
    def left(self, column, number):
        self.start = (number - column, column - 1)
        self.goTo = '2' # Representing left

    # Moving up
    def up(self, row, column, number):
        self.start = (row - 1, column + column + row - number - 1)
        self.goTo = '3' # Representing up

    # Moving up
    def right(self, row, column, number):
        self.start = ((row + column) + (row + column) - number - 1, 0)
        self.goTo = '4' # Representing right

    def rotate(self):
        self.rotation = [
            int(a)
            for a in bin(random.randrange(1024))
                [2:].zfill(10)
        ]


class Chromosome:
    def __init__(self, garden, start=True):
        self.garden = garden
        self.fGarden = Garden(self.garden.map)
        self.genesFill(garden, start)

    def genesFill(self, garden, start):
        self.genes = []
        helper = garden.m + garden.n + garden.rocks
        if start == True:
            for i in range(helper):
                self.genes.append(Gene(self.garden))
            self.algo()

    def fitnessFunc(self):
        self.fitness = 0
        itera = sum(self.fGarden.map, [])
        for x in itera:
            if x > 0:
                self.fitness += 1

    def algo(self):
        g = self.fGarden

        number = 0

        # Start of genes iterations
        for gene in self.genes:
            position = list(gene.start)
            goTo = gene.goTo
            x = 0

            # We check if we can enter the garden
            if g.map[position[0]][position[1]] != 0:
                continue
            number += 1

            while (1):
                # Rake the tile
                g.map[position[0]][position[1]] = number

                # We chose next tile to move on
                if goTo == '3':
                    position[0] -= 1
                elif goTo == '1':
                    position[0] += 1
                elif goTo == '2':
                    position[1] -= 1
                elif goTo == '4':
                    position[1] += 1

                # We check if it it not edge of the map
                if position[0] not in range(g.m) or position[1] not in range(g.n):
                    break

                # We check if it is not raken - if not we move there
                if g.map[position[0]][position[1]] == 0:
                    continue

                # If we fing any obstacle we change movement direction
                if goTo == '3':
                    position[0] += 1
                elif goTo == '1':
                    position[0] -= 1
                elif goTo == '2':
                    position[1] += 1
                elif goTo == '4':
                    position[1] -= 1

                # We choose new tile
                if goTo == '3' or goTo == '1':
                    helper = ([position[0], position[1] - 1], [position[0], position[1] + 1])
                else:
                    helper = ([position[0] - 1, position[1]], [position[0] + 1, position[1]])

                # We check surrounding tiles
                nv = []
                for p in helper:
                    try:
                        nv.append(g.map[p[0]][p[1]])
                    except IndexError:
                        nv.append('X')
                # If we find one not raken
                if nv.count(0) == 1:
                    position = helper[nv.index(0)]

                # if we find two not raken
                elif nv.count(0) == 2:
                    position = helper[gene.rotation[x]]
                    x += 1
                    if x == len(gene.rotation):
                        x = 0

                # If everything is raken
                else:
                    if 'X' not in nv:
                        self.fitnessFunc()
                        return
                    break

                if goTo == '3' or goTo == '1':
                    if helper.index(position) == 0:
                        goTo = '2'
                    else:
                        goTo = '4'
                else:
                    if helper.index(position) == 0:
                        goTo = '3'
                    else:
                        goTo = '1'

            self.fitnessFunc()

    # Mutation of chromosomes
    def mutate(self, newChr):
        for i in range(len(newChr.genes)):
            # New chromosome
            number = random.random()
            if number < 0.1:
                newChr.genes[i] = Gene(self.garden)
            # New rotations
            elif number < 0.2:
                newChr.genes[i].rotate()

    # Crossing of new chromosomes
    def crossing(self, other):
        # Create new chromosome with empty genes
        newChr = Chromosome(self.garden, False)

        # Crossing process
        mutateNum = random.random()
        crossNum = random.random()
        pivotPoint = random.randrange(len(self.genes))
        if crossNum < 0.85:
            # Crossing second type - 1 - Choosing random genes from both
            newChr.genes = []
            for i in range(len(self.genes)):
                newChr.genes.append(random.choice((self.genes[i], other.genes[i])))
        elif crossNum < 0.425:
            # Crossing first type - 2 - first part is from Chromosome 1, second is from Chromosome 2
            newChr.genes = self.genes[:pivotPoint] + other.genes[pivotPoint:]
        else:
            # Crossing third type - 3 - No crossing
            newChr.genes = random.choice((self.genes, other.genes))

        # Mutations
        if mutateNum < 0.5:
            self.mutate(newChr)

        newChr.algo()
        return newChr

def solveMap(map):
    # Inicialisation of variables
    generation = []

    # Garden creation
    garden = Garden(map)

    # Creation of starting set of chromosones
    for i in range(50):
        generation.append(Chromosome(garden))

    # Generations creation
    for i in range(1000):
        # Saving the best chromosome
        bestChr = max(generation, key=lambda x: x.fitness)
        nextGeneration = [bestChr]
        # Check if we didnt find solution
        if bestChr.fitness == garden.max_fitness:
            break
        # Creating more chromosones to fill generation
        for j in range(49):
            # Choose random chromosomes from current generation
            chromosome1, chromosome2 = sorted(random.sample(generation, 4), key=lambda x: x.fitness)[2:4]
            # Create very new Chromosome by crossing and mutation
            nextGeneration.append(chromosome1.crossing(chromosome2))
        generation = nextGeneration
    number = i
    # Formatted Print
    finalprint(garden, bestChr, number)

def generateMap():

    # Inicialisation of variables
    generation = []

    # Garden creation
    garden = GGarden()

    # Creation of starting set of chromosones
    for i in range(50):
        generation.append(Chromosome(garden))

    # Generations creation
    for i in range(800):
        # Saving the best chromosome
        bestChr = max(generation, key=lambda x: x.fitness)
        nextGeneration = [bestChr]
        # Check if we didnt find solution
        if bestChr.fitness == garden.max_fitness:
            break
        # Creating more chromosones to fill generation
        for j in range(49):
            # Choose random chromosomes from current generation
            chromosome1, chromosome2 = sorted(random.sample(generation, 4), key=lambda x: x.fitness)[2:4]
            # Create very new Chromosome by crossing and mutation
            nextGeneration.append(chromosome1.crossing(chromosome2))
        generation = nextGeneration
    number = i
    # Formatted Print
    finalprint(garden, bestChr, number)


def finalprint(garden, best, number):
    print()
    print()

    # Printing all necesarry generation information
    print('Generations:%4d  Max-Fitness:%4d  Best-Fitness:%4d' % (number + 1, garden.max_fitness, best.fitness))
    print('Tiles Left: %d' % (garden.max_fitness - best.fitness))
    print("_________________________________________________________")
    print("Initial Garden")

    # Transforming garden into clear grided output
    helper = ""
    for x in garden.map:
        for y in x:
            if y == -1:
                helper += ' K '
            else:
                helper += '%2d ' % y
        helper += '\n'
    print(helper)

    print("_________________________________________________________")
    print("Final Result")

    # Transforming solved garden into clear grided output

    helper = ""
    for x in best.fGarden.map:
        for y in x:
            if y == -1:
                helper += ' K '
            else:
                helper += '%2d ' % y
        helper += '\n'
    print(helper)

    print("_________________________________________________________")
    sys.exit()


print("----------------->Welcome to Zen Garden<-----------------")
print("")
print("Choose to load a map from a file or generate a random one")
print("_________________________________________________________")
print("Write: File - Load from file")
print("Write: Generate - Generate random map")
print("Write: Test - Test mode")
print("_________________________________________________________")
inp = input()

# File Function - loading from File
if inp == "File" or inp == "file":
    print("Counting...")
    file = []
    # File opening
    f = open("garden.txt", "r")
    pocet = 0
    # Transforming chars into 2D array of integers
    while(1):
        row = []
        riadok = f.readline()
        if riadok == '':
            break
        pocet += 1
        riadok = riadok.split()
        for i in riadok:
            if i == '00':
                row.append(0)
            if i == '-1':
                row.append(-1)
        file.append(row)
    solveMap(file)
elif inp == "Generate" or inp == "generate":    # Generate Function - generate Random garden
    print("Counting...")
    generateMap()
elif inp == "Test" or inp == "test":            # Test Function - Choose from availbale tests
    print("_________________________________________________________")
    print("Choose the number of test from 1 - 4")
    print("Test1 - Model test")
    print("Test2 - Unsolvable test")
    print("Test3 - Test with staying in the garden")
    print("Test4 - Test with one tile exit")
    print("_________________________________________________________")
    inp = input()
    if inp == '1':
        print("Counting...")
        solveMap(test1)
    elif inp == '2':
        print("Counting...")
        solveMap(test2)
    elif inp == '3':
        print("Counting...")
        solveMap(test3)
    elif inp == '4':
        print("Counting...")
        solveMap(test4)
    else:
        print("You entered wrong command")
        sys.exit()
else:
    print("You entered wrong command")
    sys.exit()
