# Learning-Pygame
Building a simple game using PyGame.
Space Shooter graphics by Kenney Vleugels (www.kenney.nl)
Thank you Kenney! 


#what is pygame

Pygame is what's called a game library which and the library is just a
collection of tools and these tools happen to be ones that are really
helpful for the common things you need to do when you're making games like
showing graphics on the screen and animating it playing sound and
controlling things using mouse or using the keyboard or a gamepad or whatever you're using for control.


#game Loop

The most important thing you need to know about a game or the most important piece
that goes into making a game at its heart is called the game loop. The game
loop is what makes the game happen. Every game at its heart has a game loop
running and in that game loop a certain number of things have to happen
every frame of the game, the first one is processing input that's also sometimes called events that just means
anything from outside of your game that happens and have the game respond to it, like a key getting pressed or the mouse getting clicked or a button on the gamepad getting pressed or whatever the case may
and the second step is updating the game, that means changing anything that
needs to change if a character on the screen needs to move,
need to figure out where it's supposed to move to and if two things run into each
other we need to figure out what was supposed to happen when they ran at each
other anything that has to change in your game since the last time you
updated it and then the last part is render. you can think of it as drawing that's used to
draw everything to the screen. after we've figured out what changed now we have to
draw that, if we figured out that the character moved to the right a certain
number of pixels well now we need to draw it that number of pixels to the right. 


#sprites

Sprite is a computer graphics term for just an object on the
screen that can move around. when you played Mario
everything you see on the screen is a sprite Mario's sprite
the coins are sprites the mushrooms are sprites so on, the sprites are super
useful in gaming because you often want to have a lot of different objects
moving around on the screen and Pygame has a lot of tools built into it that
makes it very easy to work with sprites.


#sprite groups

The update section is where we're going to tell each sprite or figure out what
each sprite needs to do. Does it need to move, does it need to animate, or what needs
to change about it and then obviously in the draw section we need to tell the
program to draw that sprite onto the screen. You can imagine if you start
having a whole lot of sprites on the screen ,that can start to get kind of
messy, your update section is going to be really long with drawing every sprite
and your draw section if you're gonna be really long with drawing every sprite.
So to solve that problem pygame has something called a sprite group and a
group is just a collection of sprites.So if you have a group it can make your
update and draw section a lot easier.

	all_sprites = pygame.sprite.Group()


	all_sprites.draw(screen)


#graphics

To make sure that we ahave sprites for each ovject we initialize them as follows
#loading Graphics
	background = pygame.image.load("background.png").convert()
	background_rect = background.get_rect()
	player_image = pygame.image.load("player.png").convert()
	bot_image = pygame.image.load("enemyShip.png").convert()
	bullet_image = pygame.image.load("laserRed.png").convert()
these will load the sprite so that we can easily use them in our code


#player class 

To create a player, or a new player we need to create a player class, and initialize it so that
everytime we call it, a new player object is created and the imitial attributes or qualities of 
the new player are assigned to it. pygame.sprite.Sprite.__init__(self) is a command that is always used inside 
a class so that sprites for it are set to initial. Every sprite must have a image and a rect attribute. image is what it looks like and rect is very useful to move it and other such features.
so to add a player,

	player = Player()
	all_sprites.add(player)


#rect
not done


#movement

Define a functioon inside the PLayer class called update, where movement of the object ( player ) can be done.
For movement, we can use rect.x or rext.y and change values so as to mak the sprite move. But to control these values we use button presses and clicks. For example, to move right, we may use the right button on keyboard to move the rect 5 pixels to the right as follows.

	if keystate[pygame.K_RIGHT]:
				self.speedx = 5	
	self.rect.x	+= self.speedx

this is written in the update function of PLayer class so that we can change the state or player or update the state of player everytime.
Explore more keystates and click and add new movement dimensions.


#enemy bots

To make the enemies, make a class called Bots and do the initialization as we did before for PLayer. This is same as all objects are treated the same in pygame. So the same features will be there for it except for on thing, that is the ability to control their movement. We must make them move in an haphazard manner or in a random fashion in every new game.
For the player, we mentioned where it will be placed in the screen as in we described the rect.x and rect.y for the player. In the enemy's case we need to make it appear somewhere random in the screen. we will choose a place above the screen so that it looks as though it appreas out of nowhere. so we use the random value to pick a point above the screen as follows.
and for speed as well, we randomise it so different bots travel at different speeds as follows.

	self.rect.x = random.randrange(width - self.rect.width)
	self.rect.y = random.randrange(-100,-40)
	self.speedy = random.randrange(1,5)
	self.speedx = random.randrange(-3,3) 

