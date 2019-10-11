
'''
		The most elementar class in the nerf bot project.
'''
class Component:
	def __init__(self, name, weight, subcomponents):
		self.name = name
		self.weight = weight
		self.subcomponents = subcomponents