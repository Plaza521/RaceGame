import pygame
import time
from settings import *

class Timer:
	def __init__(self, scr):
		self.scr = scr
		self.timer = 0
		self.timer_work = False
		self.is_started = False
		self.TIMER_FONT = pg.font.Font(TIMER_FONT_NAME,TIMER_SIZE)
	def start(self):
		if not self.is_started:
			self.timer_work = True
			self.timer_start = time.time_ns()/1_000_000_000
			self.is_started = True
	def tick(self):
		if self.timer_work:
			self.timer = time.time_ns()/1_000_000_000 - self.timer_start
	def render(self):
		out_text = self.TIMER_FONT.render(f"{self.timer}", 0, TIMER_COLOR)
		self.scr.blit(out_text, (0,0))
	def finish(self):
		self.timer_work = False