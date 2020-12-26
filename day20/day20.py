from typing import List, Tuple


GRID_SIZE = 12


def rotate(grid, amount):
    for i in range(amount):
        grid = [list(row) for row in zip(*grid)][::-1]
    return grid


def horizontal_flip(grid):
    return [row[::-1] for row in grid]


def matching_edges(tile1, tile2):
    top1, bottom1 = tile1[0], tile1[-1][::-1]
    left1, right1 = [row[0] for row in tile1][::-1], [row[-1] for row in tile1]
    top2, bottom2 = tile2[0], tile2[-1][::-1]
    left2, right2 = [row[0] for row in tile2][::-1], [row[-1] for row in tile2]

    tile1_edges = [right1, top1, left1, bottom1]
    tile2_edges = [right2, top2, left2, bottom2]
    matches = []
    for i in range(4):
        for j in range(4):
            if tile1_edges[i] == tile2_edges[j]:
                matches.append(([i, j], False))
            elif tile1_edges[i] == tile2_edges[j][::-1]:
                matches.append(([i, j], True))
    return matches


def match(tiles) -> List[List[Tuple[int, List[List[str]]]]]:
    edge_matches = {}
    tile_items = list(tiles.items())
    for i in range(len(tiles) - 1):
        for j in range(i + 1, len(tiles)):
            matches = matching_edges(tile_items[i][1], tile_items[j][1])
            edge_matches[(tile_items[i][0], tile_items[j][0])] = matches
            edge_matches[(tile_items[j][0], tile_items[i][0])] = [(m1[::-1], m2) for m1, m2 in matches]

    for tile_num, _ in tile_items:
        edges_that_match = [m[0][0][0] for t, m in edge_matches.items() if t[0] == tile_num and len(m) > 0]
        if len(edges_that_match) == 2 and 0 in edges_that_match and 3 in edges_that_match:
            corner_tile = tile_num

    grid = []
    for r in range(GRID_SIZE):
        if r == 0:
            row = [(corner_tile, tiles[corner_tile])]
        else:
            last_tile = grid[-1][0][0]
            bottom_edge = grid[-1][0][1][-1]
            row = []

            for tile_num, tile in tile_items:
                if tile_num == last_tile:
                    continue
                top, bottom = tile[0], tile[-1][::-1]
                left, right = [r[0] for r in tile][::-1], [r[-1] for r in tile]
                if top == bottom_edge:
                    row.append((tile_num, tile))
                    break
                elif bottom == bottom_edge:
                    row.append((tile_num, rotate(tile, 2)))
                    break
                elif left == bottom_edge:
                    row.append((tile_num, rotate(tile, 3)))
                    break
                elif right == bottom_edge:
                    row.append((tile_num, rotate(tile, 1)))
                    break
                elif top[::-1] == bottom_edge:
                    row.append((tile_num, horizontal_flip(tile)))
                    break
                elif bottom[::-1] == bottom_edge:
                    row.append((tile_num, rotate(horizontal_flip(tile), 2)))
                    break
                elif left[::-1] == bottom_edge:
                    row.append((tile_num, rotate(horizontal_flip(tile), 1)))
                    break
                elif right[::-1] == bottom_edge:
                    row.append((tile_num, rotate(horizontal_flip(tile), 3)))
                    break

        for c in range(GRID_SIZE - 1):
            last_tile = row[-1][0]
            right_edge = [r[-1] for r in row[-1][1]][::-1]
            for tile_num, tile in tile_items:
                if tile_num == last_tile:
                    continue
                top, bottom = tile[0], tile[-1][::-1]
                left, right = [r[0] for r in tile][::-1], [r[-1] for r in tile]
                if top == right_edge:
                    row.append((tile_num, rotate(tile, 1)))
                    break
                elif bottom == right_edge:
                    row.append((tile_num, rotate(tile, 3)))
                    break
                elif left == right_edge:
                    row.append((tile_num, tile))
                    break
                elif right == right_edge:
                    row.append((tile_num, rotate(tile, 2)))
                    break
                elif top[::-1] == right_edge:
                    row.append((tile_num, rotate(horizontal_flip(tile), 1)))
                    break
                elif bottom[::-1] == right_edge:
                    row.append((tile_num, rotate(horizontal_flip(tile), 3)))
                    break
                elif left[::-1] == right_edge:
                    row.append((tile_num, rotate(horizontal_flip(tile), 2)))
                    break
                elif right[::-1] == right_edge:
                    row.append((tile_num, horizontal_flip(tile)))
                    break
        grid.append(row)
    return grid


def exists_sea_monster(image, pos):
    if pos[0] + 3 > len(image) or pos[1] + 20 > len(image[0]):
        return False, []
    required_pos = [(1, 0), (2, 1), (2, 4), (1, 5), (1, 6), (2, 7), (2, 10), (1, 11),
                    (1, 12), (2, 13), (2, 16), (1, 17), (0, 18), (1, 18), (1, 19)]
    for sm_pos in required_pos:
        if image[sm_pos[0] + pos[0]][sm_pos[1] + pos[1]] != '#':
            return False, []
    return True, [(sm_pos[0] + pos[0], sm_pos[1] + pos[1]) for sm_pos in required_pos]


def part1(tiles):
    matched = match(tiles)
    return matched[0][0][0] * matched[0][-1][0] * matched[-1][0][0] * matched[-1][-1][0]


def part2(tiles):
    matched = match(tiles)
    matched = [[[r[1:-1] for r in grid[1:-1]] for _, grid in row] for row in matched]

    image = []
    for i in range(8 * GRID_SIZE):
        row, r = i // 8, i % 8
        image_row = ""
        for grid in matched[row]:
            image_row += ''.join(grid[r])
        image.append(image_row)

    image = rotate(horizontal_flip(image), 3)

    sm_pos = set()
    for i in range(8 * GRID_SIZE):
        for j in range(8 * GRID_SIZE):
            exists, pos = exists_sea_monster(image, (i, j))
            if exists:
                sm_pos.update(pos)

    count_unoccupied = 0
    for i in range(8 * GRID_SIZE):
        for j in range(8 * GRID_SIZE):
            if image[i][j] == '#' and (i, j) not in sm_pos:
                count_unoccupied += 1
    return count_unoccupied


def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        tiles = [tile.split('\n') for tile in '\n'.join(lines).split('\n\n')]
        tiles = {int(tile[0][5:-1]): [list(row) for row in tile[1:]] for tile in tiles}

    print(part1(tiles))
    print(part2(tiles))


if __name__ == '__main__':
    main()
