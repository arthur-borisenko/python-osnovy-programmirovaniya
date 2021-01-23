import math


class Tri:
    S = 0

    def __init__(self, n1, n2, n3):
        p = (n1 + n3 + n2) / 2
        n = p * (p - n1) * (p - n2) * (p - n3)
        if n != 0:
            sqrtr = math.sqrt(n)
            self.S = round(sqrtr, 6)


def run():
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    print(Tri(n1, n2, n3).S, end='')


if __name__ == '__main__':
    run()
