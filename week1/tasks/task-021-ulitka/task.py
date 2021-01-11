def main():
    h = int(input())
    a = int(input())
    b = int(input())
    minSpeed = a - b
    print((h - b-1) // minSpeed + 1, end='')


if __name__ == '__main__':
    main()
