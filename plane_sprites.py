import pygame

SCREEN_RECT = pygame.Rect(0,0,340,573)
class GameSprite(pygame.sprite.Sprite):
    "精灵"
    def __init__(self,image_name,speed=1):
        #调用父类的初始化
        super().__init__()

        #对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed =speed

    def update(self):
        self.rect.y += self.speed
        pass

class Background(GameSprite):
    def update(self):
        #调用父类
        super().update()
        #
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = - self.rect.height
        pass