
#Skeleton for game


"""importing pygame and random.
pygame: module to make games using oython, has certain fnctions and methods which help cretae objects for a 
		game and add effects to make game more interactive 
random: when generating enemies and where they appear, we use random to create a uniqueness for each game """
import pygame
import random

# The height and width give a description of the size of the window for our game
# Fps is frames per second and higher it is, smoother and faster the game. adjust accordingly for your game
width = 400
height = 500
FPS = 30

#colors 
# there are written based on the RGB model for colors. ( refer rgb model for more colors )
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


#initialize game window
# pygame has a punction init(), this has to be present to make your code run.
pygame.init()
pygame.mixer.init() #for music and media
screen = pygame.display.set_mode((width,height)) #this is the screen or window for our game to run init	
pygame.display.set_caption("Warp") # set_caption() is used to name our game when we run it.
clock = pygame.time.Clock() # Clock() function is used to make delays within the game, such as delay in re-spawning player


""" sprite is a computer graphic which may be moved on-screen and otherwise manipulated as a single entity.
	here we are grouping all sprites for different objects (player, enemies, projectiles etc.,) 
	so that we can update and render them together"""
all_sprites = pygame.sprite.Group()

#Game Loop
""" this is the heart if our game, this follows the game loop.
	it takes inputs(key presses)
	it updates sprites and other constraints such as lives, difficulty etc.,
	it renders or draws the spries after all the above and it is an indefinite loop	"""
running = True #use this so that we can control the loop
while running:
	#keep loop running at FPS
	clock.tick(FPS)
	#inputs
	for event in pygame.event.get(): #an event is an action we do or an  input we give to the game such as a key press
		#closing window
		if event.type == pygame.QUIT:
			running = False
	
	#update
	all_sprites.update() #the all_sprites group we created earlier can be updated together 
	
	#drawing/ rendering
	screen.fill(black) # initially we want the screen to be black and hence we fill it
	all_sprites.draw(screen) #drawing or rendering all the sprites we store for differnt objects in the game
	
	#update after drawing
	pygame.display.update() #this updates the window after we draw the sprites

pygame.quit() #this is a fuction in pygame which closes the window when the close button is pressed
