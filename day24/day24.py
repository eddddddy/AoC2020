def tokenize(s):
    i = 0
    tokens = []
    while i < len(s):
        if s[i] == 'e':
            tokens.append('e')
            i += 1
        elif s[i] == 'w':
            tokens.append('w')
            i += 1
        elif s[i] == 'n':
            if s[i + 1] == 'e':
                tokens.append('ne')
            elif s[i + 1] == 'w':
                tokens.append('nw')
            i += 2
        elif s[i] == 's':
            if s[i + 1] == 'e':
                tokens.append('se')
            elif s[i + 1] == 'w':
                tokens.append('sw')
            i += 2
    return tokens


def part1(tiles):
    flipped = {}
    for tile in tiles:
        directions = tokenize(tile)
        pos = (0, 0)
        for direction in directions:
            if direction == 'e':
                pos = (pos[0] + 2, pos[1])
            elif direction == 'w':
                pos = (pos[0] - 2, pos[1])
            elif direction == 'se':
                pos = (pos[0] + 1, pos[1] - 1)
            elif direction == 'sw':
                pos = (pos[0] - 1, pos[1] - 1)
            elif direction == 'ne':
                pos = (pos[0] + 1, pos[1] + 1)
            elif direction == 'nw':
                pos = (pos[0] - 1, pos[1] + 1)
        if pos not in flipped:
            flipped[pos] = False
        flipped[pos] = not flipped[pos]

    return len([pos for pos, is_flipped in flipped.items() if is_flipped]), flipped


def count_flipped_neighbours(pos, flipped):
    directions = [(2, 0), (1, 1), (-1, 1), (-2, 0), (-1, -1), (1, -1)]
    count = 0
    for direction in directions:
        if (pos[0] + direction[0], pos[1] + direction[1]) in flipped and \
                flipped[(pos[0] + direction[0], pos[1] + direction[1])]:
            count += 1
    return count


def part2(tiles):
    _, flipped = part1(tiles)
    for _ in range(100):
        new_flipped = flipped.copy()
        x_min, x_max = min([pos[0] for pos, _ in flipped.items()]), max([pos[0] for pos, _ in flipped.items()])
        y_min, y_max = min([pos[1] for pos, _ in flipped.items()]), max([pos[1] for pos, _ in flipped.items()])
        for x in range(x_min - 2, x_max + 3):
            for y in range(y_min - 1, y_max + 2):
                num_flipped_neighbours = count_flipped_neighbours((x, y), flipped)
                if (x, y) not in flipped:
                    flipped[(x, y)] = False
                if flipped[(x, y)]:
                    if num_flipped_neighbours == 0 or num_flipped_neighbours > 2:
                        new_flipped[(x, y)] = False
                else:
                    if num_flipped_neighbours == 2:
                        new_flipped[(x, y)] = True
        flipped = new_flipped

    return len([pos for pos, is_flipped in flipped.items() if is_flipped]), flipped


def main():
    with open('input.txt', 'r') as f:
        tiles = [line.strip() for line in f.readlines()]

    print(part1(tiles)[0])
    print(part2(tiles)[0])


if __name__ == '__main__':
    main()
