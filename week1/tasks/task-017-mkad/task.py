def main():
    speed = int(input())
    time = int(input())
    totalPath = speed * time
    print(totalPath % 109, end='')


if __name__ == '__main__':
    main()
