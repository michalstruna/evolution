from typing import Callable
import pygame
import sys
from services.ui import Color

def init_screen() -> pygame.Surface:
	pygame.init()
	screen_info = pygame.display.Info()
	width, height = screen_info.current_w, screen_info.current_h
	pygame.display.set_caption("Evolution")
	return pygame.display.set_mode((width, height))


def loop_screen(screen: pygame.Surface, update: Callable) -> None:
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		screen.fill(Color.GRAY)
		update()
		pygame.display.update()
