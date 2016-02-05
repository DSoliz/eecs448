import pygame, sys
from pygame.locals import *
import math
import time

HEIGHT = WIDTH = 400

pygame.init()
display = pygame.display.set_mode((HEIGHT,WIDTH),0,32)

#colors
BLACK =(0,0,0)
RED = (255,0,0)
WHITE =(255,255,255)

#r = desired radius
r = HEIGHT/2

radius = r*r

#clock center for vector start positions
center = HEIGHT/2

time_input = 0

sec = time_input * ((2*math.pi)/60)

#need method to draw markers

#infinite loop to run clock
while True:
	#clear and fill the display
	display.fill(WHITE)

	#draw markers

	#math function to determine end of vector position
	y_sec = r*(-math.cos(sec))
	x_sec = r*(math.sin(sec))
	
	#drawing line
	pygame.draw.line(display, RED, (center, center), (center+x_sec, center+y_sec), 2)
	
	#update display changes
	pygame.display.update()
	
	#increase by 1/60 of revolution AKA 1 second
	sec += 2*math.pi/60
	
	#time interval between each loop run set to 1 second
	time.sleep(1)
	
	#for loop used check quit command from pygame window AKA press the X to quit
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
