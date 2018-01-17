import pygame
from pygame.locals import *
import random
from copy import deepcopy


class GameOfLife:

    def __init__(self, width=640, height=480, cell_size=10, speed=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_grid(self):
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (0, y), (self.width, y))

    def run(self):
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        self.clist = self.cell_list(randomize=True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            self.draw_cell_list(self.clist)
            self.clist = self.update_cell_list(self.clist)
            self.draw_grid()

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def cell_list(self, randomize=True):
        self.clist = []
        for i in range(self.cell_height):
            empty = []
            for j in range(self.cell_width):
                empty.append(random.randint(0, 1))
            self.clist.append(empty)
        if not randomize:
            for i in range(self.cell_height):
                for j in range(self.cell_width):
                    self.clist[i][j] = 0
        return self.clist

    def draw_cell_list(self, clist):
        for i in range(self.height // self.cell_size):
            for j in range(self.width // self.cell_size):
                if clist[i][j] == 1:
                    pygame.draw.rect(self.screen, pygame.Color('green'),
                                     (i*self.cell_size+1, j*self.cell_size+1,
                                     self.cell_size - 1, self.cell_size - 1))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'),
                                     (i * self.cell_size+1, j*self.cell_size+1,
                                     self.cell_size - 1, self.cell_size - 1))

    def get_neighbours(self, cell):
        neighbours = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i or j) & (0 <= cell[0] + i < self.cell_height)\
                & (0 <= cell[1] + j < self.cell_width):
                    neighbours.append(self.clist[cell[0] + i][cell[1] + j])
        return neighbours

    def update_cell_list(self, cell_list):
        new_list = deepcopy(cell_list)
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if cell_list[i][j]:
                    if sum(self.get_neighbours((i, j))) in (2, 3):
                        new_list[i][j] = 1
                    else:
                        new_list[i][j] = 0
                else:
                    if sum(self.get_neighbours((i, j))) == 3:
                        new_list[i][j] = 1
                    else:
                        new_list[i][j] = 0
        self.clist = new_list
        return new_list

if __name__ == '__main__':
    game = GameOfLife(601, 601, 20)
    game.run()
