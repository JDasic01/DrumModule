import pygame

class Pad(pygame.sprite.Sprite):
	def __init__(self,type):
		super().__init__()
		
		if type == 'snare':
			snare = pygame.image.load('').convert_alpha()
			self.frames = [snare]
			y_pos  = 300
		elif type == 'tom':
			tom = pygame.image.load('').convert_alpha()
			self.frames = [tom]
			y_pos  = 300
		elif type == 'bass':
			bass = pygame.image.load('').convert_alpha()
			self.frames = [bass]
			y_pos  = 300
		else:
			cymbal = pygame.image.load('').convert_alpha()
			self.frames = [cymbal]
			y_pos  = 300


pygame.init()
screen = pygame.display.set_mode((875,760))
pygame.display.set_caption('DrumModule')
clock = pygame.time.Clock()

background_surface = pygame.image.load('assets\drum_kit.png').convert()
background_rect = background_surface.get_rect(center = (437, 380))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()		
		else:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				game_active = True
				start_time = int(pygame.time.get_ticks() / 1000)

	screen.blit(background_surface, background_rect)

	pygame.display.update()
	clock.tick(60)