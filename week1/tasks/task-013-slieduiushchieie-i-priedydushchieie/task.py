def run(n: int) -> list:
    return ["The next number for the number ",
            n, " is ",
            n + 1, ".",
            " The previous number for the number ",
            n,
            " is ",
            n - 1,
            "."]


def main():
    result = run(int(input()))
    result4 = result[4]
    result3 = result[3]
    print(result[0],
          result[1],
          result[2],
          result3,
          result4,
          sep='')
    print(result[5],
          result[6],
          result[7],
          result[8],
          result[9],
          sep='',
          end='')


if __name__ == '__main__':
    main()
