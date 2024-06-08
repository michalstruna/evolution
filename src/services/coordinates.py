import math
from random import randint

Pos = tuple[float, float]

def polar_to_cartesian(pos: Pos) -> Pos:
	pass

def cartesian_to_polar(pos: Pos) -> Pos:
	angle = math.atan2(pos[1], pos[0])
	distance = math.sqrt(pos[0]**2 + pos[1]**2)
	return(angle, distance)

def get_random_pos(max_x: int, max_y: int) -> Pos:
	return (randint(0, max_x), randint(0, max_y))

def move(start: Pos, direction: float, distance: float) -> Pos:
	return (start[0] + distance * math.cos(direction), start[1] + distance * math.sin(direction))

def norm_rad(rad: float) -> float:
	return (rad + 2 * math.pi) % (2 * math.pi)

def get_pos_diff(pos1: Pos, pos2: Pos) -> Pos:
	return (pos2[0] - pos1[0], pos2[1] - pos1[1])

def get_rotation_to_target(pos: Pos, target: Pos, rotation: float, step: float) -> float:
	path_polar = cartesian_to_polar(get_pos_diff(pos, target))
	return path_polar[0]

def pos_equal(pos1: Pos, pos2: Pos) -> bool:
	return round(pos1[0]) == round(pos2[0]) and round(pos1[1]) == round(pos2[1])