def closing_bracket_index(expression, open_bracket_index):
    depth = 0
    for i in range(open_bracket_index, len(expression)):
        if expression[i] == ')':
            depth += 1
        elif expression[i] == '(':
            depth -= 1
        if depth == 0:
            return i


def evaluate_part1(expression, rev=True):
    if rev:
        expression = expression[::-1]
    if len(expression) == 1:
        return int(expression[0])
    elif expression[0] == ')':
        close_index = closing_bracket_index(expression, 0)
        return evaluate_part1([f'{evaluate_part1(expression[1:close_index], rev=False)}'] + expression[close_index + 1:], rev=False)
    else:
        left = expression[0]
        operand = expression[1]
        rest = expression[2:]
        if operand == '+':
            return int(left) + evaluate_part1(rest, rev=False)
        elif operand == '*':
            return int(left) * evaluate_part1(rest, rev=False)


def evaluate_part2(expression):
    class CustomInt:
        def __init__(self, value):
            self.value = value

        def __add__(self, other):
            return CustomInt(self.value * other.value)

        def __mul__(self, other):
            return CustomInt(self.value + other.value)

    expression = ''.join(expression).replace('+', '-').replace('*', '+').replace('-', '*')
    for i in range(10):
        expression = expression.replace(str(i), f'CustomInt({i})')
    return eval(expression).value


def part1(expressions):
    s = 0
    for expression in expressions:
        s += evaluate_part1(expression)
    return s


def part2(expressions):
    s = 0
    for expression in expressions:
        s += evaluate_part2(expression)
    return s


def main():
    with open('input.txt', 'r') as f:
        expressions = [list(line.strip().replace(' ', '')) for line in f.readlines()]

    print(part1(expressions))
    print(part2(expressions))


if __name__ == '__main__':
    main()
