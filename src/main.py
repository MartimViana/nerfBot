## IMPORTS
from vision import *
from moviment import Moviment, Wheel

## GLOBAL VARIABLES
# Version names
robot_names = ["Arnold", "T800", "T1000", "Beta", "Data", "Optimus", "Iron Giant", "Bruno", "Sentinel", "WALL-E", "Atom", "L-2SO", "A.X.L"]

# Pins
PIN_LEFT_WHEELS_IN = 1
PIN_LEFT_WHEELS_OUT = 2
PIN_RIGHT_WHEELS_IN = 3
PIN_RIGHT_WHEELS_OUT = 4


## FUNCTIONS
def createMoviment():
	# create right wheels
	upRight = Wheel("Upper right wheel", 0, PIN_RIGHT_WHEELS_IN, PIN_RIGHT_WHEELS_OUT)
	downRight = Wheel("Lower right wheel", 0, PIN_RIGHT_WHEELS_IN, PIN_RIGHT_WHEELS_OUT)

	# create left wheels
	upLeft = Wheel("Upper left wheel", 0, PIN_LEFT_WHEELS_IN, PIN_LEFT_WHEELS_OUT)
	downLeft = Wheel("Lower left wheel", 0, PIN_LEFT_WHEELS_IN, PIN_LEFT_WHEELS_OUT)
	return Moviment("Wheels", 0, (upRight, downRight, upLeft, downLeft))

def createCameras():
	return 0

##MAIN CODE
if __name__=='__main__':
	# Instantiate components
	createMoviment()
	createCameras()
