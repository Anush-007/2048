import pygame
from pygame import constants

from package.constants import Constants
from package.grid import Grid



const = Constants()

#setup

win = pygame.display.set_mode((const.size, const.size))
pygame.display.set_caption(const.title)

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
