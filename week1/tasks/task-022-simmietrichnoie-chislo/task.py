def fill(n: str) -> str:
    string = ""
    if len(n) < 4:
        nullCount = 4 - len(n)
        for i in range(nullCount):
            string = string + "0"
    return string + n


def simetric_check(n: str) -> bool:
    splitted = list(n)
    reversedList = splitted.copy()
    reversedList.reverse()
    if reversedList == splitted:
        return 1
    else:
        return 0


def main():
    print(simetric_check(fill(input())), end='')


if __name__ == '__main__':
    main()
