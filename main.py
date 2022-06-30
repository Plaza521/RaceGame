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
				if   game_map[i][j]=='#':
					pg.draw.rect(scr,BLACK,(j*SIZE_OF_BLOCK+player.x,i*SIZE_OF_BLOCK+player.y,
											SIZE_OF_BLOCK,SIZE_OF_BLOCK))
				elif game_map[i][j]=='1':
					scr.blit(FILLED, (j*SIZE_OF_BLOCK-player.x+WIDTH//2,i*SIZE_OF_BLOCK-player.y+HEIGHT//2))
					if (y+1)*SIZE_OF_BLOCK > player.y > y*SIZE_OF_BLOCK and (x+1)*SIZE_OF_BLOCK > player.x > x*SIZE_OF_BLOCK:
						is_collision = True
				elif game_map[i][j]=='2':
					scr.blit(LLO,    (j*SIZE_OF_BLOCK-player.x+WIDTH//2,i*SIZE_OF_BLOCK-player.y+HEIGHT//2))
					if (y+1)*SIZE_OF_BLOCK - SIZE_OF_BLOCK/4 > player.y > y*SIZE_OF_BLOCK + SIZE_OF_BLOCK/4 and (x+1)*SIZE_OF_BLOCK - SIZE_OF_BLOCK/4 > player.x > x*SIZE_OF_BLOCK + SIZE_OF_BLOCK/4:
						is_collision = True # Lower wall
					if (y+1)*SIZE_OF_BLOCK > player.y > y*SIZE_OF_BLOCK and x*SIZE_OF_BLOCK + SIZE_OF_BLOCK/4 > player.x > x*SIZE_OF_BLOCK:
						is_collision = True # Left wall
					if (y+1)*SIZE_OF_BLOCK > player.y > (y+1)*SIZE_OF_BLOCK - SIZE_OF_BLOCK/4 and (x+1)*SIZE_OF_BLOCK > player.x > x*SIZE_OF_BLOCK:
						is_collision = True # Square in center
				elif game_map[i][j]=='3':
					if (y+1)*SIZE_OF_BLOCK > player.y > y*SIZE_OF_BLOCK and x*SIZE_OF_BLOCK + SIZE_OF_BLOCK/4 > player.x > x*SIZE_OF_BLOCK:
						is_collision = True # Left wall
					if y*SIZE_OF_BLOCK + SIZE_OF_BLOCK/4 > player.y > y*SIZE_OF_BLOCK and (x+1)*SIZE_OF_BLOCK > player.x > x*SIZE_OF_BLOCK:
						is_collision = True # Upper wall
					if (y+1)*SIZE_OF_BLOCK - SIZE_OF_BLOCK/4 > player.y > y*SIZE_OF_BLOCK + SIZE_OF_BLOCK/4 and (x+1)*SIZE_OF_BLOCK - SIZE_OF_BLOCK/4 > player.x > x*SIZE_OF_BLOCK + SIZE_OF_BLOCK/4:
						is_collision = True # Square in center
					scr.blit(ULO,    (j*SIZE_OF_BLOCK-player.x+WIDTH//2,i*SIZE_OF_BLOCK-player.y+HEIGHT//2))
				elif game_map[i][j]=='4':
					if y*SIZE_OF_BLOCK + SIZE_OF_BLOCK/4 > player.y > y*SIZE_OF_BLOCK and (x+1)*SIZE_OF_BLOCK > player.x > x*SIZE_OF_BLOCK:
						is_collision = True # Upper wall
					if (y+1)*SIZE_OF_BLOCK > player.y > y*SIZE_OF_BLOCK and (x+1)*SIZE_OF_BLOCK > player.x > (x+1)*SIZE_OF_BLOCK - SIZE_OF_BLOCK/4:
						is_collision = True # Right wall
					if (y+1)*SIZE_OF_BLOCK - SIZE_OF_BLOCK/4 > player.y > y*SIZE_OF_BLOCK + SIZE_OF_BLOCK/4 and (x+1)*SIZE_OF_BLOCK - SIZE_OF_BLOCK/4 > player.x > x*SIZE_OF_BLOCK + SIZE_OF_BLOCK/4:
						is_collision = True # Square in center
					scr.blit(URO,    (j*SIZE_OF_BLOCK-player.x+WIDTH//2,i*SIZE_OF_BLOCK-player.y+HEIGHT//2))
				elif game_map[i][j]=='5':
					if (y+1)*SIZE_OF_BLOCK > player.y > y*SIZE_OF_BLOCK and (x+1)*SIZE_OF_BLOCK > player.x > (x+1)*SIZE_OF_BLOCK - SIZE_OF_BLOCK/4:
						is_collision = True # Right wall
					if (y+1)*SIZE_OF_BLOCK > player.y > (y+1)*SIZE_OF_BLOCK-SIZE_OF_BLOCK/4 and (x+1)*SIZE_OF_BLOCK > player.x > x*SIZE_OF_BLOCK:
						is_collision = True # Lower wall
					if (y+1)*SIZE_OF_BLOCK - SIZE_OF_BLOCK/4 > player.y > y*SIZE_OF_BLOCK + SIZE_OF_BLOCK/4 and (x+1)*SIZE_OF_BLOCK - SIZE_OF_BLOCK/4 > player.x > x*SIZE_OF_BLOCK + SIZE_OF_BLOCK/4:
						is_collision = True # Square in center
					scr.blit(LRO,    (j*SIZE_OF_BLOCK-player.x+WIDTH//2,i*SIZE_OF_BLOCK-player.y+HEIGHT//2))
				elif game_map[i][j]=='6':
					scr.blit(LLI,    (j*SIZE_OF_BLOCK-player.x+WIDTH//2,i*SIZE_OF_BLOCK-player.y+HEIGHT//2))
					if (y+1)*SIZE_OF_BLOCK > player.y > y*SIZE_OF_BLOCK and x*SIZE_OF_BLOCK + SIZE_OF_BLOCK/4 > player.x > x*SIZE_OF_BLOCK:
						is_collision = True # Left wall
					if (y+1)*SIZE_OF_BLOCK > player.y > (y+1)*SIZE_OF_BLOCK-SIZE_OF_BLOCK/4 and (x+1)*SIZE_OF_BLOCK > player.x > x*SIZE_OF_BLOCK:
						is_collision = True # Lower wall
					if (y+1)*SIZE_OF_BLOCK-SIZE_OF_BLOCK/4 > player.y > y*SIZE_OF_BLOCK+SIZE_OF_BLOCK/2 and x*SIZE_OF_BLOCK + SIZE_OF_BLOCK/2 > player.x > x*SIZE_OF_BLOCK + SIZE_OF_BLOCK/4:
						is_collision = True # Dot in center
				elif game_map[i][j]=='7':
					scr.blit(ULI,    (j*SIZE_OF_BLOCK-player.x+WIDTH//2,i*SIZE_OF_BLOCK-player.y+HEIGHT//2))
					if (y+1)*SIZE_OF_BLOCK > player.y > y*SIZE_OF_BLOCK and x*SIZE_OF_BLOCK + SIZE_OF_BLOCK/4 > player.x > x*SIZE_OF_BLOCK:
						is_collision = True # Left wall
					if y*SIZE_OF_BLOCK + SIZE_OF_BLOCK/4 > player.y > y*SIZE_OF_BLOCK and (x+1)*SIZE_OF_BLOCK > player.x > x*SIZE_OF_BLOCK:
						is_collision = True # Upper wall
					if y*SIZE_OF_BLOCK+SIZE_OF_BLOCK/2 > player.y > y*SIZE_OF_BLOCK+SIZE_OF_BLOCK/4 and x*SIZE_OF_BLOCK+SIZE_OF_BLOCK/2 > player.x > x*SIZE_OF_BLOCK+SIZE_OF_BLOCK/4:
						is_collision = True # Dot in center
				elif game_map[i][j]=='8':
					if y*SIZE_OF_BLOCK + SIZE_OF_BLOCK/4 > player.y > y*SIZE_OF_BLOCK and (x+1)*SIZE_OF_BLOCK > player.x > x*SIZE_OF_BLOCK:
						is_collision = True # Upper wall
					if (y+1)*SIZE_OF_BLOCK > player.y > y*SIZE_OF_BLOCK and (x+1)*SIZE_OF_BLOCK > player.x > (x+1)*SIZE_OF_BLOCK - SIZE_OF_BLOCK/4:
						is_collision = True # Right wall
					if y*SIZE_OF_BLOCK+SIZE_OF_BLOCK/2 > player.y > y*SIZE_OF_BLOCK+SIZE_OF_BLOCK/4 and (x+1)*SIZE_OF_BLOCK-SIZE_OF_BLOCK/4 > player.x > x*SIZE_OF_BLOCK+SIZE_OF_BLOCK/2:
						is_collision = True # Dot in center
					scr.blit(URI,    (j*SIZE_OF_BLOCK-player.x+WIDTH//2,i*SIZE_OF_BLOCK-player.y+HEIGHT//2))
				elif game_map[i][j]=='9':
					if (y+1)*SIZE_OF_BLOCK > player.y > y*SIZE_OF_BLOCK and (x+1)*SIZE_OF_BLOCK > player.x > (x+1)*SIZE_OF_BLOCK - SIZE_OF_BLOCK/4:
						is_collision = True # Right wall
					if (y+1)*SIZE_OF_BLOCK > player.y > (y+1)*SIZE_OF_BLOCK-SIZE_OF_BLOCK/4 and (x+1)*SIZE_OF_BLOCK > player.x > x*SIZE_OF_BLOCK:
						is_collision = True # Lower wall
					if (y+1)*SIZE_OF_BLOCK-SIZE_OF_BLOCK/4 > player.y > y*SIZE_OF_BLOCK+SIZE_OF_BLOCK/2 and (x+1)*SIZE_OF_BLOCK-SIZE_OF_BLOCK/4 > player.x > x*SIZE_OF_BLOCK+SIZE_OF_BLOCK/2:
						is_collision = True # Dot in center
					scr.blit(LRI,    (j*SIZE_OF_BLOCK-player.x+WIDTH//2,i*SIZE_OF_BLOCK-player.y+HEIGHT//2))
				else:
					scr.blit(EMPTY,  (j*SIZE_OF_BLOCK-player.x+WIDTH//2,i*SIZE_OF_BLOCK-player.y+HEIGHT//2))
		if is_collision:
			# running = False
			pg.draw.rect(scr,RED,(0,0,10,10))
			is_collision = False
		# for x in range(len(game_map)):
		# 	for y in range(len(game_map[x])):
		# 		if game_map[x][y] != '0':
		# 			if (x+1)*SIZE_OF_BLOCK > player.y > x*SIZE_OF_BLOCK and (y+1)*SIZE_OF_BLOCK > player.x > y*SIZE_OF_BLOCK:
		# 				running = False

		player.render(scr)
		pg.display.flip()

if __name__ == '__main__':
	main()