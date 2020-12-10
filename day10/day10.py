def part1(joltages):
    joltages = sorted(joltages)
    joltages = [0, *joltages, joltages[-1] + 3]
    count1, count3 = 0, 0
    for i in range(len(joltages) - 1):
        diff = joltages[i + 1] - joltages[i]
        if diff == 1:
            count1 += 1
        elif diff == 3:
            count3 += 1
    return count1 * count3


def part2(joltages):
    joltages = sorted(joltages)
    joltages = [0, *joltages, joltages[-1] + 3]
    counts = [0] * len(joltages)
    for i in range(len(joltages)):
        if i == 0:
            counts[i] = 1
        else:
            subtotal = counts[i - 1]
            if i >= 2 and joltages[i] - joltages[i - 2] <= 3:
                subtotal += counts[i - 2]
                if i >= 3 and joltages[i] - joltages[i - 3] <= 3:
                    subtotal += counts[i - 3]
            counts[i] = subtotal
    return counts[-1]


def main():
    with open('input.txt', 'r') as f:
        joltages = [int(line.strip()) for line in f.readlines()]

    print(part1(joltages))
    print(part2(joltages))


if __name__ == '__main__':
    main()
