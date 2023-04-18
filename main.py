import pygame
from player import Player
from enemy_right import EnemyRight
from enemy_bottom import EnemyBottom
from enemy_top import EnemyTop
from enemy_left import EnemyLeft
from bullet import Bullet
pygame.init()

snd_dir = 'media/snd/'
img_dir = 'media/img/'


width = 1366
height = 768
fps = 30
game_name = "Shooter"

icon = pygame.image.load(img_dir + 'icon.png')
pygame.display.set_icon(icon)

# Цвета
BLACK = "#000000"
WHITE = "#FFFFFF"
RED = "#FF0000"
GREEN = "#008000"
BLUE = "#0000FF"
CYAN = "#00FFFF"

#Создаем игровой экран
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(game_name)

def get_hit_sprite(hits_dict):
    for hit in hits_dict.values():
        return hit[0]



timer = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
mobs_sprites = pygame.sprite.Group()
bullets_sprites = pygame.sprite.Group()
players_sprites = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

enemy_right = EnemyRight()
all_sprites.add(enemy_right)

enemy_bottom = EnemyBottom()
all_sprites.add(enemy_bottom)

enemy_top = EnemyTop()
all_sprites.add(enemy_top)

enemy_left = EnemyLeft()
all_sprites.add(enemy_left)
all_sprites.add(player)                 # Добавляем игрока в группу спрайтов
players_sprites.add(player)             # Добавляем игрока в группу игроков
all_sprites.add([enemy_left, enemy_right, enemy_top, enemy_bottom])  # В группу всем
mobs_sprites.add([enemy_left, enemy_right, enemy_top, enemy_bottom])

#for i in range(4):
 #   enemy_right = EnemyRight()
  #  all_sprites.add(enemy_right)

run = True

while run:
    timer.tick(fps)
    all_sprites.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.snd_shoot.play()
                bullet = Bullet(player)
                all_sprites.add(bullet)
                bullets_sprites.add(bullet)

    shots = pygame.sprite.groupcollide(bullets_sprites, mobs_sprites, True, True)
    scratch = pygame.sprite.groupcollide(mobs_sprites, players_sprites, False, False)
    if scratch:
        sprite = get_hit_sprite(scratch)
        sprite.snd_scratch.play()
    screen.fill(CYAN)
    all_sprites.draw(screen)
    pygame.display.update()
pygame.quit()
