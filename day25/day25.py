from functools import reduce


def exponentiate(base, exponent, mod):
    ret = 1
    for _ in range(exponent):
        ret = ret * base % mod
    return ret


def add_to_power_cache(power_cache, base, exponent, mod):
    if exponent == 1:
        power_cache[1] = base % mod
    elif exponent // 2 not in power_cache:
        add_to_power_cache(power_cache, base, exponent // 2, mod)
    else:
        power_cache[exponent] = power_cache[exponent // 2] ** 2 % mod


def transform_subject_number(subject, loop_size, power_cache):
    def powers_of_two(num):
        return [1 << idx for idx, bit in enumerate(bin(num)[:1:-1]) if bit == "1"]

    powers = powers_of_two(loop_size)
    for power in powers:
        if power not in power_cache:
            add_to_power_cache(power_cache, subject, power, 20201227)

    return reduce(lambda x, y: x * power_cache[y] % 20201227, powers, 1)


def part1(public1, public2):
    power_cache = {}
    for i in range(1, 20201227):
        transformed = transform_subject_number(7, i, power_cache)
        if transformed == public1:
            return exponentiate(public2, i, 20201227)
        elif transformed == public2:
            return exponentiate(public1, i, 20201227)


def main():
    with open('input.txt') as f:
        public1, public2 = [int(line.strip()) for line in f.readlines()]

    print(part1(public1, public2))


if __name__ == '__main__':
    main()
