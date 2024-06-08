import pygame
import math
import sys
import random

class Color:
	GRAY = (70, 70, 70)
	BLUE = (100, 150, 250)
	RED = (255, 100, 100)
	
class Prey:
	
	def __init__(self, pos=(0, 0), size = 20, sight=4, speed=0.3, rotation=0, stability=0.01, carnivority=0.5):
		self.size = size
		self.sight = sight
		self.pos = pos
		self.speed = speed
		self.rotation = rotation
		self.stability = stability
		self.carnivority = carnivority

	def rotate(self, direction):
		self.rotation += direction * self.stability

	def move(self):
		self.pos = (self.pos[0] + self.speed * math.cos(self.rotation), self.pos[1] + self.speed * math.sin(self.rotation))

	def render(self):
		color = (self.carnivority * 255, 0, (1 - self.carnivority) * 255)

		pygame.draw.circle(
			screen,
			color,
			self.pos,
			self.size
		)

		pygame.draw.circle(
			screen,
			Color.RED, 
			(
				self.pos[0] + self.size * math.cos(self.rotation - 0.5),
				self.pos[1] + self.size * math.sin(self.rotation - 0.5)
			),
			self.sight
		)

		pygame.draw.circle(
			screen,
			Color.RED, 
			(
				self.pos[0] + self.size * math.cos(self.rotation + 0.5),
				self.pos[1] + self.size * math.sin(self.rotation + 0.5)
			),
			self.sight
		)

		pygame.draw.line(
			screen,
			color,
			(
				self.pos[0] - self.size * math.cos(self.rotation),
				self.pos[1] - self.size * math.sin(self.rotation)
			),
			(
				self.pos[0] - self.size * math.cos(self.rotation) * self.stability * 300,
				self.pos[1] - self.size * math.sin(self.rotation) * self.stability * 300
			),
			int(self.stability * 500)
		)

pygame.init()
screen_info = pygame.display.Info()
width, height = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Evolution")

entities = list(map(lambda _: Prey(
	pos=(random.randint(100, width - 100), random.randint(100, height - 100)),
	sight=random.randint(1, 10),
	size=random.randint(5, 30),
	speed=random.random(),
	carnivority=random.random()
), range(100)))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	screen.fill(Color.GRAY)

	i = 0

	for entity in entities:
		i += 1
		entity.move()
		entity.rotate(1 if i % 2 == 0 else -1)
		entity.render()

			
	pygame.display.update()

