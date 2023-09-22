import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            self.contents.extend([key] * value)

    def draw(self, number):
        if number >= len(self.contents):
            return self.contents
        balls = random.sample(self.contents, number)
        for ball in balls:
            self.contents.remove(ball)
        return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0

    for _ in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        balls = new_hat.draw(num_balls_drawn)

        no_of_balls = {key: balls.count(key) for key in expected_balls}
        
        if all(no_of_balls[key] >= expected_balls[key] for key in expected_balls):
            successes += 1

    return successes / num_experiments
