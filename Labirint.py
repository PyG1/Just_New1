from maze_generator import *
import pygame


class Portal:
    def __init__(self):
        self.img = pygame.image.load('data/portal.jpg').convert_alpha()
        self.img = pygame.transform.scale(self.img, (TILE - 10, TILE - 10))
        self.rect = self.img.get_rect()
        self.set_pos()

    def set_pos(self):
        self.rect.topleft = randrange(cols) * TILE + 5, randrange(rows) * TILE + 5

    def draw(self):
        game_surface.blit(self.img, self.rect)


def is_collide(x, y):
    tmp_rect = player_rect.move(x, y)
    if tmp_rect.collidelist(walls_collide_list) == -1:
        return False
    return True


def claim_portal():
    for portal in portal_list:
        if player_rect.collidepoint(portal.rect.center):
            portal.set_pos()
            return True
    return False


def is_game_over():
    global time, portals, FPS, maze, walls_collide_list
    if time < 0 or portals == 1:
        maze = generate_maze()
        walls_collide_list = sum([cell.get_rects() for cell in maze], [])
        player_rect.center = TILE // 2, TILE // 2
        [portal.set_pos() for portal in portal_list]
        time, portals, FPS = 60, 0, 50


FPS = 50
pygame.init()
game_surface = pygame.Surface(RES)
surface = pygame.display.set_mode((WIDTH + 300, HEIGHT))
clock = pygame.time.Clock()

bg_game = pygame.image.load('data/bg_1.jpg').convert()
bg = pygame.image.load('data/bg_main.jpg').convert()

maze = generate_maze()

STEP = 4
player_img = pygame.image.load('data/0.png').convert_alpha()
player_img = pygame.transform.scale(player_img, (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))
player_rect = player_img.get_rect()
player_rect.center = TILE // 2, TILE // 2
directions = {'a': (-STEP, 0), 'd': (STEP, 0), 'w': (0, -STEP), 's': (0, STEP)}
keys = {'a': pygame.K_a, 'd': pygame.K_d, 'w': pygame.K_w, 's': pygame.K_s}
direction = (0, 0)

portal_list = [Portal() for i in range(1)]

walls_collide_list = sum([cell.get_rects() for cell in maze], [])

image1 = pygame.transform.scale(pygame.image.load('data/0.png').convert_alpha(),
                                (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))
image2 = pygame.transform.scale(pygame.image.load('data/1.png').convert_alpha(),
                                (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))
image3 = pygame.transform.scale(pygame.image.load('data/2.png').convert_alpha(),
                                (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))
image4 = pygame.transform.scale(pygame.image.load('data/3.png').convert_alpha(),
                                (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))

pygame.time.set_timer(pygame.USEREVENT, 1000)
time = 60
portals = 0

font = pygame.font.SysFont('Impact', 150)
font1 = pygame.font.SysFont('Impact', 50)
text_font = pygame.font.SysFont('Impact', 80)


def show_menu():
    # import pygame_menu
    menu_bg = pygame.image.load('data/fon.jpg')
    # start_btn = Button(100, 70)
    # skins_btn = Button(50, 70)
    # exit_btn = Button(150, 70)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        pygame.display.blit(menu_bg, (0, 0))
    start_btn.draw(300, 200, 'Start', None, 50)
    pygame.display.update()
    clock.tick(60)

# show_menu()


def game_cycle():
    while True:
        global surface, game_surface, player_img, time, portals
        surface.blit(bg, (WIDTH, 0))
        surface.blit(game_surface, (0, 0))
        game_surface.blit(bg_game, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.USEREVENT:
                time -= 1

        pressed_key = pygame.key.get_pressed()
        for key, key_value in keys.items():
            if pressed_key[key_value] and not is_collide(*directions[key]):
                direction = directions[key]
                break
        if pressed_key[key_value] and not is_collide(*direction):
            if player_img != image2 and direction == (STEP, 0) and not is_collide(*direction):
                player_img = image2

            if player_img != image3 and direction == (-STEP, 0) and not is_collide(*direction):
                player_img = image3

            if player_img != image4 and direction == (0, STEP) and not is_collide(*direction):
                player_img = image4

            if player_img != image1 and direction == (0, -STEP) and not is_collide(*direction):
                player_img = image1
            player_rect.move_ip(direction)

        [cell.draw(game_surface) for cell in maze]

        if claim_portal():
            portals += 1
        is_game_over()

        game_surface.blit(player_img, player_rect)

        [portal.draw() for portal in portal_list]

        surface.blit(text_font.render('TIME', True, pygame.Color('red')), (WIDTH + 70, 30))
        surface.blit(font.render(f'{time}', True, pygame.Color('red')), (WIDTH + 70, 130))
        surface.blit(text_font.render('Mission:', True, pygame.Color('cyan')), (WIDTH + 15, 350))
        surface.blit(font1.render('Get the Portal', True, pygame.Color('cyan')), (WIDTH + 15, 480))

        pygame.display.flip()
        clock.tick(FPS)


game_cycle()