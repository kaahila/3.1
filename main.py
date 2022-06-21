import pygame
from classes import *

pygame.init()

# init game window
gameHight = 1000
gameWidth = 1000
screen = pygame.display.set_mode((gameHight, gameWidth))

# Titel and Icon
pygame.display.set_caption("Krasses Game")
icon = pygame.image.load("A.png")
pygame.display.set_icon(icon)


# Player
class Player:
    def __init__(self, x, y, playerImg, fahrzeug):
        self.x = x
        self.y = y
        self.xVelocity = 0
        self.yVelocity = 0
        self.img = playerImg
        self.x_direction = "right"
        self.y_direction = "down"
        self.decelerate_y = False;
        self.decelerate_x = False;
        self.accelerate_x = False;
        self.accelerate_y = False;
        self.directon_factor = {
            "right": 1,
            "left": -1,
            "up": -1,
            "down": 1
        }
        self.slow_factor = 0.8
        self.fahrzeug = fahrzeug
        self.speed = self.fahrzeug.get_ccm() * self.fahrzeug.get_power() / 100
        self.maxVelocity = self.fahrzeug.get_max_speed()

    def __move(self):
        global deltaTime
        # Check if player is decelerating
        if self.decelerate_x:
            self.__decelerateX()
        if self.decelerate_y:
            self.__decelerateY()
        if self.accelerate_x:
            self.__accelerateX()
        if self.accelerate_y:
            self.__accelerateY()
        # Move player
        tmp_x = self.x + self.xVelocity * self.directon_factor[self.x_direction] * (deltaTime / 1000)
        temp_y = self.y + self.yVelocity * self.directon_factor[self.y_direction] * (deltaTime / 1000)
        if 0 < tmp_x < gameWidth:
            self.x = tmp_x
        if 0 < temp_y < gameHight:
            self.y = temp_y

    def __accelerateX(self):
        self.decelerate_x = False
        self.accelerate_x = True
        if self.xVelocity <= self.maxVelocity - self.speed:
            self.xVelocity += self.speed

    def __accelerateY(self):
        self.decelerate_y = False
        self.accelerate_y = True
        if self.yVelocity <= self.maxVelocity - self.speed:
            self.yVelocity += self.speed

    def __decelerateX(self):
        self.decelerate_x = True
        self.accelerate_x = False
        if self.xVelocity > 1:
            self.xVelocity *= self.slow_factor
        else:
            self.xVelocity = 0

    def __decelerateY(self):
        self.decelerate_y = True
        if self.yVelocity > 1:
            self.yVelocity *= self.slow_factor
        else:
            self.yVelocity = 0

    def update(self):
        self.__move()
        screen.blit(self.img, (self.x, self.y))

    def setAccelerateX(self, accelerate_x, direction):
        self.accelerate_x = accelerate_x
        self.decelerate_x = not accelerate_x
        self.x_direction = direction

    def setAccelerateY(self, accelerate_y, direction):
        self.accelerate_y = accelerate_y
        self.decelerate_y = not accelerate_y
        self.y_direction = direction

    def setDecelerateX(self, decelerate_x):
        self.decelerate_x = decelerate_x
        self.accelerate_x = not decelerate_x

    def setDecelerateY(self, decelerate_y):
        self.decelerate_y = decelerate_y
        self.accelerate_y = not decelerate_y


playerImg = pygame.image.load("car.png")
fahrzeug = FamilyCar("ABC123", 1000, 0, 0, "red", True, "VW", "Golf", 100, 200, "Diesel", 10, 100, 4, 0.0, False)
player = Player(0, 0, playerImg, fahrzeug)

# Time
deltaTime = 0
clock = pygame.time.Clock()


def deltatime():
    global deltaTime
    deltaTime = clock.tick(60)


# Game Loop
running = True
while running:
    # Time
    deltatime()
    # RGB - Red - Green - Blue
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.setAccelerateX(True, "left")
            if event.key == pygame.K_RIGHT:
                player.setAccelerateX(True, "right")
            if event.key == pygame.K_UP:
                player.setAccelerateY(True, "up")
            if event.key == pygame.K_DOWN:
                player.setAccelerateY(True, "down")
        # if keystroke is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.setDecelerateX(True)
            if event.key == pygame.K_RIGHT:
                player.setDecelerateX(True)
            if event.key == pygame.K_UP:
                player.setDecelerateY(True)
            if event.key == pygame.K_DOWN:
                player.setDecelerateY(True)

    # Update Player
    player.update()

    pygame.display.update()
