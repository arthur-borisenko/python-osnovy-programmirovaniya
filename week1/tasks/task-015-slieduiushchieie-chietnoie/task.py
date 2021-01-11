def main():
    data = int(input())
    if data % 2 == 0:
        print(data + 2, end='')
    else:
        print(data + 1, end='')


if __name__ == '__main__':
    main()
