import pygame
import playerClass
import os

WIDTH = 800
HEIGHT = 500
img_folder = playerClass.img_folder
sceneAsset = pygame.image.load(os.path.join(img_folder, 'scene.png')).convert()


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
            player.image = playerClass.playerStand
            player.leftMove = False
            player.rightMove = False

    def moveRight(self, player, moveType):
        if not self.isEndScene(moveType):
            self.rect.x -= 5
            player.leftMove = False
            player.rightMove = True
            player.changePlayerFrame(False)
        else:
            player.image = playerClass.playerStand
            player.leftMove = False
            player.rightMove = False

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = sceneAsset
        self.rect = self.image.get_rect()
        self.sceneWidth = self.image.get_width()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
