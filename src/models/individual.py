import math
import pygame
from services.ui import Color
from abc import ABC, abstractmethod
from services.coordinates import get_random_pos, move, get_rotation_to_target, pos_equal

class Individual(ABC):

	def __init__(
			self,
			screen: pygame.Surface,
			pos: tuple[int, int]=(0, 0),
			size: float=20,
			sight: float=4,
			speed: float=0.3,
			rotation: float=0,
			stability: float=0.01
		):
		self.screen = screen
		self.size = size
		self.sight = sight
		self.pos = pos
		self.speed = speed
		self.rotation = rotation
		self.stability = stability
		self.target = self.pos

	@abstractmethod
	def render(self):
		pass

	def rotate(self, direction: int):
		self.rotation = (self.rotation + direction * self.stability) % (2 * math.pi)

	def move(self):
		if pos_equal(self.target, self.pos):
			self.target = get_random_pos(self.screen.get_width(), self.screen.get_height())

		self.rotation = get_rotation_to_target(self.pos, self.target, self.rotation, self.stability)
		self.pos = move(self.pos, self.rotation, self.speed)


class Prey(Individual):

	def render(self):
		# Body
		pygame.draw.circle(
			self.screen,
			Color.BLUE,
			self.pos,
			self.size
		)

		# Eye
		pygame.draw.circle(
			self.screen,
			Color.RED, 
			(
				self.pos[0] + self.size * math.cos(self.rotation - 0.5),
				self.pos[1] + self.size * math.sin(self.rotation - 0.5)
			),
			self.sight
		)

		# Eye
		pygame.draw.circle(
			self.screen,
			Color.RED, 
			(
				self.pos[0] + self.size * math.cos(self.rotation + 0.5),
				self.pos[1] + self.size * math.sin(self.rotation + 0.5)
			),
			self.sight
		)

		# Tail
		pygame.draw.line(
			self.screen,
			Color.BLUE,
			(
				self.pos[0] - self.size * math.cos(self.rotation),
				self.pos[1] - self.size * math.sin(self.rotation)
			),
			(
				self.pos[0] - self.size * math.cos(self.rotation) * self.stability * 100,
				self.pos[1] - self.size * math.sin(self.rotation) * self.stability * 100
			),
			int(self.stability * 200)
		)

		pygame.draw.circle(self.screen, Color.RED, self.target, 10)