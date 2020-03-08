import pygame
import pygametext

running = True

pygame.init()


screen = pygame.display.set_mode((640, 360))
clock = pygame.time.Clock()

pgt = pygametext.PGT(screen) # Define pygametext object.
layer = 0
def setLayer(x):
	global layer
	layer = x
	print("Current Layer:", layer)

pgt.button(10,10,100,50,(255,255,0),"Button",(0,0,0),pgt.none,None,0) # Add pgt Button
pgt.switch(120,10,100,50,(255,255,0),"Switch",(0,0,0),pgt.none,None,0) # Add pgt Switch
pgt.checkbox(10,70,20,(255,255,255),pgt.none,None,0) # Add pgt Switch
pgt.text(10,100,"Text",(255,0,0),40,0) # Add pgt Text
pgt.textbox(10,150,200,30,(0,0,0),0) # Add pgt Textbox
pgt.square(10,190,100,60,(0,0,255),0) # Add pgt Square
pgt.square(40,210,100,60,(0,255,0),0) # Add pgt Square
pgt.square(60,180,100,60,(255,0,0),0) # Add pgt Square

for element in pgt.getLayer(0):
	if type(element) == pgt.Textbox:
		element.text = "Textbox!"
		for char in element.text:
			element.chars.append(char)

def update(): # Update & Eventd
	global layer
	events = pygame.event.get()

	pgt.update(events, layer) # Update all pgt elements from layer 0. Takes events arg to process some elements.

	for event in events:
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			quit()

def draw():
	global layer
	screen.fill((255,255,255)) # Clear screen
	pgt.draw(layer) # Draw all pgt elements from layer 0
	
	pygame.display.flip()

while running:
	update()
	draw()
	clock.tick(60)