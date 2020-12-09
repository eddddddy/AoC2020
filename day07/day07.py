from typing import List, Tuple


class Node:
    def __init__(self, color):
        self.color = color
        self.contains = {}
        self.contained_in = {}


def build_graph(rules: List[Tuple[str, List[Tuple[str, int]]]]):
    nodes = {}
    for rule in rules:
        color, contains = rule
        if color not in nodes:
            nodes[color] = Node(color)
        for contained_color, _ in contains:
            if contained_color not in nodes:
                nodes[contained_color] = Node(contained_color)
        nodes[color].contains.update({nodes[contained_color]: amount for contained_color, amount in contains})
        for contained_color, amount in contains:
            nodes[contained_color].contained_in[nodes[color]] = amount

    return nodes


def parse_lines_into_rules(lines):
    def strip_bag(s):
        if s.endswith('bags'):
            return s[:-5]
        elif s.endswith('bag'):
            return s[:-4]

    rules = []
    for line in lines:
        contain_index = line.index('contain')
        color = strip_bag(line[:contain_index - 1])
        contains = line[contain_index + 8:].split(',')
        contains = [contain.strip(' .') for contain in contains]
        if contains[0].startswith('no'):
            rules.append((color, []))
        else:
            contained_in = []
            for s in contains:
                s = strip_bag(s)
                space_index = s.index(' ')
                amount = int(s[:space_index])
                contained_color = s[space_index + 1:]
                contained_in.append((contained_color, amount))
            rules.append((color, contained_in))
    return rules


def part1(graph):
    seen = set()
    search_queue = ["shiny gold"]
    count = 0
    while search_queue:
        color = search_queue[0]
        search_queue = search_queue[1:]

        if color in seen:
            continue

        seen.add(color)
        node = graph[color]
        search_queue.extend([n.color for n in node.contained_in])
        count += 1

    return count - 1


def part2(graph):
    def count_bags(node):
        count = 1
        for contained_node, amount in node.contains.items():
            count += amount * count_bags(contained_node)
        return count

    return count_bags(graph["shiny gold"]) - 1


def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        rules = parse_lines_into_rules(lines)
        graph = build_graph(rules)

    print(part1(graph))
    print(part2(graph))


if __name__ == '__main__':
    main()
