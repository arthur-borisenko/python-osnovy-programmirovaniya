def main():
    string = input()
    if int(string) < 10:
        print('0', end='')
    else:
        print(string[len(string) - 2], end='')


if __name__ == '__main__':
    main()