Noe by writing an update funtion for this class we can change the characteristics of the bot.

	def update(self):
			self.rect.x += self.speedx
			self.rect.y += self.speedy	
			if self.rect.top > height or self.rect.left < -10 or self.rect.right > width:
				self.rect.x = random.randrange(width - self.rect.width)
				self.rect.y = random.randrange(-100,-40)
				self.speedy = random.randrange(1,5)

the if statement makes sure that the bot goes back to the top when it reaches the bottom.

Now we need to make a sprite group for this as well, so we can update and draw in one go.
	
	bots = pygame.sprite.Group()
	for i in range(8):
	 	bot = Bots()
	 	all_sprites.add(bot)
	 	bots.add(bot)			

 The for loop is used beacause we need multiple enemies and not an individual bot.
 

 #collisions

 Pygame has a feature called spritecollide which lets us know is there is a collision between sprite and a group.

 	hits_player = pygame.sprite.spritecollide(player,bots,False)

 so we pass the groups between which we seek interaction. we pass the player sprite and bots group and false/true represents whether we delete the onejct or not. This return a list, so hits_player will be a list.
So using an 'if' over this lsi twe can control what happens in the game.
	
	if hits_player:
			bot_explosion.play()
			player.lives -= 1

This is just an exampe of what all can be done, such as reducing player life or puting a sound.


#bullets/ prjectiles

As always we need to make a class called Bullets and folow the same stes as before. this will have a smaller dimension, so keep that in mind.
Just like bots we need to spawn bullet somewhere, but only player can shoot so we will psawn it at player position and it will have a high speed too. So using these,

	class Bullet(pygame.sprite.Sprite):
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



In the player class, we need to add the ability for the player to shoot, so we make a function called shoot as follows,
	def shoot(self):
			bullet = Bullet(self.rect.centerx, self.rect.top)#bottom of bullet at top of player
			all_sprites.add(bullet)
			bullets.add(bullet)

		#remember that the self, points to player.

In the game loop we need to add one button (spacebar), so that we can shoot as follows,

	for event in pygame.event.get():
			#closing window
			if event.type == pygame.QUIT:
				running = False
			#shooting	
			elif event.type == pygame.KEYDOWN:
				if event.key ==	pygame.K_SPACE:
					player.shoot()

#for collisin between bullet and bots, we use the same method as before, but we use group collide as we have two groups bots and bullets

#bullet hitting bots
	hits_bots = pygame.sprite.groupcollide(bots,bullets,True,True) #true kills that object

As we need continuous generation of bots we use this,
	
	#to create new bots
	for hit in hits_bots:
		bot = Bots()
		all_sprites.add(bot)
		bots.add(bot)


#sound and music

To add sound effects and music pygame has mixer.sound and mixer.music respectively. and we write this together so as to avoid confusion.

#loading sounds
	shoot_sound = pygame.mixer.Sound("laser1.wav")
	bot_explosion = pygame.mixer.Sound("explosion.wav")
	pygame.mixer.music.load("PetterTheSturgeon - GameJam simulator 2018.mp3") 
	pygame.mixer.music.set_volume(0.8)

#play the music
pygame.mixer.music.play(loops = -1) #till we play the music keeps playing (-1 imdicates it will loop at the end of song)

#scoring

Outside loop and classes we need to write a fuction so as to display text, constraint for score will be killing bots, so we can do this in the code


	for hit in hits_bots:
		bot_explosion.play()
		bot = Bots()
		all_sprites.add(bot)
		bots.add(bot)
		score += 2

and the function will be as follows,

	def draw_text(surf, text, size, x,y):
		font = pygame.font.Font(font_name,size)
		text_surface = font.render(text,True, white) #true means the text can be antialiased or not
		text_rect = text_surface.get_rect()
		text_rect.midtop = (x,y)
		surf.blit(text_surface,text_rect)

and we call this funtion in the loop,

		#drawing/ rendering
	screen.fill(black)
	screen.blit(background,background_rect)
	all_sprites.draw(screen)
	draw_text(screen,str(score),18,width/2,10)			


#for game over screen

we write a funtion outsie of all loop and classes as follows,

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

this will be called after player dies,
we need to change the starting of the while loop as follows,

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
			for i in range(8):
				bot = Bots()
				all_sprites.add(bot)
				bots.add(bot)
			score = 0
			game_over = False