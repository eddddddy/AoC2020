def part1(expenses, s=2020):
    to_look_for = set()
    for expense in expenses:
        if expense in to_look_for:
            return expense * (s - expense)
        to_look_for.add(s - expense)
    return -1


def part2(expenses):
    for expense in expenses:
        expenses_copy = expenses[:]
        expenses_copy.remove(expense)

        result = part1(expenses_copy, s=2020 - expense)
        if result >= 0:
            return expense * result


def main():
    with open('input.txt', 'r') as f:
        expenses = f.readlines()
        expenses = [int(expense) for expense in expenses]

    print(part1(expenses))
    print(part2(expenses))


if __name__ == '__main__':
    main()
