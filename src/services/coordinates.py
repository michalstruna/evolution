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
	diff_angle = norm_rad(path_polar[0] - rotation)
	return rotation + min(step, diff_angle) * (1 if diff_angle < math.pi else -1)

def pos_equal(pos1: Pos, pos2: Pos) -> bool:
	return abs(pos1[0] - pos2[0]) < 1 and abs(pos1[1] - pos2[1]) < 1