def main():
    speed = int(input())
    path = int(input())
    if path % speed == 0:
        print(path // speed, end='')
    else:
        print(path // speed + 1, end='')


if __name__ == '__main__':
    main()
