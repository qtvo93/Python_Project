# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:52:28 2020

@author: Thinh Vo
"""

import pygame, sys
from datetime import datetime
from playsound import playsound
from pygame import mixer  

mixer.init()

def rotate(surface,angle):
	rotated_surface = pygame.transform.rotozoom(surface,angle,1)
	rotated_rect = rotated_surface.get_rect(center=(400,400))
	return rotated_surface,rotated_rect

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([800,800])
wheel=pygame.image.load("wheel2.png")
arrow=pygame.image.load("arrow.png")
arrow=pygame.transform.scale(arrow, (120, 70))
arrow_rect = arrow.get_rect(center=(750,450))
wheel_rect=wheel.get_rect(center=(400,400))
angle = 0
Run = True
y=1

now = datetime.now() 

while Run == True:
	mixer.music.load('audio.mp3')
	mixer.music.play()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	angle +=1
	screen.fill((255,255,255))
	wheel_rotated,wheel_rotated_rect=rotate(wheel,angle)
	screen.blit(wheel_rotated,wheel_rotated_rect)
	screen.blit(arrow,arrow_rect)
	pygame.display.flip()
	clock.tick(60)	
	
	then = datetime.now() 
	if ((then-now).total_seconds() - 10 )> 0:
		y = 0
		if y == 0:
			mixer.music.stop()
			Run = False		
			
if Run == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	playsound('Tada.mp3')
	screen.blit(arrow,arrow_rect)
	screen.blit(wheel,wheel_rect)
	