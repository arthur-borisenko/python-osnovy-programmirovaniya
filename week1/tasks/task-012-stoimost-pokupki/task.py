def GetCost(number):
    h = number // 100
    m = number % 100
    return [h, m]


def run(a, b, n):
    v = b + a * 100
    res = GetCost(v * n)
    return res


def ResultCall():
    result = run(int(input()), int(input()), int(input()))
    print(result[0], result[1])


if __name__ == '__main__':
    ResultCall()
