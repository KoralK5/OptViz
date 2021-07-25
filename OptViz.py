from os import system
from time import sleep
from math import *
import pygame

def optimize(f, x, rate=0.1):
	return x - (f(x + 0.001) - f(x)) / 0.001 * rate

def f(x):
	global y; return eval(y)

def draw(screen, coords, color):
	pygame.draw.rect(screen, color, pygame.rect.Rect(coords))

x = float(input('x = '))
y = input('y = ')

dims = (700, 300)
screen = pygame.display.set_mode(dims)

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
pygame.display.set_caption('f(x) = ' + y)
pygame.init()
starter = f(x)

running = True
while running:
	system('clear')

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			break

	x = optimize(f, x)
	fx = f(x)

	color = (255 - max(min(starter/fx, 255), 0), max(min(starter/fx, 255), 0), 0)

	screen.fill((50, 50, 50))
	draw(screen, (abs(350 - x%dims[0]), abs(150 - fx%dims[1]), 10, 10), color)

	xRend = format(x, '.4f') if -1000 < x < 1000 else format(x, '.4E')
	yRend = format(fx, '.4f') if -1000 < fx < 1000 else format(fx, '.4E')

	xText = font.render(' '*('-' not in xRend) + xRend, True, color)
	yText = font.render(' '*('-' not in yRend) + yRend, True, color)

	screen.blit(xText, (15, 15))
	screen.blit(yText, (15, 45))
	pygame.display.update()

	sleep(0.1)
