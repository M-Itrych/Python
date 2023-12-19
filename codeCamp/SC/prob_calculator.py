import copy
import random


class Hat:
    def __init__(self, **colors):
        self.contents = self.contents = [key for key, value in colors.items() for _ in range(value)]

    def draw(self, draws):
        if draws > len(self.contents):
            return self.contents
        return random.sample(self.contents, draws)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for _ in range(num_experiments):
        expected_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        colors_gotten = hat_copy.draw(num_balls_drawn)

        for color in colors_gotten:
            if color in expected_copy:
                expected_copy[color] -= 1

        if all(x <= 0 for x in expected_copy.values()):
            count += 1

    return count / num_experiments


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(probability)