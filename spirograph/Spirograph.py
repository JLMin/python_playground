import math
import random


class Spirograph:
    """ Explore the math at: https://en.wikipedia.org/wiki/Spirograph """

    def __init__(self, R, r, l):
        self.R = int(R)
        self.r = int(r)
        self.k = r / float(R)
        self.l = l
        self.rotate = self.r // math.gcd(self.R, self.r)

    @staticmethod
    def with_random_size(max_size):
        R = random.randint(50, max_size // 2)
        r = random.randint(10, 9 * R // 10)
        l = random.uniform(0.1, 0.9)
        return Spirograph(R, r, l)

    def _pos(self, theta):
        R, k, l = self.R, self.k, self.l
        x = R * ((1 - k) * math.cos(theta) + l * k * math.cos((1 - k) * theta / k))
        y = R * ((1 - k) * math.sin(theta) - l * k * math.sin((1 - k) * theta / k))
        return x, y

    def start_pos(self):
        return self._pos(0)

    def gen_pos(self):
        for angle in range(0, 360 * self.rotate + 5, 5):
            theta = math.radians(angle)
            yield self._pos(theta)
