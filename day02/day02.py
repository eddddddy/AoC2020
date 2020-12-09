def part1(passwords):
    count = 0
    for min_, max_, char, password in passwords:
        if min_ <= password.count(char) <= max_:
            count += 1
    return count


def part2(passwords):
    count = 0
    for i, j, char, password in passwords:
        if ((password[i - 1] == char and password[j - 1] != char) or
                (password[i - 1] != char and password[j - 1] == char)):
            count += 1
    return count


def main():
    with open('input.txt') as f:
        lines = f.readlines()
        passwords = []
        for line in lines:
            dash_index = line.index('-')
            first_space_index = line.index(' ')
            password_start_index = line.index(':') + 2
            min_ = int(line[:dash_index])
            max_ = int(line[dash_index + 1:first_space_index])
            char = line[first_space_index + 1]
            password = line[password_start_index:]
            passwords.append([min_, max_, char, password])

    print(part1(passwords))
    print(part2(passwords))


if __name__ == '__main__':
    main()
