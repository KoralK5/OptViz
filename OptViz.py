from os import system
from time import sleep
from math import *
import pygame

def optimize(f, x, rate=0.1):
	return x - (f(x + 0.001) - f(x)) / 0.001 * rate

def f(x):
	global y; return eval(y)

def draw(screen, coords):
	pygame.draw.rect(screen, (0, 0, 128), pygame.rect.Rect(coords))

x = float(input('x = '))
y = input('y = ')

dims = (700, 300)
screen = pygame.display.set_mode(dims)

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
pygame.display.set_caption('f(x) = ' + y)
pygame.init()

running = True
while running:
	system('clear')

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			break

	x = optimize(f, x)
	print('\nx =', x)
	print('y =', f(x))

	screen.fill((50, 50, 50))
	draw(screen, (350 - x%dims[0], 150 - f(x)%dims[1], 10, 10))

	xRend = str(round(x, 4))
	yRend = str(round(f(x), 4))

	xText = font.render(' '*('-' not in xRend) + xRend, True, 'green')
	yText = font.render(' '*('-' not in yRend) + yRend, True, 'green')

	screen.blit(xText, (625, 15))
	screen.blit(yText, (625, 45))
	pygame.display.update()

	sleep(0.1)
