# pygametext
This Package adds UI Elements to PyGame.

## Install
pip install pygametext

## Import
`import pygametext`


## Initiate pygametext
`pgt = pygametext.PGT(screen)`


## Elements
`pgt.button(x,y,width,height,buttonColor,"Text",textColor,onClickFunction,onClickArguments,layer)`
-> Returns True

`pgt.switch(x,y,width,height,buttonColor,"Text",textColor,activeFunction,activeArguments,layer)`
-> Returns True

`pgt.checkbox(x,y,scale,color,activeFunction,activeArguments,layer)`
-> Returns True

`pgt.text(x,y,"Text",textColor,textSize,layer)`
-> Returns True

`pgt.textbox(x,y,width,height,textColor,layer)`
-> Returns True


## Process inputs and events
This function needs to be called if you want that the elements on specified layer to be interactive.
`pgt.update(layer)`

## Draw elements to screen
This function needs to be called if you want that the elements on specified layer to be drawn.
`pgt.draw(layer)`

## Utitilty functions
`pgt.getLayer(layer)`
-> Returns list of PGT Objects on specified Layer

`pgt.clear(id,layer)`
-> Returns True or False

`pgt.rebuild(layer)`
-> Returns True

``` python
import pygame
import pygametext

running = True

pygame.init()

screen = pygame.display.set_mode((640, 360))
clock = pygame.time.Clock()

pgt = pygametext.PGT(screen) # Define pygametext object.

pgt.button(10,10,100,50,(255,0,0),"Hello!",(0,0,0),print,"Hello World!",0) # Add pgt Button
pgt.button(120,10,100,50,(255,255,0),"Bye bye",(0,0,0),print,"Goodbye World!",0) # Add pgt Button
pgt.text(10,70,"Simple pygametext example.",(0,120,0),20,0) # Add pgt Text

def update(): # Update & Eventd
	events = pygame.event.get()

	pgt.update(events, 0) # Update all pgt elements from layer 0. Takes events arg to process some elements.

	for event in events:
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			quit()

def draw():
	screen.fill((255,255,255)) # Clear screen
	pgt.draw() # Draw all pgt elements from layer 0
	
	pygame.display.flip()

while running:
	update()
	draw()
	clock.tick(60)
```
