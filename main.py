import pygame as pg
from car import Car
from map import game_map
import other
from settings import *

def main():
	pg.init()
	pg.mixer.init()
	scr = pg.display.set_mode((WIDTH,HEIGHT))
	pg.display.set_caption("RaceGame")
	clk = pg.time.Clock()
	running = True
	player = Car((SIZE_OF_BLOCK*1.5,SIZE_OF_BLOCK*1.5))
	timer = other.Timer(scr)
	is_collision = False
	while running:
		clk.tick(FPS)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				running = False
		player.mov()
		scr.fill(WHITE)
		for i in range(len(game_map)):
			for j in range(len(game_map[i])):
				x,y = j,i
				ypmult, ymult = (y+1)*SIZE_OF_BLOCK, y*SIZE_OF_BLOCK
				xpmult, xmult = (x+1)*SIZE_OF_BLOCK, x*SIZE_OF_BLOCK
				if   game_map[i][j]=='#':
					pg.draw.rect(scr,BLACK,(xmult+player.x,ymult+player.y,
											SIZE_OF_BLOCK,SIZE_OF_BLOCK))
				elif game_map[i][j]=='1':
					scr.blit(FILLED, (xmult-player.x+H_WIDTH,ymult-player.y+H_HEIGHT))
					if ypmult > player.y > ymult and xpmult > player.x > xmult:
						is_collision = True
				elif game_map[i][j]=='S':
					scr.blit(START, (xmult-player.x+H_WIDTH,ymult-player.y+H_HEIGHT))
					if ypmult > player.y > ymult and xpmult > player.x > xmult:
						timer.start()
				elif game_map[i][j]=='F':
					scr.blit(FINISH, (xmult-player.x+H_WIDTH,ymult-player.y+H_HEIGHT))
					if ypmult > player.y > ymult and xpmult > player.x > xmult:
						timer.finish()
				elif game_map[i][j]=='2':
					scr.blit(LLO,    (xmult-player.x+H_WIDTH,ymult-player.y+H_HEIGHT))
					if ypmult - QUAD_OF_BLOCK > player.y > ymult + QUAD_OF_BLOCK and xpmult - QUAD_OF_BLOCK > player.x > xmult + QUAD_OF_BLOCK:
						is_collision = True # Lower wall
					if ypmult > player.y > ymult and xmult + QUAD_OF_BLOCK > player.x > xmult:
						is_collision = True # Left wall
					if ypmult > player.y > ypmult - QUAD_OF_BLOCK and xpmult > player.x > xmult:
						is_collision = True # Square in center
				elif game_map[i][j]=='3':
					if ypmult > player.y > ymult and xmult + QUAD_OF_BLOCK > player.x > xmult:
						is_collision = True # Left wall
					if ymult + QUAD_OF_BLOCK > player.y > ymult and xpmult > player.x > xmult:
						is_collision = True # Upper wall
					if ypmult - QUAD_OF_BLOCK > player.y > ymult + QUAD_OF_BLOCK and xpmult - QUAD_OF_BLOCK > player.x > xmult + QUAD_OF_BLOCK:
						is_collision = True # Square in center
					scr.blit(ULO,    (xmult-player.x+H_WIDTH,ymult-player.y+H_HEIGHT))
				elif game_map[i][j]=='4':
					if ymult + QUAD_OF_BLOCK > player.y > ymult and xpmult > player.x > xmult:
						is_collision = True # Upper wall
					if ypmult > player.y > ymult and xpmult > player.x > xpmult - QUAD_OF_BLOCK:
						is_collision = True # Right wall
					if ypmult - QUAD_OF_BLOCK > player.y > ymult + QUAD_OF_BLOCK and xpmult - QUAD_OF_BLOCK > player.x > xmult + QUAD_OF_BLOCK:
						is_collision = True # Square in center
					scr.blit(URO,    (xmult-player.x+H_WIDTH,ymult-player.y+H_HEIGHT))
				elif game_map[i][j]=='5':
					if ypmult > player.y > ymult and xpmult > player.x > xpmult - QUAD_OF_BLOCK:
						is_collision = True # Right wall
					if ypmult > player.y > ypmult-QUAD_OF_BLOCK and xpmult > player.x > xmult:
						is_collision = True # Lower wall
					if ypmult - QUAD_OF_BLOCK > player.y > ymult + QUAD_OF_BLOCK and xpmult - QUAD_OF_BLOCK > player.x > xmult + QUAD_OF_BLOCK:
						is_collision = True # Square in center
					scr.blit(LRO,    (xmult-player.x+H_WIDTH,ymult-player.y+H_HEIGHT))
				elif game_map[i][j]=='6':
					scr.blit(LLI,    (xmult-player.x+H_WIDTH,ymult-player.y+H_HEIGHT))
					if ypmult > player.y > ymult and xmult + QUAD_OF_BLOCK > player.x > xmult:
						is_collision = True # Left wall
					if ypmult > player.y > ypmult-QUAD_OF_BLOCK and xpmult > player.x > xmult:
						is_collision = True # Lower wall
					if ypmult-QUAD_OF_BLOCK > player.y > ymult+HALF_OF_BLOCK and xmult + HALF_OF_BLOCK > player.x > xmult + QUAD_OF_BLOCK:
						is_collision = True # Dot in center
				elif game_map[i][j]=='7':
					scr.blit(ULI,    (xmult-player.x+H_WIDTH,ymult-player.y+H_HEIGHT))
					if ypmult > player.y > ymult and xmult + QUAD_OF_BLOCK > player.x > xmult:
						is_collision = True # Left wall
					if ymult + QUAD_OF_BLOCK > player.y > ymult and xpmult > player.x > xmult:
						is_collision = True # Upper wall
					if ymult+HALF_OF_BLOCK > player.y > ymult+QUAD_OF_BLOCK and xmult+HALF_OF_BLOCK > player.x > xmult+QUAD_OF_BLOCK:
						is_collision = True # Dot in center
				elif game_map[i][j]=='8':
					if ymult + QUAD_OF_BLOCK > player.y > ymult and xpmult > player.x > xmult:
						is_collision = True # Upper wall
					if ypmult > player.y > ymult and xpmult > player.x > xpmult - QUAD_OF_BLOCK:
						is_collision = True # Right wall
					if ymult+HALF_OF_BLOCK > player.y > ymult+QUAD_OF_BLOCK and xpmult-QUAD_OF_BLOCK > player.x > xmult+HALF_OF_BLOCK:
						is_collision = True # Dot in center
					scr.blit(URI,    (xmult-player.x+H_WIDTH,ymult-player.y+H_HEIGHT))
				elif game_map[i][j]=='9':
					if ypmult > player.y > ymult and xpmult > player.x > xpmult - QUAD_OF_BLOCK:
						is_collision = True # Right wall
					if ypmult > player.y > ypmult-QUAD_OF_BLOCK and xpmult > player.x > xmult:
						is_collision = True # Lower wall
					if ypmult-QUAD_OF_BLOCK > player.y > ymult+HALF_OF_BLOCK and xpmult-QUAD_OF_BLOCK > player.x > xmult+HALF_OF_BLOCK:
						is_collision = True # Dot in center
					scr.blit(LRI,    (xmult-player.x+H_WIDTH,ymult-player.y+H_HEIGHT))
				else:
					scr.blit(EMPTY,  (xmult-player.x+H_WIDTH,ymult-player.y+H_HEIGHT))
		if is_collision:
			running = False
			# pg.draw.rect(scr,RED,(0,0,10,10))
			# is_collision = False
		# for x in range(len(game_map)):
		# 	for y in range(len(game_map[x])):
		# 		if game_map[x][y] != '0':
		# 			if xpmult > player.y > xmult and ypmult > player.x > ymult:
		# 				running = False
		timer.tick()
		player.render(scr)
		timer.render()
		pg.display.flip()


if __name__ == '__main__':
	main()