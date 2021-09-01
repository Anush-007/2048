import pygame
from pygame import constants

from package.constants import size, title
from package.grid import Grid



#setup

win = pygame.display.set_mode((size, size))
pygame.display.set_caption(title)

def gameloop():
	game_not_over = True
	game_not_exit = True

	grid = Grid()

	while game_not_over:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_not_over = False

			if event.type == pygame.KEYDOWN:
				grid.move(event.key)


		
		win.fill((75, 50, 60))
		pygame.display.update()

gameloop()

pygame.quit()
quit()
