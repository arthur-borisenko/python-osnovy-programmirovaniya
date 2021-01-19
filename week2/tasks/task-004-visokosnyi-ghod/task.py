def check1(n1):
    if (n1 % 4 == 0 and n1 % 100 != 0) or n1 % 400 == 0:
        return True


def start():
    n = int(input())
    if check1(n):
        print('YES', end='')
    else:
        print("NO", end="")


if __name__ == '__main__':
    start()
