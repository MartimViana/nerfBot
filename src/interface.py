#	interface.py
#	This program will serve as the connection between the hardware and the
#	software components.
#
#	IMPORTS
import math

#	GLOBAL VARIABLES
elementaryCharge = 1.6*10^(-19)
atmosphericPressure = 0

#	FUNCTIONS
##	Basic calculations
def wattsToJoules(watts, seconds):
	return watts * seconds

def joulesToWatts(joules, seconds):
	return joules / seconds

def wattsToNewtons(watts, seconds, distance):
	return distance * wattsToJoules(watts, seconds)

def newtonsToWatts(newtons, seconds, distance):
	return joulesToWatts(newtons / distance, seconds)

## Ballistical-related calculus
def calculateBulletSpeed(pistonPressure, volumicMassAir, exitRadius, pistonRadius):
	return math.sqrt((pistonPressure - atmosphericPressure)/(volumicMassAir*(1-((exitRadius*exitRadius)/(pistonRadius*pistonRadius)))))

	