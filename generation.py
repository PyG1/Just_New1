from random import choice, randrange
from Func import *


class Cell:
    def __init__(self, col, row, tile, thick):
        self.col, self.row = col, row
        self.tile = tile
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False
        self.thickness = thick
        self.x, self.y = self.col * self.tile, self.row * self.tile

    def draw(self, sc, visible, dark):
        if visible or not dark:
            if self.walls['top']:
                pygame.draw.line(sc, pygame.Color('gray12'),
                                 (self.x, self.y), (self.x + self.tile, self.y),
                                 self.thickness)
            if self.walls['right']:
                pygame.draw.line(sc, pygame.Color('gray12'),
                                 (self.x + self.tile, self.y),
                                 (self.x + self.tile, self.y + self.tile),
                                 self.thickness)
            if self.walls['bottom']:
                pygame.draw.line(sc, pygame.Color('gray12'),
                                 (self.x + self.tile, self.y + self.tile),
                                 (self.x, self.y + self.tile), self.thickness)
            if self.walls['left']:
                pygame.draw.line(sc, pygame.Color('gray12'),
                                 (self.x, self.y + self.tile), (self.x, self.y),
                                 self.thickness)
        elif not visible and dark:
            pygame.draw.rect(sc, (0, 0, 0),
                             (self.x, self.y, self.tile, self.tile))

    def get_rects(self):
        rects = []
        x, y = self.col * self.tile, self.row * self.tile
        if self.walls['top']:
            rects.append(pygame.Rect((x, y), (self.tile, self.thickness)))
        if self.walls['right']:
            rects.append(pygame.Rect((x + self.tile, y), (self.thickness, self.tile)))
        if self.walls['bottom']:
            rects.append(pygame.Rect((x, y + self.tile), (self.tile, self.thickness)))
        if self.walls['left']:
            rects.append(pygame.Rect((x, y), (self.thickness, self.tile)))
        return rects


class Maze:
    def __init__(self, tile, cols, rows, thick):
        self.grid_cells = None
        self.player_col = 0
        self.player_row = 0
        self.thick = thick
        self.cols = cols
        self.rows = rows
        self.tile = tile
        self.visible_cells = []
        self.generate()

    def cells(self):
        return self.grid_cells

    def find_index(self, col, row):
        return col + row * self.cols

    def __getitem__(self, key):
        return self.grid_cells[key]

    def get_collides(self):
        return sum([cell.get_rects() for cell in self.grid_cells], [])

    def isVisible(self, cell):
        return self.find_index(cell.col, cell.row) in self.visible_cells

    def get_visible_cells_rects(self):
        return [pygame.Rect(self.grid_cells[i].x, self.grid_cells[i].y,
                            self.tile, self.tile) for i in self.visible_cells]

    def move_player(self, x, y):
        self.player_col = (x + self.tile // 2) // self.tile
        self.player_row = (y + self.tile // 2) // self.tile
        self.checkVisibleCells()

    def checkVisibleCells(self):
        visible_cells = [self.find_index(self.player_col, self.player_row)]

        for row in range(self.player_row - 1, -1, -1):
            index = self.find_index(self.player_col, row)
            if self.grid_cells[index].walls['bottom']:
                break
            visible_cells.append(index)

        for row in range(self.player_row + 1, self.rows):
            index = self.find_index(self.player_col, row)
            if self.grid_cells[index].walls['top']:
                break
            visible_cells.append(index)

        for col in range(self.player_col - 1, -1, -1):
            index = self.find_index(col, self.player_row)
            if self.grid_cells[index].walls['right']:
                break
            visible_cells.append(index)

        for col in range(self.player_col + 1, self.cols):
            index = self.find_index(col, self.player_row)
            if self.grid_cells[index].walls['left']:
                break
            visible_cells.append(index)

        self.visible_cells = visible_cells

    def draw(self, game_surface, dark):
        [cell.draw(game_surface, self.isVisible(cell), dark) for cell in self.grid_cells]

    def generate(self):
        self.grid_cells = [Cell(col, row, self.tile, self.thick) for row in range(self.rows) for col in range(self.cols)]
        current_cell = self.grid_cells[0]
        array = []
        break_count = 1

        while break_count != len(self.grid_cells):
            current_cell.visited = True
            next_cell = self.check_neighbors(current_cell)
            if next_cell:
                next_cell.visited = True
                break_count += 1
                array.append(current_cell)
                self.remove_walls(current_cell, next_cell)
                current_cell = next_cell
            elif array:
                current_cell = array.pop()

    def check_cell(self, col, row):
        if col < 0 or col > self.cols - 1 or row < 0 or row > self.rows - 1:
            return False
        return self.grid_cells[self.find_index(col, row)]

    def check_neighbors(self, cell):
        neighbors = []
        top = self.check_cell(cell.col, cell.row - 1)
        right = self.check_cell(cell.col + 1, cell.row)
        bottom = self.check_cell(cell.col, cell.row + 1)
        left = self.check_cell(cell.col - 1, cell.row)
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        return choice(neighbors) if neighbors else False

    def remove_walls(self, current, next):
        dx = current.col - next.col
        if dx == 1:
            current.walls['left'] = False
            next.walls['right'] = False
        elif dx == -1:
            current.walls['right'] = False
            next.walls['left'] = False
        dy = current.row - next.row
        if dy == 1:
            current.walls['top'] = False
            next.walls['bottom'] = False
        elif dy == -1:
            current.walls['bottom'] = False
            next.walls['top'] = False
