def part1(boarding_passes):
    highest_id = -1
    all_ids = []
    for boarding_pass in boarding_passes:
        row = int(boarding_pass[:7].replace('F', '0').replace('B', '1'), 2)
        col = int(boarding_pass[7:].replace('L', '0').replace('R', '1'), 2)
        seat_id = row * 8 + col
        highest_id = max(highest_id, seat_id)
        all_ids.append(seat_id)
    return highest_id, all_ids


def part2(boarding_passes):
    _, all_ids = part1(boarding_passes)
    all_ids = set(all_ids)
    for seat_id in range(1024):
        if seat_id not in all_ids and (seat_id + 1) in all_ids and (seat_id - 1) in all_ids:
            return seat_id


def main():
    with open('input.txt') as f:
        boarding_passes = [line.strip() for line in f.readlines()]

    print(part1(boarding_passes)[0])
    print(part2(boarding_passes))


if __name__ == '__main__':
    main()
