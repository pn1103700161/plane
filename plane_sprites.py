import pygame
import random

SCREEN_RECT = pygame.Rect(0,0,340,573)
CREATE_ENEMY_EVENT = pygame.USEREVENT
#hero子弹
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
    "精灵"
    def __init__(self,image_name,speed=1,speed1=1):
        #调用父类的初始化
        super().__init__()

        #对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.speed1 = speed1
    def update(self):
        self.rect.y += self.speed

        pass

class Background(GameSprite):

    def __init__(self,is_alt=False):
        super().__init__('./images/bg2.png')


    def update(self):
        #调用父类
        super().update()
        #
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = - self.rect.height
        pass


class Enemy(GameSprite):

    def __init__(self):
        # 调用父类，制定敌机
        super().__init__('./images/enemy.png')
        #随机速度
        self.speed = random.randint(1,3)
        #随机位置
        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)
        pass

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()
        pass

    def __del__(self):
        print("敌机挂了")


class Hero(GameSprite):

    def __init__(self):
        #1.调用父类方法设置 images&speed
        super().__init__('./images/plane1.png',0,0)

        #2.hero初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        #3.zidan
        self.bullet = pygame.sprite.Group()


    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

        self.rect.y += self.speed1
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > 489:
            self.rect.y = 489

    def fire(self):
        print("发射子弹")

        for i in (0,1,2):

        #1.创建子弹
            bullet = Bullet()

        #2.设置精灵位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx

        #3.精灵添加到精灵组
            self.bullet.add(bullet)


class Bullet(GameSprite):
    def __init__(self):
        super().__init__('./images/bullet.png',-3)
        pass

    def update(self):
        super().update()

        if self.rect.bottom < 0:
            self.kill()


    def __del__(self):
        print("子弹销毁")