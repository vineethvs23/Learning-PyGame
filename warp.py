
#Skeleton for game
import pygame
import random

width = 400
height = 500
FPS = 60

#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#initialize game window
pygame.init()
pygame.mixer.init() #for music and media
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Warp!")
clock = pygame.time.Clock()
difficulty = 20

font_name = pygame.font.match_font("arial")
def draw_text(surf, text, size, x,y):
	font = pygame.font.Font(font_name,size)
	text_surface = font.render(text,True, white) #true means the text can be antialiased or not
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x,y)
	surf.blit(text_surface,text_rect)


def draw_lives(surf,x,y,lives,image):
	for i in range(lives):
		image_rect = image.get_rect()
		image_rect.x = x + 25 * i
		image_rect.y = y
		surf.blit(image,image_rect)

def show_screen():
	screen.blit(background,background_rect)
	draw_text(screen,"Warp!",64,width/2,height/4)
	draw_text(screen,"arrow keys to move, space to shoot",22,width/2,height/2)	
	draw_text(screen,"press enter to begin",18, width/2, height *0.75)
	pygame.display.update()	
	waiting = True
	while waiting:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_RETURN:
					waiting = False	



class Player(pygame.sprite.Sprite):
	"""docstring for Player"""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((50,40))
		self.image = pygame.transform.scale(player_image,(50,40))
		self.image.set_colorkey(black)
		self.rect =  self.image.get_rect()
		self.radius = 19
		#pygame.draw.circle(self.image, red,self.rect.center,self.radius)
		self.rect.centerx = width/2
		self.rect.bottom = height-10
		self.speedx = 0
		self.lives = 3
		self.hidden = False
		self.hidden_time = pygame.time.get_ticks()


	def update(self):
		#unhide
		if self.hidden and pygame.time.get_ticks() - self.hidden_time > 1000:
			self.hidden = False
			self.rect.center = (width/2, height-30)

		self.speedx = 0
		keystate = pygame.key.get_pressed()#list of keys pressed
		if keystate[pygame.K_LEFT]: #use k_a dor any other keys for actions
			self.speedx = -5
		if keystate[pygame.K_RIGHT]:
			self.speedx = 5	
		self.rect.x	+= self.speedx
		if self.rect.right > width:
			self.rect.right = width
		if self.rect.left <0:
			self.rect.left =0	

	def shoot(self):
		bullet = Bullet(self.rect.centerx, self.rect.top)#bottom of bullet at top of player
		all_sprites.add(bullet)
		bullets.add(bullet)
		shoot_sound.play()	

	def hide(self):
		#hide player
		self.hidden = True
		self.hidden_time = pygame.time.get_ticks()
		self.rect.center = (width/2, height+200)


class Bots(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((30,30))
		self.image = pygame.transform.scale(bot_image,(30,30))
		self.image.set_colorkey(black)
		self.rect = self.image.get_rect()
		self.radius = 15
		#pygame.draw.circle(self.image, red,self.rect.center,self.radius)
		#to mkae them spawn above window
		self.rect.x = random.randrange(width - self.rect.width)
		self.rect.y = random.randrange(-100,-40)
		self.speedy = random.randrange(1,5)
		self.speedx = random.randrange(-3,3)

	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy	
		if self.rect.top > height or self.rect.left < -10 or self.rect.right > width:
			self.rect.x = random.randrange(width - self.rect.width)
			self.rect.y = random.randrange(-100,-40)
			self.speedy = random.randrange(1,5)			

class Bullet(pygame.sprite.Sprite):
	"""docstring for BU"""
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((10,10))
		self.image = bullet_image
		self.rect = self.image.get_rect()
		self.rect.bottom = y
		self.rect.centerx = x
		self.speedy = -10

	def update(self):
		self.rect.y += self.speedy
		#kill if it moves above window
		if self.rect.bottom < 0:
			self.kill()	

					

#loading Graphics
background = pygame.image.load("background.png").convert()
background_rect = background.get_rect()
player_image = pygame.image.load("player.png").convert()
player_mini_image = pygame.transform.scale(player_image,(20,20))
bot_image = pygame.image.load("enemyShip.png").convert()
bullet_image = pygame.image.load("laserRed.png").convert()

		

#loading sounds
shoot_sound = pygame.mixer.Sound("laser1.wav")
bot_explosion = pygame.mixer.Sound("explosion.wav")
#player_explosion = pygame.mixer.Sound("Chunky Explosion.mp3")
pygame.mixer.music.load("PetterTheSturgeon - GameJam simulator 2018.mp3") 
pygame.mixer.music.set_volume(0.8)

# all_sprites = pygame.sprite.Group()
# bots = pygame.sprite.Group() #group of all bots 
# bullets = pygame.sprite.Group()#group of bullets
# player = Player()
# all_sprites.add(player)	
# for i in range(8):
# 	bot = Bots()
# 	all_sprites.add(bot)
# 	bots.add(bot)
# score = 0


#play the music
pygame.mixer.music.play(loops = -1) #till we play

#Game Loop 
game_over = True
running = True
while running:
	if game_over:
		show_screen()
		all_sprites = pygame.sprite.Group()
		bots = pygame.sprite.Group() #group of all bots 
		bullets = pygame.sprite.Group()#group of bullets
		player = Player()
		all_sprites.add(player)	
		for i in range(difficulty):
			bot = Bots()
			all_sprites.add(bot)
			bots.add(bot)
		score = 0
		game_over = False
	#keep loop running at FPS
	clock.tick(FPS)
	#inputs
	for event in pygame.event.get():
		#closing window
		if event.type == pygame.QUIT:
			running = False
		#shooting	
		elif event.type == pygame.KEYDOWN:
			if event.key ==	pygame.K_SPACE:
				player.shoot()
	
	#update
	all_sprites.update()

	#bullet hitting bots
	hits_bots = pygame.sprite.groupcollide(bots,bullets,True,True,pygame.sprite.collide_circle)#bot hits bullet or other way around
	#to create new bots
	for hit in hits_bots:
		bot_explosion.play()
		bot = Bots()
		all_sprites.add(bot)
		bots.add(bot)
		score += 2
	#checking if player is hit
	hits_player = pygame.sprite.spritecollide(player,bots,False,pygame.sprite.collide_circle)#list
	if hits_player:
		bot_explosion.play()
		player.hide()
		player.lives -= 1
		difficulty -= -5
	if player.lives == 0:
		game_over = True	
	
	#drawing/ rendering
	screen.fill(black)
	screen.blit(background,background_rect)
	all_sprites.draw(screen)
	draw_text(screen,str(score),18,width/2,10)
	draw_lives(screen, width-100, 5 , player.lives, player_mini_image)
	
	#update after drawing
	pygame.display.update()

pygame.quit()


#AABB CBB PPC