from queue import Queue


def playout_part1(p1_cards, p2_cards):
    p1_queue, p2_queue = Queue(), Queue()
    for card in p1_cards:
        p1_queue.put(card)
    for card in p2_cards:
        p2_queue.put(card)

    while not p1_queue.empty() and not p2_queue.empty():
        p1_card, p2_card = p1_queue.get(), p2_queue.get()
        if p1_card > p2_card:
            p1_queue.put(p1_card)
            p1_queue.put(p2_card)
        else:
            p2_queue.put(p2_card)
            p2_queue.put(p1_card)

    if p1_queue.empty():
        return list(p2_queue.queue), False
    else:
        return list(p1_queue.queue), True


def playout_part2(p1_cards, p2_cards):
    p1_queue, p2_queue = Queue(), Queue()
    for card in p1_cards:
        p1_queue.put(card)
    for card in p2_cards:
        p2_queue.put(card)

    i = 0
    while not p1_queue.empty() and not p2_queue.empty():
        if i > 1000:
            return [], True
        else:
            i += 1
        p1_card, p2_card = p1_queue.get(), p2_queue.get()

        if p1_queue.qsize() >= p1_card and p2_queue.qsize() >= p2_card:
            new_p1_cards = list(p1_queue.queue)[:p1_card]
            new_p2_cards = list(p2_queue.queue)[:p2_card]
            if max(new_p1_cards) > max(new_p2_cards):
                p1_won = True
            else:
                p1_won = playout_part2(new_p1_cards, new_p2_cards)[1]
        else:
            p1_won = p1_card > p2_card

        if p1_won:
            p1_queue.put(p1_card)
            p1_queue.put(p2_card)
        else:
            p2_queue.put(p2_card)
            p2_queue.put(p1_card)

    if p1_queue.empty():
        return list(p2_queue.queue), False
    else:
        return list(p1_queue.queue), True


def part1(p1_cards, p2_cards):
    winner_deck, _ = playout_part1(p1_cards, p2_cards)
    s = 0
    for i, card in enumerate(winner_deck[::-1], start=1):
        s += i * card
    return s


def part2(p1_cards, p2_cards):
    winner_deck, _ = playout_part2(p1_cards, p2_cards)
    s = 0
    for i, card in enumerate(winner_deck[::-1], start=1):
        s += i * card
    return s


def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        p1_cards, p2_cards = '\n'.join(lines).split('\n\n')
        p1_cards = [int(card) for card in p1_cards.split('\n')[1:]]
        p2_cards = [int(card) for card in p2_cards.split('\n')[1:]]

    print(part1(p1_cards, p2_cards))
    print(part2(p1_cards, p2_cards))


if __name__ == '__main__':
    main()
