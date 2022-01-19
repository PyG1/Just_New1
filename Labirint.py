from game_menu import men
from end_g import records
from generation import *


class ControlKey:
    def __init__(self, key, dx, dy, act):
        self.key, self.dx, self.dy, self.act = key, dx, dy, act


class MagicKey(pygame.sprite.Sprite):
    image = pygame.transform.scale(skin('key_3', conv=False), (int(stats('tile')) - 2 * int(stats('thick')),
                                                               int(stats('tile')) - 2 * int(stats('thick'))))

    def __init__(self):
        self.key_g = pygame.sprite.Group()
        super().__init__(self.key_g)
        self.img = MagicKey.image
        self.color_key = MagicKey.image.get_at((0, 0))
        self.img.set_colorkey(self.color_key)
        self.img = self.img.convert_alpha()
        self.rect = self.img.get_rect().move(randrange(cols) * int(stats('tile')) + WALL_THICK,
                                             randrange(rows) * int(stats('tile')) + WALL_THICK)

    def kill_sprites(self):
        for sprite in self.key_g:
            sprite.kill()

    def collide(self):
        for sprite in self.key_g:
            return True if player_rect.collidepoint(sprite.rect.center) else False

    def draw(self, surface):
        self.key_g.draw(surface)

    def claim(self):
        for sprite in self.key_g:
            if player_rect.collidepoint(sprite.rect.center):
                sprite.kill()
                return True
        return False


class Portal:
    def __init__(self):
        global img_p, img_p1
        self.img_p = img_p
        self.img_p1 = img_p1
        self.found = False
        self.rect = img_p.get_rect()
        self.set_pos()

    def set_pos(self):
        self.rect.topleft = randrange(cols) * int(stats('tile')) + WALL_THICK, \
                            randrange(rows) * int(stats('tile')) + WALL_THICK

    def draw(self, key):
        if read(4) == '   None' or (self.found and read(4) == 'Darkness'):
            game_surface.blit(self.img_p, self.rect)
            if key:
                if self.img_p != self.img_p1:
                    self.img_p = self.img_p1

    def check_found(self, visible_rects):
        if read(4) == 'Darkness':
            if not self.found and self.rect.collidelist(visible_rects) != -1:
                self.found = True
                return True
            return False


def is_collide(x, y):
    tmp_rect = player_rect.move(x, y)
    if tmp_rect.collidelist(walls_collide_list) == -1:
        return False
    return True


def claim_portal():
    global portal, pres
    return player_rect.collidepoint(portal.rect.center) and pres


def start_new_game():
    global time, portal_reached, FPS, maze, walls_collide_list, img_p, img_p1, WALL_THICK, TILE, \
        magic_key_got, magic_key, portal, direction, dark, player_rect, rows, cols, a, image1, image2,\
        image3, image4, img_p, img_p1, player_img

    a = int(stats('tile')) - 2 * int(stats('thick'))
    WALL_THICK = stats('thick')
    TILE = int(stats('tile'))
    cols, rows = 800 // TILE, 600 // TILE
    maze = Maze(TILE, cols, rows, WALL_THICK)
    walls_collide_list = maze.get_collides()
    magic_key = MagicKey()
    magic_key_got = False
    magic_key.image = pygame.transform.scale(skin('key_3', conv=False), (a, a))
    magic_key.rect = magic_key.img.get_rect().move(randrange(cols) * int(stats('tile')) + WALL_THICK,
                                                   randrange(rows) * int(stats('tile')) + WALL_THICK)
    magic_key.draw(surface)
    dark = True if stats('challenge') == 'Darkness' else False
    maze.draw(game_surface, dark)

    image1 = pygame.transform.scale(skin(stats("skin") + '0'), (a, a))
    player_img = image1
    image2 = pygame.transform.scale(skin(stats("skin") + '1'), (a, a))
    image3 = pygame.transform.scale(skin(stats("skin") + '2'), (a, a))
    image4 = pygame.transform.scale(skin(stats("skin") + '3'), (a, a))
    player_rect = player_img.get_rect()
    player_rect.center = int(stats('tile')) // 2, int(stats('tile')) // 2
    maze.move_player(player_rect[0], player_rect[1])

    img_p = pygame.transform.scale(skin('closed', conv=False), (a, a))
    img_p1 = pygame.transform.scale(skin('opened', conv=False), (a, a))
    portal = Portal()
    portal.rect = img_p.get_rect()
    portal.set_pos()
    write(8, 'False')
    direction = (0, 0)
    portal_reached, FPS = False, 60
    if TILE == 100:
        time = 40
    elif TILE == 20:
        time = 240
    else:
        time = 60


