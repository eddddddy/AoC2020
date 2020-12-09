from string import ascii_lowercase
from functools import reduce


def part1(answers):
    yes_answers = []
    for answer in answers:
        answer = answer.replace('\n', '')
        yes_answers.append(len(set(answer)))
    return sum(yes_answers)


def part2(answers):
    yes_answers = []
    for answer in answers:
        answer = [set(a) for a in answer.split('\n')]
        yes_answers.append(len(reduce(lambda x, y: x.intersection(y), answer, set(ascii_lowercase))))
    return sum(yes_answers)


def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        answers = '\n'.join(lines).split('\n\n')

    print(part1(answers))
    print(part2(answers))


if __name__ == '__main__':
    main()
