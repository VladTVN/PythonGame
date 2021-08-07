import pygame
import os

WIDTH = 800
HEIGHT = 500
BLACK = (0, 0, 0)
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'src/sprites')
playerRunRight = [pygame.image.load(os.path.join(img_folder, 'character_robot_run0.png')).convert(),
                  pygame.image.load(os.path.join(img_folder, 'character_robot_run1.png')).convert(),
                  pygame.image.load(os.path.join(img_folder, 'character_robot_run2.png')).convert()]
playerStand = pygame.image.load(os.path.join(img_folder, 'character_robot_idle.png')).convert()


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



