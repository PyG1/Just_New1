from Func import *


def men(time=60):
    screen = pygame.display.set_mode(display)
    pygame.display.set_caption('Pause')

    ing = skin('v_game')
    clos = skin('v_men')
    in_g = Button(410, 460, ing, 0.3)
    in_m = Button(240, 460, clos, 0.3)
    font = pygame.font.SysFont('Comic Sans MS', 40)
    name = font.render(stats('player'), True, (255, 80, 0))
    coins = font.render(stats('money') + '$', True, (255, 80, 0))
    tm = font.render(str(time), True, (255, 80, 0))
    m = 'Get to the portal' if stats('mission') == 'True' else 'Collect the key'
    mission = font.render(m, True, (255, 80, 0))
    run = True
    while run:
        menu_bg = skin('g_men')
        screen.blit(menu_bg, (0, 0))
        screen.blit(name, (420, 160))
        screen.blit(coins, (420, 210))
        screen.blit(tm, (385, 265))
        screen.blit(mission, (240, 365))
        if in_g.pressed(screen):
            if stats('sound') == 'On':
                button.play(0)
            run = False
        if in_m.pressed(screen):
            if stats('sound') == 'On':
                button.play(0)
            if stats('song') == 'On':
                pygame.mixer.pause()
                pygame.mixer.Sound.play(fon)
            return 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        pygame.display.update()