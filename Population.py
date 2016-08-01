from DNA import DNA
from random import randint
import math

class Population:
	def __init__(self, popAmmount, target, mutRate):
		self.mutRate = mutRate
		self.gen = 0
		self.target = target
		self.population = []
		for i in range(popAmmount):
			self.population.append(DNA(len(target)))

	def display(self):
		out = ""
		for g in self.population:
			out += g.display() + ' fitness: ' + str(g.calcFitness(self.target)) +'\n'
		out += 'gen number: ' + str(self.gen)
		print (out)

	def calcFitness(self):
		for g in self.population:
			g.calcFitness(self.target)

	def naturalSelection(self):
		self.matingPool = []
		for i in self.population:
			fitness = math.floor(i.calcFitness(self.target) * 100)
			for j in range(fitness):
				self.matingPool.append(i)

	def checkGen(self):
		for i in range(len(self.population)):
			if self.target == "".join(self.population[i].genes):
				return True
		return False

	def newGen(self):
		self.naturalSelection()
		for i in range(len(self.population)):
			#select parents
			a = randint(0, len(self.matingPool) - 1)
			parent1 = self.matingPool[a]
			b = randint(0, len(self.matingPool) - 1)
			parent2 = self.matingPool[b]
			#cossvover
			child = parent1.crossover(parent2);
			#mutation
			child.mutation(self.mutRate)
			self.population[i] = child
		self.gen = self.gen + 1
		return self.checkGen()
