from functools import reduce


def part1(earliest_time, bus_ids):
    wait_time = 0
    while True:
        for bus_id in bus_ids:
            if (earliest_time + wait_time) % bus_id == 0:
                return wait_time * bus_id
        wait_time += 1


def part2(bus_ids, departures):
    def crt(a, b, p, q):
        d = 0
        while True:
            if (d * p + a - b) % q == 0:
                return p * q, d * p + a
            d += 1

    bus_departure_offsets = [(bus_id, bus_id - departures.index(bus_id)) for bus_id in bus_ids]
    return reduce(lambda x, y: crt(x[1], y[1], x[0], y[0]), bus_departure_offsets, (1, 0))[1]


def main():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
        earliest_time = int(lines[0])
        departures = [int(bus_id) if bus_id != 'x' else 'x' for bus_id in lines[1].split(',')]
        bus_ids = [bus_id for bus_id in departures if bus_id != 'x']

    print(part1(earliest_time, bus_ids))
    print(part2(bus_ids, departures))


if __name__ == '__main__':
    main()
