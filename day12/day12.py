def part1(insts):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    pos = [0, 0]
    direction = (1, 0)
    for action, value in insts:
        if action == 'N':
            pos[1] += value
        elif action == 'S':
            pos[1] -= value
        elif action == 'E':
            pos[0] += value
        elif action == 'W':
            pos[0] -= value
        elif action == 'L':
            direction = directions[((directions.index(direction) + value // 90) % 4 + 4) % 4]
        elif action == 'R':
            direction = directions[((directions.index(direction) - value // 90) % 4 + 4) % 4]
        elif action == 'F':
            pos = [pos[0] + direction[0] * value, pos[1] + direction[1] * value]

    return abs(pos[0]) + abs(pos[1])


def part2(insts):
    def rotate(direction, amount):
        amount = (amount % 4 + 4) % 4
        if amount == 0:
            return direction
        elif amount == 1:
            return -direction[1], direction[0]
        elif amount == 2:
            return -direction[0], -direction[1]
        elif amount == 3:
            return direction[1], -direction[0]

    pos = (0, 0)
    waypoint = [10, 1]
    for action, value in insts:
        if action == 'N':
            waypoint[1] += value
        elif action == 'S':
            waypoint[1] -= value
        elif action == 'E':
            waypoint[0] += value
        elif action == 'W':
            waypoint[0] -= value
        elif action == 'L':
            waypoint = list(rotate(waypoint, value // 90))
        elif action == 'R':
            waypoint = list(rotate(waypoint, -value // 90))
        elif action == 'F':
            pos = (pos[0] + waypoint[0] * value, pos[1] + waypoint[1] * value)
    return abs(pos[0]) + abs(pos[1])


def main():
    with open('input.txt', 'r') as f:
        insts = [line.strip() for line in f.readlines()]
        insts = [(inst[0], int(inst[1:])) for inst in insts]

    print(part1(insts))
    print(part2(insts))


if __name__ == '__main__':
    main()
