def resultFunc(number: int):
    result = GetHoursAndMinutes(number)
    return result


def GetHoursAndMinutes(number):
    hours = number // 60
    m = number % 60
    h = hours % 24
    return [h, m]


def ResultCall():
    result = resultFunc(int(input()))
    print(result[0], result[1])


if __name__ == "__main__":
    ResultCall()
