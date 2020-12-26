from itertools import product


class Node:
    def __init__(self, rule):
        self.rule = rule
        self.children = []

    def get_valid_messages(self):
        if ('a',) in self.children:
            return {'a'}
        elif ('b',) in self.children:
            return {'b'}
        else:
            messages = set()
            for child in self.children:
                if len(child) == 1:
                    messages.update(child[0].get_valid_messages())
                else:
                    left_messages = child[0].get_valid_messages()
                    right_messages = child[1].get_valid_messages()
                    concat_messages = product(left_messages, right_messages)
                    concat_messages = [''.join(message) for message in concat_messages]
                    messages.update(concat_messages)
            return messages


def parse_rules(rules):
    def initialize_node(num):
        if num not in nodes:
            rule_node = Node(num)
            nodes[num] = rule_node

    nodes = {}
    for rule in rules:
        rule_num = int(rule[:rule.index(':')])
        productions = rule[rule.index(':') + 1:]

        initialize_node(rule_num)

        if 'a' in productions:
            nodes[rule_num].children = [('a',)]
        elif 'b' in productions:
            nodes[rule_num].children = [('b',)]
        elif '|' not in productions:
            productions = productions.split()
            if len(productions) == 1:
                num = int(productions[0])
                initialize_node(num)
                nodes[rule_num].children = [(nodes[num],)]
            else:
                left_num, right_num = [int(num) for num in productions]
                initialize_node(left_num)
                initialize_node(right_num)
                nodes[rule_num].children = [(nodes[left_num], nodes[right_num])]
        else:
            production1, production2 = [production.strip() for production in productions.split('|')]
            production1, production2 = production1.split(), production2.split()
            children = []
            if len(production1) == 1:
                num = int(production1[0])
                initialize_node(num)
                children.append((nodes[num],))
            else:
                left_num1, right_num1 = [int(num) for num in production1]
                initialize_node(left_num1)
                initialize_node(right_num1)
                children.append((nodes[left_num1], nodes[right_num1]))
            if len(production2) == 1:
                num = int(production2[0])
                initialize_node(num)
                children.append((nodes[num],))
            else:
                left_num2, right_num2 = [int(num) for num in production2]
                initialize_node(left_num2)
                initialize_node(right_num2)
                children.append((nodes[left_num2], nodes[right_num2]))
            nodes[rule_num].children = children
    return nodes


def part1(rules, messages):
    count = 0
    valid_messages_42 = rules[42].get_valid_messages()
    valid_messages_31 = rules[31].get_valid_messages()
    for message in messages:
        if len(message) != 24:
            continue
        chunk1, chunk2, chunk3 = message[:8], message[8:16], message[16:]
        if chunk1 in valid_messages_42 and chunk2 in valid_messages_42 and chunk3 in valid_messages_31:
            count += 1
    return count


def part2(rules, messages):
    count = 0
    valid_messages_42 = rules[42].get_valid_messages()
    valid_messages_31 = rules[31].get_valid_messages()
    for message in messages:
        if len(message) % 8 != 0:
            continue
        chunks = [message[i:i + 8] for i in range(0, len(message), 8)]
        if not all([chunk in valid_messages_42 or chunk in valid_messages_31 for chunk in chunks]):
            continue
        chunk_rules = []
        for chunk in chunks:
            if chunk in valid_messages_42:
                chunk_rules.append(42)
            else:
                chunk_rules.append(31)
        if 31 not in chunk_rules:
            continue
        switch_index = chunk_rules.index(31)
        if not all([rule == 42 for rule in chunk_rules[:switch_index]]):
            continue
        if not all([rule == 31 for rule in chunk_rules[switch_index:]]):
            continue
        if 2 * switch_index <= len(chunk_rules):
            continue
        count += 1
    return count


def main():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
        rules, messages = [line.strip().split('\n') for line in '\n'.join(lines).split('\n\n')]
        rules = parse_rules(rules)

    print(part1(rules, messages))
    print(part2(rules, messages))


if __name__ == '__main__':
    main()
