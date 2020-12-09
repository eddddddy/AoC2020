from typing import Tuple, List


def part1(program: List[Tuple[str, int]]):
    pc, acc = 0, 0
    executed = set()
    while pc < len(program):
        inst, i = program[pc]
        if inst == 'nop':
            pc += 1
        elif inst == 'acc':
            acc += i
            pc += 1
        elif inst == 'jmp':
            pc += i

        if pc in executed:
            break
        else:
            executed.add(pc)
    else:
        return acc, True

    return acc, False


def part2(program: List[Tuple[str, int]]):
    for i in range(len(program)):
        if program[i][0] == 'nop':
            program_copy = program[:]
            program_copy[i] = ('jmp', program[i][1])
        elif program[i][0] == 'jmp':
            program_copy = program[:]
            program_copy[i] = ('nop', program[i][1])
        else:
            continue

        acc, halts = part1(program_copy)
        if halts:
            return acc


def main():
    with open('input.txt', 'r') as f:
        program = [line.strip() for line in f.readlines()]
        program = [(line.split()[0], int(line.split()[1])) for line in program]

    print(part1(program)[0])
    print(part2(program))


if __name__ == '__main__':
    main()
