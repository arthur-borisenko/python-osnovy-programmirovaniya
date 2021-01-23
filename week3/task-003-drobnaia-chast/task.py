import logging
import math

logging.basicConfig(filename="log.log", level=logging.DEBUG)


class Chast:
    res = 0

    def __init__(self, n):
        self.res = self.doneNumber(n)

    @staticmethod
    def doneNumber(n):
        low = math.floor(n)
        return round(n - float(low), 14)


def start():
    result = Chast(float(input())).res
    print(result, end='')


if __name__ == '__main__':
    start()
