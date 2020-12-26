def parse_ticket_fields_to_set(rules):
    ticket_field_sets = {}
    for line in rules:
        split_line = line.split()
        name = ' '.join(split_line[:-3])
        first_range = split_line[-3]
        second_range = split_line[-1]
        first_range = set(range(int(first_range.split('-')[0]), int(first_range.split('-')[1]) + 1))
        second_range = set(range(int(second_range.split('-')[0]), int(second_range.split('-')[1]) + 1))
        ticket_field_sets[name[:-1]] = first_range.union(second_range)
    return ticket_field_sets


def part1(ticket_field_sets, nearby_tickets):
    valid_field_range = set().union(*ticket_field_sets.values())
    error_rate = 0
    invalid_tickets = []
    for ticket in nearby_tickets:
        for field in ticket:
            if field not in valid_field_range:
                error_rate += field
                if ticket not in invalid_tickets:
                    invalid_tickets.append(ticket)
    return error_rate, invalid_tickets


def part2(ticket_field_sets, ticket, nearby_tickets):
    invalid_tickets = part1(ticket_field_sets, nearby_tickets)[1]
    nearby_tickets = [nearby_ticket for nearby_ticket in nearby_tickets if nearby_ticket not in invalid_tickets]

    index_to_field_map = {}
    still_to_match = set(range(len(ticket)))
    still_names_to_match = set(ticket_field_sets.keys())
    while still_to_match:
        still_to_match_copy = still_to_match.copy()
        for index in still_to_match:
            possible_field_names = still_names_to_match.copy()
            for nearby_ticket in nearby_tickets:
                for field in still_names_to_match:
                    if nearby_ticket[index] not in ticket_field_sets[field]:
                        if field in possible_field_names:
                            possible_field_names.remove(field)
            if len(possible_field_names) == 1:
                field_name = list(possible_field_names)[0]
                index_to_field_map[index] = field_name
                still_to_match_copy.remove(index)
                still_names_to_match.remove(field_name)
        still_to_match = still_to_match_copy

    product = 1
    for index, field in index_to_field_map.items():
        if field.startswith('departure'):
            product *= ticket[index]
    return product


def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        rules, ticket, nearby_tickets = '\n'.join(lines).split('\n\n')
        ticket_field_sets = parse_ticket_fields_to_set(rules.split('\n'))
        ticket = [int(num) for num in ticket.split('\n')[1].split(',')]
        nearby_tickets = [[int(num) for num in ticket.split(',')] for ticket in nearby_tickets.split('\n')[1:]]

    print(part1(ticket_field_sets, nearby_tickets)[0])
    print(part2(ticket_field_sets, ticket, nearby_tickets))


if __name__ == '__main__':
    main()
