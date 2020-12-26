class Cup:
    def __init__(self, cup, next=None):
        self.cup = cup
        self.next = next


class Circle:
    def __init__(self, cups):
        nodes = {}
        for cup in cups:
            nodes[cup] = Cup(cup)
        for i in range(len(cups)):
            nodes[cups[i]].next = nodes[cups[(i + 1) % len(cups)]]

        self.nodes = nodes
        self.num_cups = len(cups)
        self.current = cups[0]

    def step(self):
        current_node = self.nodes[self.current]
        next1 = current_node.next
        next2 = next1.next
        next3 = next2.next

        next_cup_values = [next1.cup, next2.cup, next3.cup]
        dest_cup = (current_node.cup + self.num_cups - 2) % self.num_cups + 1
        while dest_cup in next_cup_values:
            dest_cup = (dest_cup + self.num_cups - 2) % self.num_cups + 1
        dest_node = self.nodes[dest_cup]

        current_node.next = next3.next
        next3.next = dest_node.next
        dest_node.next = next1

        self.current = current_node.next.cup

    def gather(self):
        cups = []
        current_node = self.nodes[1].next
        while current_node.cup != 1:
            cups.append(current_node.cup)
            current_node = current_node.next
        return cups


def part1(cups):
    circle = Circle(cups)
    for i in range(100):
        circle.step()

    return ''.join([str(c) for c in circle.gather()])


def part2(cups):
    cups = cups + list(range(max(cups) + 1, 1000001))
    circle = Circle(cups)
    for i in range(10000000):
        circle.step()

    first, second = circle.gather()[:2]
    return first * second


def main():
    with open('input.txt', 'r') as f:
        cups = [int(c) for c in f.readlines()[0].strip()]

    print(part1(cups))
    print(part2(cups))


if __name__ == '__main__':
    main()
