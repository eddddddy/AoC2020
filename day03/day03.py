from functools import reduce


def part1(grid, slope=(3, 1)):
    right, down = slope

    width = len(grid[0])
    tree_count = 0
    pos = [0, 0]
    while pos[0] < len(grid):
        if grid[pos[0]][pos[1]] == '#':
            tree_count += 1
        pos[0] += down
        pos[1] = (pos[1] + right) % width
    return tree_count


def part2(grid):
    tree_counts = []
    for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        tree_counts.append(part1(grid, slope=slope))
    return reduce(lambda x, y: x * y, tree_counts, 1)


def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        grid = [list(line) for line in lines]

    print(part1(grid))
    print(part2(grid))


if __name__ == '__main__':
    main()
