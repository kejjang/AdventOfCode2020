from utilities.operator import OperatorBase


class Operator(OperatorBase):
    def exec(self, part: int = 1):
        self.__parse_foods()
        return (parts := {1: self.__part1, 2: self.__part2}).get(part if part in parts else 1)()

    def __part1(self) -> int:
        self.__get_dangerous_ingredient_list()
        return sum([len(i) for i in self.__foods])

    def __part2(self) -> int:
        d_list = self.__get_dangerous_ingredient_list()
        return ",".join([d_list[i] for i in sorted(d_list.keys())])

    def __parse_foods(self):
        self.__allergens: dict(list) = {}
        self.__foods = []
        for i, line in enumerate(self.data):
            ingredients, allergens = line[:-1].split(" (contains ")
            ingredients = ingredients.strip().split(" ")
            self.__foods += [ingredients]

            allergens = allergens.strip().split(", ")
            for item in allergens:
                self.__allergens[item] = self.__allergens.get(item, []) + [i]

    def __find_same_ingredient_with_same_allergen(self, allergen):
        food_list = [self.__foods[i] for i in self.__allergens[allergen]]
        intersections = set(food_list[0])
        for i in range(1, len(food_list)):
            intersections = intersections & set(food_list[i])
        return list(intersections)

    def __get_dangerous_ingredient_list(self):
        d_list = {}
        allergens = list(self.__allergens.keys())

        while 1:
            if len(allergens) == 0:
                break

            for al in allergens:
                ings = self.__find_same_ingredient_with_same_allergen(al)
                if len(ings) == 1:
                    d_list[al] = ings[0]

            for key in d_list.keys():
                if key in allergens:
                    allergens.remove(key)
                    for i in range(len(self.__foods)):
                        self.__foods[i] = [x for x in self.__foods[i] if x != d_list[key]]

        return d_list
