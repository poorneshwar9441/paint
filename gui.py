import pygame
import sys
import random

#screen
class Screen:
	def __init__(self,width,height):
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width,self.height))
		self.screen.fill((255,255,255))
		pygame.display.update()



#each pixel
class Pixel:
	def __init__(self,height,width,x,y):
		self.height = height
		self.width = width 
		self.color =(255,255,255)
		self.x = x
		self.y = y

	def draw(self,screen):
		pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))

	def update_color(self,color):
		self.color = color


	def clear_pixel(self):
		self.color = (255,255,255)


	def is_on_pixel(self,x,y):
		if x>self.x and x<self.x+self.width:
			if y>self.y and y<self.y+self.width:
				return True

			else:
				return False

		else:
			return False


			
#used to create lines in the gui 
class Line:
	def __init__(self,x,y,X,Y):
		self.x = x
		self.y = y
		self.X = X
		self.Y = Y
		self.color = (0,0,0)

	def draw(self,screen):
		pygame.draw.line(screen,self.color,(self.x,self.y),(self.X,self.Y))



#used to creates buttons
class Tools:
	def __init__(self,color,x,y,w,h):
		self.color  = color 
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		


	def draw_button(self,screen):
		pygame.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))


	def is_on_button(self,x,y):
		if x>self.x and x<self.x+self.w:
			if y>self.y and y<self.y+self.h:
				return True

			else:
				return False

		else:
			return False




#main class 
class Main:
	def __init__(self):
		self.s = Screen(500,600)
		self.clear_button = Tools((255,255,0),120,520,50,30)
		self.eraser_button = Tools((255,255,0),180,520,50,30)

		self.red_button =  Tools((255,0,0),20,520,20,20)
		self.green_button = Tools((0,255,0),40,520,20,20)
		self.blue_button = Tools((0,0,255),60,520,20,20)

		self.yellow_button = Tools((255,255,0),20,540,20,20)
		self.brown_button = Tools((165,42,42),40,540,20,20)
		self.orange_button = Tools((255,140,0),60,540,20,20)

		self.pink_button = Tools((255,182,193),20,560,20,20)
		self.grey_button = Tools((128,128,128),40,560,20,20)
		self.violet_button = Tools((238,130,238),60,560,20,20)


		self.is_valid = True

	def grid_creator(self,height,width):
		l = []
		lines_hor = []
		lines_ver = []
		for i in range(0,500,5):
			for j in range(0,500,5):
				p = Pixel(5,5,j,i)
				l.append(p)

		for i in range(0,505,5):
			lob = Line(i,0,i,500)
			lines_ver.append(lob)

		for i in range(0,505,5):
			lob = Line(0,i,500,i)
			lines_hor.append(lob)
			

		return [l,lines_hor,lines_ver]




	def welocome_screen(self):		
		self.s.screen.fill((255,255,255))
		while(True):

			for e in pygame.event.get():
				if(e.type == pygame.QUIT):
					pygame.quit()
					sys.exit()
					
			pygame.draw.rect(self.s.screen,(255,0,0),(250,250,50,30))
			pygame.display.update()

			x = pygame.mouse.get_pos()[0]
			y = pygame.mouse.get_pos()[1]

			if(x>250 and x<300):
				if(y>250 and y<270):
					k = True
					

				else:
					k = False				

			else:
				k = False


			if(k and pygame.mouse.get_pressed()[0]):
				break;


	def main_game_loop(self):
		pygame.init()
		l1 = self.grid_creator(5,5)[0]
		l2 = self.grid_creator(5,5)[1]
		l3 = self.grid_creator(5,5)[2]
		color = (255,0,0)
		variable = 0
		self.welocome_screen()
		while True:
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			

			for i in l1:
				y =i.is_on_pixel(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
				if(y and (pygame.mouse.get_pressed()[0])):
					i.update_color(color)
				i.draw(self.s.screen)

			for i in l2:
				i.draw(self.s.screen)

			for i in l3:
				i.draw(self.s.screen)




			self.clear_button.draw_button(self.s.screen)
			k = self.clear_button.is_on_button(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])

			if(k and pygame.mouse.get_pressed()[0]):
				for i in l1:
					i.clear_pixel()


			self.eraser_button.draw_button(self.s.screen)
			h = self.eraser_button.is_on_button(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])

			if(h and pygame.mouse.get_pressed()[0]):
				color = (255,255,255)


			self.red_button.draw_button(self.s.screen)
			m = self.red_button.is_on_button(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])

			if(m and pygame.mouse.get_pressed()[0]):
				color = self.red_button.color


			self.green_button.draw_button(self.s.screen)
			n = self.green_button.is_on_button(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
			if(n  and pygame.mouse.get_pressed()[0]):
				color = (0,255,0)


			self.blue_button.draw_button(self.s.screen)
			n1 = self.blue_button.is_on_button(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
			if(n1 and pygame.mouse.get_pressed()[0]):
				color = (0,0,255)


			self.yellow_button.draw_button(self.s.screen)
			n2 = self.yellow_button.is_on_button(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
			if(n2 and pygame.mouse.get_pressed()[0]):
				color = self.yellow_button.color


			self.brown_button.draw_button(self.s.screen)
			n3 = self.brown_button.is_on_button(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
			if(n3 and pygame.mouse.get_pressed()[0]):
				color = self.brown_button.color


			self.orange_button.draw_button(self.s.screen)
			n4  = self.orange_button.is_on_button(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
			if(n4 and pygame.mouse.get_pressed()[0]):
				color = self.orange_button.color


			self.pink_button.draw_button(self.s.screen)
			n5 = self.pink_button.is_on_button(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
			if(n5 and pygame.mouse.get_pressed()[0]):
				color = self.pink_button.color

			self.grey_button.draw_button(self.s.screen)
			n6 = self.grey_button.is_on_button(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
			if(n6 and pygame.mouse.get_pressed()[0]):
				color = self.grey_button.color


			self.violet_button.draw_button(self.s.screen)
			n7 = self.violet_button.is_on_button(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
			if(n7 and pygame.mouse.get_pressed()[0]):
				color = self.violet_button.color

			pygame.display.update()


m  = Main()
m.main_game_loop()











		