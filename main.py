import pygame as pg
from car import Car
from map import game_map
from settings import *

def main():
	pg.init()
	pg.mixer.init()
	scr = pg.display.set_mode((WIDTH,HEIGHT))
	pg.display.set_caption("RaceGame")
	clk = pg.time.Clock()
	running = True
	player = Car((SIZE_OF_BLOCK*1.5,SIZE_OF_BLOCK*1.5))
	while running:
		clk.tick(FPS)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				running = False
		player.mov()
		scr.fill(WHITE)
		for i in range(len(game_map)):
			for j in range(len(game_map[i])):
				if   game_map[i][j]=='#':
					pg.draw.rect(scr,BLACK,(j*SIZE_OF_BLOCK,i*SIZE_OF_BLOCK,
											SIZE_OF_BLOCK,SIZE_OF_BLOCK))
				elif game_map[i][j]=='1':
					scr.blit(FILLED,(j*SIZE_OF_BLOCK,i*SIZE_OF_BLOCK,
									SIZE_OF_BLOCK,SIZE_OF_BLOCK))
				elif game_map[i][j]=='2':
					scr.blit(LL,(j*SIZE_OF_BLOCK,i*SIZE_OF_BLOCK,
								SIZE_OF_BLOCK,SIZE_OF_BLOCK))
				elif game_map[i][j]=='3':
					scr.blit(UL,(j*SIZE_OF_BLOCK,i*SIZE_OF_BLOCK,
								SIZE_OF_BLOCK,SIZE_OF_BLOCK))
				elif game_map[i][j]=='4':
					scr.blit(UR,(j*SIZE_OF_BLOCK,i*SIZE_OF_BLOCK,
								SIZE_OF_BLOCK,SIZE_OF_BLOCK))
				elif game_map[i][j]=='5':
					scr.blit(LR,(j*SIZE_OF_BLOCK,i*SIZE_OF_BLOCK,
								SIZE_OF_BLOCK,SIZE_OF_BLOCK))
				else:
					scr.blit(EMPTY,(j*SIZE_OF_BLOCK,i*SIZE_OF_BLOCK,
									SIZE_OF_BLOCK,SIZE_OF_BLOCK))
		# for x in range(len(game_map)):
		# 	for y in range(len(game_map[x])):
		# 		if game_map[y][x] == '#':
		# 			if (x+1)*SIZE_OF_BLOCK > player.x > x*SIZE_OF_BLOCK and (y+1)*SIZE_OF_BLOCK > player.y > y*SIZE_OF_BLOCK:
		# 				running = False
		player.render(scr)
		pg.display.flip()

if __name__ == '__main__':
	main()