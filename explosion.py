import pygame

snd_dir = 'media/snd/'  # Путь до папки со звуками
img_dir = 'media/img/'  # Путь до папки со спрайтами
width = 1366                            # ширина игрового окна
height = 768                            # высота игрового окна

# Создаем класс игрока
class Explosion(pygame.sprite.Sprite):
   def __init__(self):  # Специальная функция, где указываем что будет у игрока
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(img_dir + 'explosion/0.png')
       self.rect = self.image.get_rect()

