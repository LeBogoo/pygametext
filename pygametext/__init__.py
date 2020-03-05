import pygame as pg
pg.font.init()

class NoElementToDelete(Exception):
	pass

class PGT:
	def none(x):
		pass

	def __init__(self,screen):
		print("Hello from pygametext!")
		self.screen = screen
		self.layers = []
		self.lastID = 0
		for i in range(0,101):
			self.layers.append([])
#		(x,y,width,height,color,text,action,layer)
	def square(self,x,y,w,h,c,l = 0):
		sqr = PGT.Square(self.screen,x,y,w,h,c,self.lastID)
		self.layers[l].append(sqr)
		self.lastID += 1

	def text(self,x,y,t,tc,ts=14,l = 0):
		txt = PGT.Text(self.screen,x,y,t,tc,ts,self.lastID)
		self.layers[l].append(txt)
		self.lastID += 1

	def button(self,x,y,w,h,c,t,tc,a,p,l = 0):
		btn = PGT.Button(self.screen,x,y,w,h,c,t,tc,a,p,self.lastID)
		self.layers[l].append(btn)
		self.lastID += 1

	def switch(self,x,y,w,h,c,t,tc,a,p,l = 0):
		sw = PGT.Switch(self.screen,x,y,w,h,c,t,tc,a,p,self.lastID)
		self.layers[l].append(sw)
		self.lastID += 1

	def checkbox(self,x,y,s,c,a,p,l = 0):
		cb = PGT.Checkbox(self.screen,x,y,s,c,a,p,self.lastID)
		self.layers[l].append(cb)
		self.lastID += 1

	def textbox(self,x,y,w,h,tc, l = 0):
		txtBx = PGT.Textbox(self.screen,x,y,w,h,tc,self.lastID)
		self.layers[l].append(txtBx)
		self.lastID += 1

	def update(self, events, layer = 0):
		for element in self.layers[layer]:
			element.update(events)

	def draw(self,layer = 0):
		for element in self.layers[layer]:
			element.draw()

	def getLayer(self,layer=0):
		return self.layers[layer]

	def clear(self,id=-1,layer=0):
		if id == -1:
			self.layers[layer] = []
		else:
			print(len(self.layers[layer]))
			if id < len(self.layers[layer]):
				self.layers[layer][id] = self.Empty(id)
			else:
				raise NoElementToDelete("You tried to delete id '{}', but it doesn't exist. Did you tried to call 'PGT.rebuild()'?".format(id))
				# raise NoElementToDelete("There is no element left to delete! Please make sure to call 'PGT.rebuild()' to regenerate your IDs!")

	
	def rebuild(self,layer=0):
		newLayer = []
		for element in self.layers[layer]:
			if type(element) != self.Empty:
				newLayer.append(element)
		self.layers[layer] = newLayer
			
	class Empty():
		def __init__(self, i):
			self.id = i	
			self.active = False
		def update(self,events):
			pass
		def draw(self):
			pass


	class Square():
		def __init__(self,screen,x,y,w,h,c,i):
			self.screen = screen
			self.x = x
			self.y = y
			self.w = w
			self.h = h
			self.c = c
			self.id = i
			self.active = False

		def update(self,events):
			pass

		def draw(self):
			square = pg.Surface((self.w,self.h)).convert_alpha()
			square.fill(self.c)
			self.screen.blit(square, (self.x,self.y))
				

	class Button():
		def __init__(self,screen,x,y,w,h,c,t,tc,a,p,i):
			self.screen = screen
			self.font = pg.font.SysFont('Arial', 14)
			self.x = x
			self.y = y
			self.w = w
			self.h = h
			self.c = c
			self.t = t
			self.tc = tc
			self.a = a
			self.p = p
			self.id = i
			self.hovering = False
			self.press_decay = 0
			self.active = False

		def update(self,events):
			mp = pg.mouse.get_pos()
			self.hovering = False
			if mp[0] >= self.x and mp[0] <= self.x + self.w and mp[1] >= self.y and mp[1] <= self.y + self.h:
				self.hovering = True


			self.active = False
			if self.hovering:
				if pg.mouse.get_pressed()[0]:
					self.active = True
					if self.press_decay == 0:
						self.a(self.p)			
					self.press_decay += 1
					if self.press_decay == 10000:
						self.press_decay = 0
				else:
					self.press_decay = 0


		def draw(self):
			btnSurf = pg.Surface((self.w,self.h)).convert_alpha()
			color1 = pg.Surface((self.w,self.h)).convert_alpha()
			outline = pg.Surface((self.w-1,self.h-1)).convert_alpha()
			outline2 = pg.Surface((self.w,self.h)).convert_alpha()
			color2 = pg.Surface((self.w-3,self.h-3)).convert_alpha()
			color1.fill((self.c[0],self.c[1],self.c[2],255))
			color2.fill((self.c[0],self.c[1],self.c[2],255))

			outline.fill((0,0,0,50))
			outline2.fill((0,0,0,50))

			btnSurf.blit(color1,(0,0))
			btnSurf.blit(outline,(0,0))
			btnSurf.blit(outline2,(0,0))
			btnSurf.blit(color2,(1,1))

			if self.active:
				act = pg.Surface((self.w,self.h)).convert_alpha()
				act.fill((0,0,0,100))
				btnSurf.blit(act, (0,0))
			elif self.hovering:
				hov = pg.Surface((self.w,self.h)).convert_alpha()
				hov.fill((255,255,255,50))
				btnSurf.blit(hov, (0,0))

			text = self.font.render(self.t, True, self.tc)
			textCoords = ((btnSurf.get_width()/2)-text.get_width()/2,(btnSurf.get_height()/2)-text.get_height()/2,)
			btnSurf.blit(text, textCoords)
			self.screen.blit(btnSurf, (self.x,self.y))
				

	class Switch():
		def __init__(self,screen,x,y,w,h,c,t,tc,a,p,i):
			self.screen = screen
			self.font = pg.font.SysFont('Arial', 14)
			self.x = x
			self.y = y
			self.w = w
			self.h = h
			self.c = c
			self.t = t
			self.tc = tc
			self.a = a
			self.p = p
			self.id = i
			self.hovering = False
			self.press_decay = 0
			self.active = False

		def update(self,events):
			mp = pg.mouse.get_pos()
			self.hovering = False
			if mp[0] >= self.x and mp[0] <= self.x + self.w and mp[1] >= self.y and mp[1] <= self.y + self.h:
				self.hovering = True


			if self.hovering:
				if pg.mouse.get_pressed()[0]:
					if self.press_decay == 0:
						if self.active:
							self.active = False
							self.press_decay += 1
						else:
							self.active = True
							self.press_decay += 1
				else:
					self.press_decay = 0

			if self.active:
				self.a(self.p)

		def draw(self):
			btnSurf = pg.Surface((self.w,self.h)).convert_alpha()
			color1 = pg.Surface((self.w,self.h)).convert_alpha()
			outline = pg.Surface((self.w-1,self.h-1)).convert_alpha()
			outline2 = pg.Surface((self.w,self.h)).convert_alpha()
			color2 = pg.Surface((self.w-3,self.h-3)).convert_alpha()
			color1.fill((self.c[0],self.c[1],self.c[2],255))
			color2.fill((self.c[0],self.c[1],self.c[2],255))

			outline.fill((0,0,0,50))
			outline2.fill((0,0,0,50))

			btnSurf.blit(color1,(0,0))
			btnSurf.blit(outline,(0,0))
			btnSurf.blit(outline2,(0,0))
			btnSurf.blit(color2,(1,1))

			if self.active:
				act = pg.Surface((self.w,self.h)).convert_alpha()
				act.fill((0,0,0,100))
				btnSurf.blit(act, (0,0))
			elif self.hovering:
				hov = pg.Surface((self.w,self.h)).convert_alpha()
				hov.fill((255,255,255,50))
				btnSurf.blit(hov, (0,0))

			text = self.font.render(self.t, True, self.tc)
			textCoords = ((btnSurf.get_width()/2)-text.get_width()/2,(btnSurf.get_height()/2)-text.get_height()/2,)
			btnSurf.blit(text, textCoords)
			self.screen.blit(btnSurf, (self.x,self.y))

	class Checkbox():
		def __init__(self,screen,x,y,s,c,a,p,i):
			self.screen = screen
			self.font = pg.font.SysFont('Arial', 14)
			self.x = x
			self.y = y
			self.s = s
			self.w = self.s
			self.h = self.s
			self.c = c
			self.a = a
			self.p = p
			self.id = i
			self.hovering = False
			self.press_decay = 0
			self.active = False

		def update(self,events):
			mp = pg.mouse.get_pos()
			self.hovering = False
			if mp[0] >= self.x and mp[0] <= self.x + self.w and mp[1] >= self.y and mp[1] <= self.y + self.h:
				self.hovering = True


			if self.hovering:
				if pg.mouse.get_pressed()[0]:
					if self.press_decay == 0:
						if self.active:
							self.active = False
							self.press_decay += 1
						else:
							self.active = True
							self.press_decay += 1
				else:
					self.press_decay = 0

			if self.active:
				self.a(self.p)

		def draw(self):
			innerSize = self.w * 0.7
			innerPos = (self.s - innerSize) / 2

			cbBaseColor = pg.Surface((self.s,self.s)).convert_alpha()
			cbColor = pg.Surface((self.s-3,self.s-3)).convert_alpha()
			cbOutline1 = pg.Surface((self.s,self.s)).convert_alpha()
			cbOutline2 = pg.Surface((self.s-1,self.s-1)).convert_alpha()
			cbInner = pg.Surface((innerSize,innerSize)).convert_alpha()

			cbInner.fill((0,0,0,120))
			cbOutline1.fill((0,0,0,50))
			cbOutline2.fill((0,0,0,50))
			cbBaseColor.fill((self.c[0],self.c[1],self.c[2],255))
			cbColor.fill((self.c[0],self.c[1],self.c[2],255))
					
			cbBaseColor.blit(cbOutline1,(0,0))
			cbBaseColor.blit(cbOutline2,(0,0))
			cbBaseColor.blit(cbColor,(1,1))
			cbBaseColor.blit(cbInner,(innerPos,innerPos))

			if self.active:
				act = pg.Surface((innerSize,innerSize)).convert_alpha()
				act.fill((0,0,0,100))
				cbBaseColor.blit(act, (innerPos,innerPos))
				
			elif self.hovering:
				hov = pg.Surface((self.s,self.s)).convert_alpha()
				hov.fill((255,255,255,30))
				cbBaseColor.blit(hov, (0,0))
			
			self.screen.blit(cbBaseColor, (self.x,self.y))
				

	class Text():
		def __init__(self,screen,x,y,t,tc,ts,i):
			self.screen = screen
			self.font = pg.font.SysFont('Arial', ts)
			self.x = x
			self.y = y
			self.t = t
			self.tc = tc
			self.id = i
			self.active = False

		def update(self,events):
			pass

		def draw(self):
			text = self.font.render(self.t, True, self.tc)
			self.screen.blit(text, (self.x,self.y))

	class Textbox():
		def __init__(self,screen,x,y,w,h,tc,i):
			self.blinkEvent = pg.USEREVENT + 1
			self.timer = pg.time.set_timer(self.blinkEvent,1000)
			self.screen = screen
			self.font = pg.font.SysFont('Arial', h-6)
			self.x = x
			self.y = y
			self.w = w
			self.h = h
			self.tc = tc
			self.id = i
			self.active = False
			self.cooldown = 0
			self.blinker = True
			self.validChars = [' ', '!', '"', '$', '%', '&', '(', ')', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '>', '?', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', ']', '{', '}','\\', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '©', 'Ä', 'Ü', 'ß', 'à', 'ä', 'è', 'é', 'ö', 'ü', '–', '’', '“', '„']

			# Internal Textbox vars
			self.textboxChars = []
			self.textboxText = ""
			self.history = []

		def update(self,events):
			global textboxString

			mp = pg.mouse.get_pos()
			if mp[0] >= self.x and mp[0] <= self.x + self.w and mp[1] >= self.y and mp[1] <= self.y + self.h:
				if pg.mouse.get_pressed()[0] and self.cooldown == 0:
					self.active = True
					self.cooldown = 1
			else:
				if pg.mouse.get_pressed()[0] and self.cooldown == 0:
					self.active = False
					self.cooldown = 1
			if pg.mouse.get_pressed()[0] == 0:
				self.cooldown = 0


			for event in events:
				if self.active:
					if event.type == pg.KEYDOWN:
						if event.key == pg.K_BACKSPACE:
							if len(self.textboxChars) != 0:
								del self.textboxChars[-1]
							self.textboxText = ""
							for char in self.textboxChars:
								self.textboxText += char
						elif event.key == pg.K_RETURN:
							self.history.append(self.textboxText)
							self.textboxText = ""
							del self.textboxChars[:]
							print(self.history)
						else:
							if event.unicode in self.validChars:
								self.textboxChars.append(event.unicode)
								self.textboxText = ""
								for char in self.textboxChars:
									self.textboxText += char
					elif  event.type == 25:
						if self.blinker:
							self.blinker = False
						else:
							self.blinker = True

		def draw(self):
			if self.w <= 10:
				self.w = 10
			if self.h <= 10:
				self.h = 10
			text = self.font.render(self.textboxText, True, self.tc)
			base = pg.Surface((self.w,self.h)).convert_alpha()
			boarder1 = pg.Surface((self.w - 1, self.h - 1)).convert_alpha()
			boarder2 = pg.Surface((self.w - 2, self.h - 2)).convert_alpha()
			textbox = pg.Surface((self.w-3,self.h-3)).convert_alpha()
			cursor = pg.Surface((2,self.h - 4)).convert_alpha()
			
			base.fill((255,255,255))
			textbox.fill((255,255,255))
			boarder1.fill((0,0,0,50))
			boarder2.fill((0,0,0,50))
			if self.active:
				if self.blinker:
					cursor.fill((0,0,0,200))
				else:
					cursor.fill((0,0,0,0))
			else:
				cursor.fill((0,0,0,0))

			base.blit(boarder1,(0,0))
			base.blit(boarder2,(1,1))


			text = self.font.render(self.textboxText, True, self.tc)
			textbox.blit(text, (1,0))

			base.blit(textbox,(2,2))
			base.blit(cursor, (text.get_width() + 4, 2))
			self.screen.blit(base, (self.x,self.y))