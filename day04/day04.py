fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']


def validate_byr(s):
    try:
        s = int(s)
        return 1920 <= s <= 2002
    except ValueError:
        return False


def validate_iyr(s):
    try:
        s = int(s)
        return 2010 <= s <= 2020
    except ValueError:
        return False


def validate_eyr(s):
    try:
        s = int(s)
        return 2020 <= s <= 2030
    except ValueError:
        return False


def validate_hgt(s):
    if s.endswith('cm'):
        s = s[:-2]
        try:
            s = int(s)
            return 150 <= s <= 193
        except ValueError:
            return False
    elif s.endswith('in'):
        s = s[:-2]
        try:
            s = int(s)
            return 59 <= s <= 76
        except ValueError:
            return False
    else:
        return False


def validate_hcl(s):
    valid_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    if not s.startswith('#'):
        return False
    if len(s) != 7:
        return False
    for char in s[1:]:
        if char not in valid_chars:
            return False
    return True


def validate_ecl(s):
    valid_strs = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return s in valid_strs


def validate_pid(s):
    valid_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if len(s) != 9:
        return False
    for char in s:
        if char not in valid_chars:
            return False
    return True


def part1(passports):
    required_fields = fields[:]
    required_fields.remove('cid')
    valid_count = 0
    for passport in passports:
        for field in required_fields:
            if field not in passport:
                break
        else:
            valid_count += 1
    return valid_count


def part2(passports):
    validate_fns = {
        'byr': validate_byr,
        'iyr': validate_iyr,
        'eyr': validate_eyr,
        'hgt': validate_hgt,
        'hcl': validate_hcl,
        'ecl': validate_ecl,
        'pid': validate_pid
    }
    required_fields = fields[:]
    required_fields.remove('cid')
    valid_count = 0
    for passport in passports:
        passport_fields = passport.split()
        for field in required_fields:
            if field not in passport:
                break
        else:
            for field in passport_fields:
                colon_index = field.index(':')
                if field[:colon_index] not in required_fields:
                    continue
                if not validate_fns[field[:colon_index]](field[colon_index + 1:]):
                    break
            else:
                valid_count += 1
    return valid_count


def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        passports = '\n'.join([line.strip() for line in lines]).split('\n\n')

    print(part1(passports))
    print(part2(passports))


if __name__ == '__main__':
    main()
