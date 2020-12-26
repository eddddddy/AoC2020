def parse_into_foods(lines):
    foods = []
    for line in lines:
        ingredients = line[:line.index('(')].strip()
        ingredients = ingredients.split()
        allergens = line[line.index('(') + 10:-1]
        allergens = allergens.split(', ')
        foods.append((ingredients, allergens))
    return foods


def get_foods_containing_allergen(foods, allergen):
    food_list = []
    for ingredients, allergens in foods:
        if allergen in allergens:
            food_list.append((ingredients, allergens))
    return food_list


def part1(foods):
    all_ingredients = [ingredient for ingredients, _ in foods for ingredient in ingredients]
    all_allergens = set([allergen for _, allergens in foods for allergen in allergens])
    all_ingredients_set = set(all_ingredients)
    ingredients_without_allergens = set()
    for ingredient in all_ingredients_set:
        for allergen in all_allergens:
            food_list = get_foods_containing_allergen(foods, allergen)
            if all([ingredient in food for food, _ in food_list]):
                break
        else:
            ingredients_without_allergens.add(ingredient)

    count = 0
    for ingredient in all_ingredients:
        if ingredient in ingredients_without_allergens:
            count += 1
    return count


def part2(foods):
    all_allergens = set([allergen for _, allergens in foods for allergen in allergens])
    allergen_map = {}
    for allergen in all_allergens:
        food_list = get_foods_containing_allergen(foods, allergen)
        possible_ingredients = set(food_list[0][0])
        for ingredients, allergens in food_list:
            possible_ingredients = possible_ingredients.intersection(set(ingredients))
        allergen_map[allergen] = possible_ingredients

    for _ in range(len(allergen_map)):
        new_allergen_map = allergen_map.copy()
        for allergen in allergen_map:
            if len(allergen_map[allergen]) == 1:
                ingredient = list(allergen_map[allergen])[0]
                for al_ in new_allergen_map:
                    if al_ != allergen and ingredient in new_allergen_map[al_]:
                        new_allergen_map[al_].remove(ingredient)
        allergen_map = new_allergen_map

    sorted_allergens = sorted(allergen_map.items())
    return ','.join([list(ingredient)[0] for allergen, ingredient in sorted_allergens])


def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        foods = parse_into_foods(lines)

    print(part1(foods))
    print(part2(foods))


if __name__ == '__main__':
    main()
