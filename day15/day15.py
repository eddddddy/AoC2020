def part1(start, limit=2020):
    last_spoken = {}
    for i in range(len(start) - 1):
        last_spoken[start[i]] = i + 1

    last = start[-1]
    for i in range(len(start), limit):
        if last in last_spoken:
            last_time = last_spoken[last]
            last_spoken[last] = i
            last = i - last_time
        else:
            last_spoken[last] = i
            last = 0
    return last


def part2(start):
    return part1(start, limit=30000000)


def main():
    with open('input.txt', 'r') as f:
        start = [int(num) for num in f.readline().strip().split(',')]

    print(part1(start))
    print(part2(start))


if __name__ == '__main__':
    main()
