from base import *

class Camera(Component):
	def __init__(self, name, weight, angle):
		Component.__init__(self, name, weight, {})
		self.angle = angle