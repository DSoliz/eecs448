import pygame, sys
from pygame.locals import *
import math
import time


pygame.init()
display = pygame.display.set_mode((400,400),0,32)

#colors
BLACK =(0,0,0)
WHITE =(255,255,255)

#r = desired radius
r = 200
radius = r*r

#clock center
center = 200

x = 0.0
y = 0.0
i = 0.0

while True:
	#clear the display
	display.fill(WHITE)
	
	#drawing line
	pygame.draw.line(display, BLACK, (200, 200), (center+x, center+y), 4)
	
	#update display changes
	pygame.display.update()
	
	#math function
	y = r*(math.sin(i))
	x = r*(math.cos(i))
	
	#increase
	i += 2*math.pi/60
	
	#time interval between each loop run
	time.sleep(1)
	
	#for quitting pygame window
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()