pygame.init()
game_surface = pygame.Surface(display)
surface = pygame.display.set_mode(display)
font = pygame.font.SysFont('Comic Sans MS', 32)
clock = pygame.time.Clock()
bg_game = skin('bg_1')
player_img = pygame.transform.scale(skin(stats('skin') + '0'), (int(stats('tile')) - 2 * int(stats('thick')),
                                                                int(stats('tile')) - 2 * int(stats('thick'))))
player_rect = player_img.get_rect()
STEP = 4
control_keys = {
    'a': ControlKey(pygame.K_a, -STEP, 0, False),
    'd': ControlKey(pygame.K_d, STEP, 0, False),
    'w': ControlKey(pygame.K_w, 0, -STEP, False),
    's': ControlKey(pygame.K_s, 0, STEP, False),
    'e': ControlKey(pygame.K_e, 0, 0, True)}
pygame.time.set_timer(pygame.USEREVENT, 1000)
e = skin('b_e', 50)
img_p = skin('closed', conv=False)
img_p1 = skin('opened', conv=False)
warning = font.render('You cant go without a key', True, pygame.Color('gray26'))


def game_cycle():
    start_new_game()
    global surface, game_surface, player_img, time, portal_reached,\
            magic_key_got, pres, direction, key_value, dark

    if stats('song') == 'On':
        pygame.mixer.Sound.play(game_fon)
    run = True
    while run:
        tm = font.render(str(time), True, (255, 80, 0))
        surface.blit(game_surface, (0, 0))
        game_surface.blit(bg_game, (0, 0))
        surface.blit(tm, (3, 3))
        magic_key.draw(game_surface)
        if player_rect.collidepoint(portal.rect.center) and magic_key_got or magic_key.collide():
            surface.blit(e, (740, 10))
        if player_rect.collidepoint(portal.rect.center) and not magic_key_got:
            surface.blit(warning, (220, 5))
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                time -= 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                pygame.mixer.pause()
                if men(time) == 0:
                    start_new_game()
                    pygame.mixer.stop()
                    run = False
                else:
                    pygame.mixer.unpause()
        pressed_key = pygame.key.get_pressed()
        action = False
        direction = (0, 0)
        for key_ch, key_value in control_keys.items():
            if pressed_key[key_value.key] and not is_collide(key_value.dx, key_value.dy):
                direction = key_value.dx, key_value.dy
                action = key_value.act
                break

        if pressed_key[key_value.key] and not is_collide(*direction):
            if player_img != image2 and direction == (STEP, 0) \
                    and not is_collide(*direction):
                player_img = image2
                pres = False

            elif player_img != image1 and direction == (0, -STEP) \
                    and not is_collide(*direction):
                player_img = image1
                pres = False

            elif player_img != image3 and direction == (-STEP, 0) \
                    and not is_collide(*direction):
                player_img = image3
                pres = False

            elif player_img != image4 and direction == (0, STEP) \
                    and not is_collide(*direction):
                player_img = image4
                pres = False

            elif action:
                pres = True

            player_rect.move_ip(direction)
            maze.move_player(player_rect[0], player_rect[1])
        maze.draw(game_surface, dark)

        if action and magic_key.claim():
            if stats('sound') == 'On':
                key_got.play(0)
            if stats('song') == 'On':
                pygame.mixer.stop()
                pygame.mixer.Sound.play(ending)
            magic_key_got = True
            write(8, 'True')
        if claim_portal() and magic_key_got:
            portal_reached = True

        if time == 0 or portal_reached:
            pygame.mixer.stop()
            start_new_game()
            records(time)
            run = False
        portal.draw(magic_key_got)
        game_surface.blit(player_img, player_rect)
        if direction != (0, 0) and portal.check_found(maze.get_visible_cells_rects()):
            pass
        pygame.display.flip()
        clock.tick(FPS)