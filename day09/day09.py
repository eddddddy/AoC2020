def part1(numbers, preamble_length=25):
    for i in range(preamble_length, len(numbers)):
        seen = set()
        for num in numbers[i - preamble_length:i]:
            if numbers[i] - num in seen and numbers[i] - num != num:
                break
            else:
                seen.add(num)
        else:
            return numbers[i]


def part2(numbers, preamble_length=25):
    target = part1(numbers, preamble_length=preamble_length)
    i, j = 0, 0
    while j < len(numbers):
        if sum(numbers[i:j + 1]) < target:
            j += 1
        elif sum(numbers[i:j + 1]) > target:
            i += 1
        else:
            return min(numbers[i:j + 1]) + max(numbers[i:j + 1])


def main():
    with open('input.txt', 'r') as f:
        numbers = [int(line.strip()) for line in f.readlines()]

    print(part1(numbers))
    print(part2(numbers))


if __name__ == '__main__':
    main()
