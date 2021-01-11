def main():
    h1 = int(input())
    m1 = int(input())
    s1 = int(input())
    h2 = int(input())
    m2 = int(input())
    s2 = int(input())
    moment1 = h1 * 60 * 60 + m1 * 60 + s1
    moment2 = h2 * 60 * 60 + m2 * 60 + s2
    moment = moment2 - moment1
    print(moment, end='')


if __name__ == "__main__":
    main()
