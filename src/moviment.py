from base import *

class Moviment(Component):
	def __init__(self, name, componentWeight, wheels):
		self.wheels = wheels
		self.componentWeight = componentWeight
		Component.__init__(self, name, self.countTotalWeight(), wheels)

	def countTotalWeight():
		result = self.componentWeight
		for wheel in self.wheels:
			result += wheels.getWeight()
		return result

class Wheel(Component):
	def __init__(self, name, weight):
		Component.__init__(self, name, weight, {})
		self.speed = [0.0, 0.0, 0.0]
		self.acceleration = [0.0, 0.0, 0.0]
		self.direction = [0.0, 0.0, 0.0]