import os
import re
import sys
import math


class NewsvendorProblemModel:
    def __init__(self, c, r, N, q, probs):
        self.unit_cost = c
        self.unit_price = r
        self.quantity_possible_demanded = N
        self.quantity_ordered = q
        self.probs = probs


def process(file_input):
    with open(os.path.join(sys.path[0], file_input), "r") as f:
        result = f.readlines()
        c = int(result[0])
        r = int(result[1])
        N = int(result[2])
        q = int(result[3])
        probs = [float(i) for i in result[4:4+N]]

        return NewsvendorProblemModel(c, r, N, q, probs)


def solution(model):
    expected_profit = 0
    included_probs = []
    for i in range(0, model.quantity_ordered):
        revenue = i * model.unit_price
        cost = model.quantity_ordered * model.unit_cost
        profit = revenue - cost
        expected_profit += model.probs[i] * profit
        included_probs.append(model.probs[i])

    expected_profit += (1-sum(included_probs)) * model.quantity_ordered * (model.unit_price - model.unit_cost)
    return math.floor(expected_profit)


files = [f for f in os.listdir(os.path.join(sys.path[0], '.')) if "input" in f]
files.sort(key=lambda f: int(re.sub('\D', '', f)))

for file in files:
    model = process(file)
    result = solution(model)
    print(f'''{file} : {result}''')


