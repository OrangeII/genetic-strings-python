from random import randint, random

def randomChar():
	charInt = randint(32, 122)
	char = chr(charInt)
	return char

class DNA:
	def __init__(self, length):
		self.genes = []
		for i in range(length):
			self.genes.append(randomChar())

	def display(self):
		out = ""
		for gene in self.genes:
			out += str(gene)
		return out

	def calcFitness(self, target):
		score = 0
		for i in range(len(self.genes)):
			if self.genes[i] == target[i]:
				score = score + 1
		self.fitness = score / len(target)
		return self.fitness

	def crossover(self, mate):
		child = DNA(len(self.genes))
		pivot = randint(0, len(self.genes) - 2) + 1
		for i in range(len(self.genes)):
			if i > pivot:
				child.genes[i] = mate.genes[i]
			else:
				child.genes[i] = self.genes[i]
		return child

	def mutation(self, mutRate):
		i = randint(0, len(self.genes)-1)
		if random() < mutRate:
			self.genes[i] = randomChar()
