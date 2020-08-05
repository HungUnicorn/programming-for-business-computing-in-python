"""
Within distance d, choose p cities out of n cites that cover the most population

City contains coordinate (x, y) and population

Use greedy algorithm
Always choose the city has the most population. If equal, choose the one with smaller id
"""
import math
import os
import sys


class SiteSelectionModel:
    def __init__(self, n, p, d, cities):
        self.num_city = n
        self.num_chosen_city = p
        self.distance_limit = d
        self.cities = cities


class City:
    def __init__(self, city_id, x, y, population):
        self.city_id = city_id
        self.x = x
        self.y = y
        self.population = population


def process(file_input):
    with open(os.path.join(sys.path[0], file_input), "r") as f:
        result = f.readlines()
        n, p, d = [int(i) for i in result[0].split(" ")]
        temp_cites = [[int(j) for j in i.split(" ")] for i in result[1:1 + n]]
        cities = []
        index = 1
        for temp_city in temp_cites:
            cities.append(City(index, temp_city[0], temp_city[1], temp_city[2]))
            index += 1

        return SiteSelectionModel(n, p, d, cities)


def calculate_distance(city1, city2):
    square = pow(city1.x - city2.x, 2) + pow(city1.y - city2.y, 2)
    return math.sqrt(square)


def find_city_neighbors(cities, distance_limit):
    city_neighbors = {}

    for city in cities:
        others = cities.copy()
        others.remove(city)
        neighbors = []

        for other in others:
            city_distance = calculate_distance(city, other)
            if city_distance <= distance_limit:
                neighbors.append(other)
        city_neighbors[city] = neighbors

    return city_neighbors


def solution(site_selection_model):
    chosen_cities = []
    already_covered = []
    sum_covered_population = 0

    city_neighbors = find_city_neighbors(site_selection_model.cities, site_selection_model.distance_limit)

    while len(chosen_cities) < site_selection_model.num_chosen_city:
        max_covered_population = 0
        chosen_city = None

        for city, neighbors in city_neighbors.items():
            diff_covered_and_neighbors = list(set(neighbors) - set(already_covered))
            covered_population = city.population + sum(c.population for c in diff_covered_and_neighbors)

            if covered_population > max_covered_population:
                max_covered_population = covered_population
                chosen_city = city

        if chosen_city is not None:
            already_covered.append(chosen_city)
            already_covered.extend(city_neighbors[chosen_city])

        sum_covered_population += max_covered_population
        chosen_cities.append(chosen_city)

        for covered_city in already_covered:
            try:
                del city_neighbors[covered_city]
            except KeyError:
                pass
                # print(f'''Already deleted: {covered_city.city_id}''')
    if chosen_cities:
        print(f'{" ".join([str(city.city_id) for city in chosen_cities])} {sum_covered_population}')
    else:
        print(sum_covered_population)


solution(process("input_ex"))
solution(process("input1"))
solution(process("input2"))
solution(process("input3"))
solution(process("input4"))
solution(process("input5"))
