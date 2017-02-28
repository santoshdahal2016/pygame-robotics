# The tank game

import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (200, 200, 0)
green = (0, 155, 0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tanks")

clock = pygame.time.Clock()

FPS = 10

direction = "right"

smallfont = pygame.font.SysFont("arial", 25)
medfont = pygame.font.SysFont("arial", 50)
largefont = pygame.font.SysFont("arial", 80)

def pause():
	paused = True
	message_to_screen("Paused",
		black,
		-100,
		size="large")
	message_to_screen("Press C to continue or Q to continue.",
		black,
		25)
	pygame.display.update()
	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					paused = False

				elif event.key == pygame.K_q:
					pygame.quit()
					quit()

		# gameDisplay.fill(white)
		
		clock.tick(5)

def score(score):
	text = smallfont.render("Score: "+str(score), True, black)
	gameDisplay.blit(text, [0, 0])			

def game_intro():

	intro = True

	while intro:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					intro = False
				if event.key == pygame.K_q:
					pygame.quit()
					quit()

		gameDisplay.fill(white)
		message_to_screen("Welcome to Tanks!", 
			green,
			-100,
			"large")

		message_to_screen("The objective of the game is to shoot and destroy.",
			black,
			-30)
		message_to_screen("the enemy tank before they destroy you.",
			black,
			10)
		message_to_screen("The more enemies you destroy, the harder they get.",
			black,
			50)

		# message_to_screen("Press C to play, P to pause or Q to quit.",
		# 	black,
		# 	180)

		pygame.draw.rect(gameDisplay, green, (150, 500, 100, 50))
		pygame.draw.rect(gameDisplay, yellow, (350, 500, 100, 50))
		pygame.draw.rect(gameDisplay, red, (550, 500, 100, 50))

		text_to_button("play", black, 150, 500, 100, 50)
		text_to_button("controls", black, 350, 500, 100, 50)
		text_to_button("quit", black, 550, 500, 100, 50)

		pygame.display.update()
		clock.tick(15)

def text_objects(text, color, size):
	if size == "small":	
		textSurface = smallfont.render(text, True, color)
	elif size == "medium":
		textSurface = medfont.render(text, True, color)
	elif size == "large":
		textSurface = largefont.render(text, True, color)

	return textSurface, textSurface.get_rect()

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight,size = "small"):
	textSurface, textRect = text_objects(msg, color, size)
	textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
	gameDisplay.blit(textSurface, textRect)

def message_to_screen(msg, color, y_displace=0, size="small"):
	# screen_text = font.render(msg,True, color)
	# gameDisplay.blit(screen_text, [display_width/2, display_height/2])
	textSurface, textRect = text_objects(msg, color, size)
	textRect.center = display_width/2 , display_height/2 + y_displace
	gameDisplay.blit(textSurface, textRect)

# game loop
def gameLoop():
	global direction
	direction = "right"

	gameExit = False
	gameOver = False

	while not gameExit:

		if gameOver == True:
			message_to_screen("Game over.", red, y_displace=-50, size="large")
			message_to_screen("Press C to play again or Q to quit",
			black, y_displace=50, size="medium")
			pygame.display.update()

		while gameOver == True:
			# gameDisplay.fill(white)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit = True
					gameOver = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = False
					if event.key == pygame.K_c:
						gameLoop()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					pass
				elif event.key == pygame.K_RIGHT:
					pass
				elif event.key == pygame.K_UP:
					pass
				elif event.key == pygame.K_DOWN:
					pass
				elif event.key == pygame.K_p:
					pause()


		gameDisplay.fill(white)

		pygame.display.update()

		clock.tick(FPS)

	pygame.quit()
	quit()

game_intro()
gameLoop()