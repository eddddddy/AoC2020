from typing import List


def apply_mask_part1(value: int, mask: str) -> int:
    return (value & int(mask.replace('X', '1'), 2)) | int(mask.replace('X', '0'), 2)


def apply_mask_part2(value: int, mask: str) -> str:
    masked = ''
    value_bin = f'{value:036b}'
    for i, char in enumerate(mask):
        if char == '0':
            masked += value_bin[i]
        else:
            masked += char
    return masked


def get_addresses_from_floating(address: str) -> List[str]:
    if 'X' not in address:
        return [address]
    else:
        return get_addresses_from_floating(address.replace('X', '0', 1)) + \
               get_addresses_from_floating(address.replace('X', '1', 1))


def part1(program):
    mask = None
    memory = {}
    for line in program:
        if isinstance(line, str):
            mask = line
        else:
            address, value = line
            memory[address] = apply_mask_part1(value, mask)
    return sum(memory.values())


def part2(program):
    mask = None
    memory = {}
    for line in program:
        if isinstance(line, str):
            mask = line
        else:
            address, value = line
            all_addresses = get_addresses_from_floating(apply_mask_part2(address, mask))
            for address in all_addresses:
                memory[address] = value
    return sum(memory.values())


def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        for i, line in enumerate(lines):
            if line.startswith('mask'):
                lines[i] = line[line.index('=') + 2:]
            else:
                address = int(line[line.index('[') + 1:line.index(']')])
                value = int(line[line.index('=') + 2:])
                lines[i] = (address, value)

    print(part1(lines))
    print(part2(lines))


if __name__ == '__main__':
    main()
