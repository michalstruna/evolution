import random
from models.individual import Prey	
from services.graphics import init_screen, loop_screen

screen = init_screen()
width, height = screen.get_width(), screen.get_height()

entities = list(map(lambda _: Prey(
	screen=screen,
	pos=(random.randint(100, width - 100), random.randint(100, height - 100)),
	sight=random.randint(1, 10),
	size=random.randint(5, 30),
	speed=random.random() * 2,
	stability=random.random() / 20
), range(10)))

def update():
	for entity in entities:
		entity.move()
		entity.render()

loop_screen(screen, update)