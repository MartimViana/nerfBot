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

def speed(initialDistance, finalDistance, initialTime, finalTime):
	return (finalDistance - initialDistance) / (finalTime - initialTime)

def acceleration(initialSpeed, finalSpeed, initialTime, finalTime):
	return speed(initialSpeed, finalSpeed, initialTime, finalTime)

def force(mass, acceleration):
	return mass * acceleration


def distance(initialX, finalX, initialY, finalY):
	return math.sqrt((finalX - initialX)*(finalX - initialX) + (finalY - initialY)*(finalY - initialY))

def distance(initialVelocity, time, acceleration):
	return initialVelocity*time + (1/2)*acceleration*time*time

## Ballistical-related calculus
def calculateBulletSpeed(pistonPressure, volumicMassAir, exitRadius, pistonRadius):
	return math.sqrt((pistonPressure - atmosphericPressure)/(volumicMassAir*(1-((exitRadius*exitRadius)/(pistonRadius*pistonRadius)))))

