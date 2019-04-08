import pygame
import time
from plane_sprites import *

pygame.init()

SCREEN_RECT = pygame.Rect(0,0,340,573)
    #1.创建窗口
screen = pygame.display.set_mode(SCREEN_RECT.size)
    #2 创建一个背景图片
bg = pygame.image.load('./images/bg2.png')
screen.blit(bg,(0,0))
pygame.display.update()

#创建飞机
hero = pygame.image.load('./images/plane1.png')
screen.blit(hero,(150,350))
pygame.display.update()

clock = pygame.time.Clock()

hero_rect = pygame.Rect(150,350,83,84)

#创建精灵
enemy = GameSprite('./images/bg2.png')
enemy1 =GameSprite('./images/bg2.png')
enemy_group = pygame.sprite.Group(enemy,enemy1)

#背景精灵
bg1 = Background('./images/enemy.png')
bg2 =Background('./images/enemy2.png',2)
bg2.rect.y = -bg2.rect.height
bg_group = pygame.sprite.Group(bg1,bg2)

i = 0
while True:
     #3 显示到屏幕
    clock.tick(60)

    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             print("退出游戏。。。")

    hero_rect.y -=1
     #判断飞机位置
    if hero_rect.y <= 0:
        hero_rect.y =573

    screen.blit(bg, (0, 0))
    screen.blit(hero,hero_rect)



    #精灵组调用
    enemy_group.update()
    enemy_group.draw(screen)
    #精灵背景
    bg_group.update()
    bg_group.draw(screen)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏。。。")
            pygame.quit()
            exit()
pass



