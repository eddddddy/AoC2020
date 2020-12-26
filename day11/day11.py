from itertools import product

import numpy as np


def step(grid, vision_map, tolerance):
    new_grid = grid.copy()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i][j] == '.':
                continue
            occupied_count = 0
            for pos in vision_map[(i, j)]:
                if grid[pos[0]][pos[1]] == '#':
                    occupied_count += 1
            if occupied_count == 0:
                new_grid[i][j] = '#'
            elif occupied_count >= tolerance:
                new_grid[i][j] = 'L'
    return new_grid


def part1(grid):
    def get_vision_map():
        vision_map = {}
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                vision = []
                for direction in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    pos = (i + direction[0], j + direction[1])
                    if 0 <= i + direction[0] < grid.shape[0] and 0 <= j + direction[1] < grid.shape[1] and \
                        grid[pos[0]][pos[1]] == 'L':
                        vision.append((i + direction[0], j + direction[1]))
                vision_map[(i, j)] = vision
        return vision_map

    grid = np.array(grid)
    vision_map = get_vision_map()
    last = None
    while True:
        if grid.tostring() == last:
            return (grid == '#').astype(np.int32).sum()
        else:
            last = grid.tostring()
            grid = step(grid, vision_map, 4)


def part2(grid):
    def get_vision_map():
        vision_map = {}
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                vision = []
                for direction in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    pos = (i + direction[0], j + direction[1])
                    while 0 <= pos[0] < grid.shape[0] and 0 <= pos[1] < grid.shape[1]:
                        if grid[pos[0]][pos[1]] == 'L':
                            vision.append((pos[0], pos[1]))
                            break
                        pos = (pos[0] + direction[0], pos[1] + direction[1])
                vision_map[(i, j)] = vision
        return vision_map

    grid = np.array(grid)
    vision_map = get_vision_map()
    last = None
    while True:
        if grid.tostring() == last:
            return (grid == '#').astype(np.int32).sum()
        else:
            last = grid.tostring()
            grid = step(grid, vision_map, 5)


def main():
    with open('input.txt', 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]

    print(part1(grid))
    print(part2(grid))


if __name__ == '__main__':
    main()
