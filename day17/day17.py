from itertools import product


class PocketDimension:
    def __init__(self, initial=None, dims=3):
        self.grid = {}
        self.dims = dims
        if initial is not None:
            for i in range(len(initial)):
                for j in range(len(initial[0])):
                    self.grid[(i, j, *([0] * (dims - 2)))] = (initial[i][j] == '#')

    def get_active_boundary(self):
        ret = []
        for dim in range(self.dims):
            ret.append(min([pos[dim] for pos, active in self.grid.items() if active]))
            ret.append(max([pos[dim] for pos, active in self.grid.items() if active]))
        return ret

    def prune(self):
        boundary = self.get_active_boundary()
        self.grid = {pos: active for pos, active in self.grid.items()
                     if all([boundary[2 * dim] <= pos[dim] <= boundary[2 * dim + 1] for dim in range(self.dims)])}

    def __getitem__(self, item):
        if item not in self.grid:
            self.grid[item] = False
        return self.grid[item]

    def __setitem__(self, item, value):
        self.grid[item] = value


def count_active_neighbours(pocket_dimension, pos):
    neighbours = product(*[[pos[dim] + delta for delta in [-1, 0, 1]] for dim in range(pocket_dimension.dims)])
    count = 0
    for neighbour in neighbours:
        if neighbour != pos and pocket_dimension[neighbour]:
            count += 1
    return count


def step(pocket_dimension):
    new_pocket_dimension = PocketDimension(dims=pocket_dimension.dims)
    new_pocket_dimension.grid = pocket_dimension.grid.copy()

    boundary = pocket_dimension.get_active_boundary()
    internal_pos = product(*[range(boundary[2 * dim] - 1, boundary[2 * dim + 1] + 2) for dim in range(pocket_dimension.dims)])

    for pos in internal_pos:
        neighbours = count_active_neighbours(pocket_dimension, pos)
        if pocket_dimension[pos] and neighbours not in [2, 3]:
            new_pocket_dimension[pos] = False
        elif not pocket_dimension[pos] and neighbours == 3:
            new_pocket_dimension[pos] = True

    new_pocket_dimension.prune()
    return new_pocket_dimension


def part1(pocket_dimension):
    for _ in range(6):
        pocket_dimension = step(pocket_dimension)
    return sum(pocket_dimension.grid.values())


def part2(pocket_dimension):
    for _ in range(6):
        pocket_dimension = step(pocket_dimension)
    return sum(pocket_dimension.grid.values())


def main():
    with open('input.txt', 'r') as f:
        state = [list(line.strip()) for line in f.readlines()]
        pocket_dimension_dim3 = PocketDimension(state)
        pocket_dimension_dim4 = PocketDimension(state, dims=4)

    print(part1(pocket_dimension_dim3))
    print(part2(pocket_dimension_dim4))


if __name__ == '__main__':
    main()
