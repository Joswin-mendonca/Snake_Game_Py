from pygame.locals import * #Loading PyGame module
import pygame
import time
from random import randint #importing 'random' module
class Player: #to make dynamic positions
    x = 0
    y = 0
    d = 0 #Direction variable
    positions = [] #To store the old positions
    length = 4 #To give the starting length of the object
class Apple: #for the apple positions
    a = 0
    b = 0
class Game: #Creating class 'Game' 
    game_width = 10 #Width of the game
    game_height = 10 #Height of the game
    grid_size = 44 #Size of the grid
    def isCollision(self,a1,b1,a2,b2,bsize): #To check collision between snake and the apple
        if a1 >= a2 and a1 <= a2 + bsize:
            if b1 >= b2 and b1 <= b2 + bsize:
                return True
        return False
    def __init__(self):
        self._running = True #Set variable 'running' to True
        self.player = Player() #Creates new player object from class 'Player'
        self.apple = Apple() #Creates new apple object from class 'Apple'
        self.apple.a = randint(0,self.game_width) * self.grid_size #horizontal position of apple
        self.apple.b = randint(0,self.game_height) * self.grid_size #vertical position of apple
    def on_init(self):
        pygame.init() #Initializing PyGame
        self._display_surf = pygame.display.set_mode((640,480), pygame.HWSURFACE) #Creating window and mentioning it's width and height||HWSURFACE=hardware accelerated surfaces
        pygame.display.set_caption('PyGame example') #Setting window title
        self._snake_image = pygame.image.load("snaku.png").convert() #loading image
        self._apple_image = pygame.image.load("apple.png").convert()
        self.name_font = pygame.font.SysFont('Bradley Hand ITC',30) #initializing font type
    def on_render(self):
        self._display_surf.fill((0,0,0)) #Clears the screen (R,G,B) values
        for pos in self.player.positions:
            self._display_surf.blit(self._snake_image,(pos[0], pos[1])) #draw the image using 'blit' and specify the image and it's positions(horizontal,vertical)
        self._display_surf.blit(self._apple_image,(self.apple.a,self.apple.b))
        name = self.name_font.render("~Joswin_Mendonca",True,(255,255,55))
        self._display_surf.blit(name,(380,440))
        pygame.display.flip() #Update the screen
    def on_cleanup(self):
        pygame.quit() #Quit function
    def on_execute(self): #Actual loop
        if self.on_init() == False:
            self._running = False
        while self._running:
            for event in pygame.event.get(): #Act based on user input/event(move,close,etc..)
                if event.type == pygame.QUIT: #For Quitting the window
                    self._running = False 
            keys=pygame.key.get_pressed() #fetching keyboard inputs
            if keys[K_RIGHT]: #To move Right
                self.player.d = 0
            if keys[K_LEFT]: #To move Left
                self.player.d = 1
            if keys[K_UP]: #To move Up
                self.player.d = 2
            if keys[K_DOWN]: #To move Down
                self.player.d = 3
            if self.player.d == 0: #Moves in the right direction continuously
                print('You clicked Right')
                self.player.x += 44
            elif self.player.d == 1: #Moves in the left direction continuously
                print('You clicked Left')
                self.player.x -= 44
            elif self.player.d == 2: #Moves in the up direction continuously
                print('You clicked Up')
                self.player.y -= 44
            elif self.player.d == 3: #Moves in the down direction continuously
                print('You clicked Down')
                self.player.y += 44
            if len(self.player.positions) < self.player.length:
                self.player.positions.append((self.player.x,self.player.y)) #To store the previous position into the variable
            else:
                self.player.positions.pop(0) #Removes the oldest positions
                self.player.positions.append((self.player.x,self.player.y))
            if self.isCollision(self.player.x,self.player.y,self.apple.a,self.apple.b,44): #To check the collisions
                print('Collides')
                self.apple.a = randint(0,self.game_width) * self.grid_size
                self.apple.b = randint(0,self.game_height) * self.grid_size
                self.player.length += 1
            if len(self.player.positions) > self.player.length-1:
                for i in range(0,self.player.length-1):
                    #print(f"{self.player.positions[i][0]},{self.player.positions[i][1]} {self.player.x},{self.player.y}")
                    if self.isCollision(self.player.x,self.player.y,self.player.positions[i][0],self.player.positions[i][1],40):
                        print('GAME OVER!!')
                        exit()
            self.on_render() #Repeatedly Clears and updates the screen
            time.sleep(0.25) #To move the image in a particular speed
        self.on_cleanup()
if __name__ == "__main__":
    game = Game() 
    game.on_execute()