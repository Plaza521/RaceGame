from settings import SIZE_OF_BLOCK
import random

# 132 637466978 87543 43 3 1 89098 5 4 5689 58656 5 4 423

with open('map.cfg','r') as mmm:
	game_map = mmm.read().split()


# ████████████████████████████████████████████████████████████████
# ████████████████████████████████████████████████████████████████
# ████████████████████████████████████████████████████████████████
# ████████████████████████████████████████████████████████████████
# ████████████████								  ████████████████
# ████████████										  ████████████
# ██████████											██████████
# ██████████											██████████
# ████████				████████████████████			  ████████
# ████████			████████████████████████████		  ████████
# ████████			████████████████████████████		  ████████
# ████████		  ████████████████████████████████		  ████████
# ████████		  ████████████████████████████████		  ████████
# ████████		  ████████████		  ████████████		  ████████
# ████████		  ██████████		  	██████████		  ████████
# ████████		  ██████████		  	██████████		  ████████
# ████████		  ██████████	  		██████████		  ████████
# ████████		  ██████████	        ██████████		  ████████
# ████████   	  ████████████	      ████████████		  ████████
# ████████	 	  ████████████████████████████████  	  ████████
# ████████		  ████████████████████████████████		  ████████
# ████████		    ████████████████████████████		  ████████
# ████████		    ████████████████████████████		  ████████
# ████████		  		████████████████████			  ████████
# ██████████	  				  						██████████
# ██████████	  				  						██████████
# ████████████    				  					  ████████████
# ████████████████				  				  ████████████████
# ████████████████████████████████████████████████████████████████
# ████████████████████████████████████████████████████████████████
# ████████████████████████████████████████████████████████████████
# ████████████████████████████████████████████████████████████████