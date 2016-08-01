from Population import Population
import os

pop = Population(200, "To be or not to be, that is the question", 0.2)

while (pop.newGen() == False):
	os.system('cls')
	pop.display()
