import pygame
import random
import os
from math import degrees

# Окно
WIDTH = 800
HEIGHT = 500
FPS = 30

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Scene (pygame.sprite.Sprite):
    sceneWidth = 0

    def isEndScene(self, moveType):
        window_width = pygame.display.get_surface().get_width()
        if moveType == "left":
            if self.rect.x+5 >= 0:
                return True
        if moveType == "right":
            if self.rect.x-5 <= -(self.sceneWidth - window_width):
                return True
        return False

    def moveLeft(self, player, moveType):
        if not self.isEndScene(moveType):
            self.rect.x += 5
            player.leftMove = True
            player.rightMove = False
            player.changePlayerFrame(True)
        else:
            player.image = playerStand
            player.leftMove = False
            player.rightMove = False

    def moveRight(self, player, moveType):
        if not self.isEndScene(moveType):
            self.rect.x -= 5
            player.leftMove = False
            player.rightMove = True
            player.changePlayerFrame(False)
        else:
            player.image = playerStand
            player.leftMove = False
            player.rightMove = False

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = sceneAsset
        self.rect = self.image.get_rect()
        self.sceneWidth = self.image.get_width()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)


class Player(pygame.sprite.Sprite):
    frame = 0
    leftMove = False
    rightMove = True

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = playerStand
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, 320)

    def changePlayerFrame(self, rotate_img):
        self.frame += 1
        if self.frame == 3:
            self.frame = 0
        self.image = playerRunRight[self.frame]
        self.image.set_colorkey(BLACK)
        if rotate_img:
            self.image = pygame.transform.flip(self.image, True, False)

    def rotatePlayer(self):
        self.frame = 0
        if self.leftMove:
            self.image = pygame.transform.flip(self.image, True, False)
        elif self.rightMove:
            self.image = pygame.transform.flip(self.image, False, False)


pygame.init()
pygame.mixer.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ХЕРОТА v0.1.1")
clock = pygame.time.Clock()
# настройка папки ассетов
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'src/sprites')
playerRunRight = [pygame.image.load(os.path.join(img_folder, 'character_robot_run0.png')).convert(),
                  pygame.image.load(os.path.join(img_folder, 'character_robot_run1.png')).convert(),
                  pygame.image.load(os.path.join(img_folder, 'character_robot_run2.png')).convert()]
playerStand = pygame.image.load(os.path.join(img_folder, 'character_robot_idle.png')).convert()
sceneAsset = pygame.image.load(os.path.join(img_folder, 'scene.png')).convert()

scene = Scene()
player = Player()
# Добавление ассетов
all_sprites = pygame.sprite.Group()
all_sprites.add(scene)
all_sprites.add(player)


def drawWindow():
    # win.blit(sceneAsset, (0,0))
    all_sprites.update()
    all_sprites.draw(win)
    pygame.display.flip()


running = True
while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            player.image = playerStand
            player.leftMove = False
            player.rightMove = False

    allPressedKeys = pygame.key.get_pressed()
    if allPressedKeys[pygame.K_LEFT]:
        scene.moveLeft(player, "left")

    if allPressedKeys[pygame.K_RIGHT]:
        scene.moveRight(player, "right")

    drawWindow()

pygame.quit()
