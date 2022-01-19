from Func import *
from map import levels
from set import settings
from shop import magaz

screen = pygame.display.set_mode(display)
pygame.display.set_caption('Labirint')

play_img = skin('play_b')
shop_img = skin('shop_b')
set_img = skin('set_b')
exit_img = skin('exit_b')

play_b = Button(250, 330, play_img, 0.6)
shop_b = Button(10, 310, shop_img, 0.4)
set_b = Button(590, 310, set_img, 0.4)
exit_b = Button(10, 530, exit_img, 0.3)

run = True
if stats('song') == 'On':
    pygame.mixer.Sound.play(fon)
while run:
    menu_bg = skin('fon')
    screen.blit(menu_bg, (0, 0))
    if shop_b.pressed(screen):
        if stats('sound') == 'On':
            button.play(0)
            flag = True
        magaz()
    if play_b.pressed(screen):
        if stats('sound') == 'On':
            button.play(0)
            flag = True
        levels()
    if set_b.pressed(screen):
        if stats('sound') == 'On':
            button.play(0)
            flag = True
        settings()
    if exit_b.pressed(screen):
        run = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()