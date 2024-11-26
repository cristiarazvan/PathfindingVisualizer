import pygame
import math
from queue import PriorityQueue, Queue
import time

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path Finding Algorithm")

# Colors
DARK_BACKGROUND = (20, 20, 20)
GRID_COLOR = (50, 50, 50)
MANGO = (255, 185, 90)
FOREST_GREEN = (34, 139, 34)
TEAL = (0, 128, 128)
GOLD = (255, 215, 0)
DARKER_BACKGROUND = (30, 30, 30)
COBALT_BLUE = (70, 130, 180)
MIDNIGHT_PURPLE = (75, 0, 130)
ORANGE_RED = (255, 69, 0)
DARK_GRAY = (60, 60, 60)

class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = DARKER_BACKGROUND
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == MANGO

    def is_open(self):
        return self.color == FOREST_GREEN

    def is_barrier(self):
        return self.color == DARK_GRAY

    def is_start(self):
        return self.color == ORANGE_RED

    def is_end(self):
        return self.color == COBALT_BLUE

    def reset(self):
        self.color = DARKER_BACKGROUND

    def make_start(self):
        self.color = ORANGE_RED

    def make_closed(self):
        self.color = MANGO

    def make_open(self):
        self.color = FOREST_GREEN

    def make_barrier(self):
        self.color = DARK_GRAY

    def make_end(self):
        self.color = COBALT_BLUE

    def make_path(self):
        self.color = MIDNIGHT_PURPLE

    def make_processing(self):
        self.color = TEAL

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

def algorithm(draw, grid, start, end, speed):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()
        time.sleep(speed)

        if current != start:
            current.make_closed()

    return False

def dfs(draw, grid, start, end, speed):
    stack = [start]
    came_from = {}
    visited = {spot: False for row in grid for spot in row}
    visited[start] = True

    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = stack.pop()

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            if not visited[neighbor]:
                stack.append(neighbor)
                visited[neighbor] = True
                came_from[neighbor] = current
                neighbor.make_open()

        draw()
        time.sleep(speed)

        if current != start:
            current.make_closed()

    return False

def bfs(draw, grid, start, end, speed):
    queue = Queue()
    queue.put(start)
    came_from = {}
    visited = {spot: False for row in grid for spot in row}
    visited[start] = True

    while not queue.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = queue.get()

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            if not visited[neighbor]:
                queue.put(neighbor)
                visited[neighbor] = True
                came_from[neighbor] = current
                neighbor.make_open()

        draw()
        time.sleep(speed)

        if current != start:
            current.make_closed()

    return False

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GRID_COLOR, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GRID_COLOR, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
    win.fill(DARK_BACKGROUND)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col

def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None
    speed = 0.02

    run = True
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start and spot != end:
                    start = spot
                    start.make_start()
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                elif spot != end and spot != start:
                    spot.make_barrier()
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end, speed)
                if event.key == pygame.K_d and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                    dfs(lambda: draw(win, grid, ROWS, width), grid, start, end, speed)
                if event.key == pygame.K_b and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                    bfs(lambda: draw(win, grid, ROWS, width), grid, start, end, speed)
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)
                if event.key == pygame.K_UP:
                    speed = max(0.001, speed - 0.01)
                if event.key == pygame.K_DOWN:
                    speed = min(0.1, speed + 0.01)

    pygame.quit()

main(WIN, WIDTH)