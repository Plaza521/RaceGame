import pygame as pg
import math
from settings import *

class Car:
	def __init__(self,cords: (float,float)):
		self.x = cords[0]
		self.y = cords[1]
		self.self_spd = 0
		self.angle = 0

	@property
	def pos(self):
		return (self.x,self.y)
	

	def mov(self):
		cos_a = math.cos(self.angle)
		sin_a = math.sin(self.angle)
		keys = pg.key.get_pressed()
		if keys[FORWARD] and keys[BACK]:
			if self.self_spd>0:
				self.self_spd -= SPEED
			if self.self_spd<0:
				self.self_spd += SPEED
		elif keys[FORWARD]:
			if self.self_spd>=0:
				self.self_spd += SPEED
			else:
				self.self_spd += SPEED*2
			# self.x += cos_a * SPEED
			# self.y += sin_a * SPEED
		elif keys[BACK]:
			if self.self_spd<=0:
				self.self_spd -= SPEED
			else:
				self.self_spd -= SPEED*2
			# self.x -= cos_a * SPEED
			# self.y -= sin_a * SPEED
		if not keys[FORWARD] and not keys[BACK]:
			if self.self_spd>0:
				self.self_spd -= SPEED
			if self.self_spd<0:
				self.self_spd += SPEED
		self.x += cos_a * self.self_spd
		self.y += sin_a * self.self_spd
		if keys[LEFT]:
			if self.self_spd>=0:
				self.angle-=SPD_T
			else:
				self.angle+=SPD_T
		if keys[RIGHT]:
			if self.self_spd>=0:
				self.angle+=SPD_T
			else:
				self.angle-=SPD_T

	def render(self,scr):
		pg.draw.line(scr,SANDY,(WIDTH//2,HEIGHT//2),(WIDTH//2+math.cos(self.angle)*40,
											   		 HEIGHT//2+math.sin(self.angle)*40))
		pg.draw.circle(scr,BLACK,(WIDTH//2,HEIGHT//2),6)