import pygame
from src.Clases.playerClass import Player, playerStand
from src.Clases.sceneClass import Scene
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


pygame.init()
pygame.mixer.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ХЕРОТА v0.1.1.1")
clock = pygame.time.Clock()

scene = Scene()
player = Player()
# Добавление ассетов
all_sprites = pygame.sprite.Group()
all_sprites.add(scene)
all_sprites.add(player)


def drawWindow():
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
