# Elnaz Samavsti
# مسئله دریاچه به وسیله
# hill climbing

import random


def lake_function(x):
    return ((x-3)*(x-3)*(x-3)*(x+1)*(x+1))


def hill_climbing():
    current = random.uniform(-5, 5)
    step = 0.1

    while True:
        next_point = current + random.uniform(-step, step)
        if lake_function(next_point) < lake_function(current):
            current = next_point

        if lake_function(current) < 0.01:
            break

    return current


best_solution = hill_climbing()
print("The most optimal way to move to the point:", best_solution)
print("The optimal value of the function at this point:",
      lake_function(best_solution))
