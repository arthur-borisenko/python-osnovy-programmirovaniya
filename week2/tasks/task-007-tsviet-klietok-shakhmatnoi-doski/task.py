def isDiving(number, divider) -> bool:
    return number % divider == 0


def checkPos(x:int) -> int:
    if isDiving(x, 2):
        return 2
    else:
        return 3


def isUpper(pos1: list, pos2: list) -> bool:
    # pos1[0]-x1 pos2[0]-x2 pos1[1]-y1 pos2[1]-y2
    chk=checkPos(pos1[0])


def isDowner(pos1: list, pos2: list) -> bool:
    # pos1[0]-x1 pos2[0]-x2 pos1[1]-y1 pos2[1]-y2
    return pos1[0] == pos2[0] and pos1[1] - 1 == pos2[1]


def isRight(pos1: list, pos2: list) -> bool:
    # pos1[0]-x1 pos2[0]-x2 pos1[1]-y1 pos2[1]-y2
    return pos1[1] == pos2[1] and pos1[0] + 1 == pos2[0]


def isLeft(pos1: list, pos2: list) -> bool:
    # pos1[0]-x1 pos2[0]-x2 pos1[1]-y1 pos2[1]-y2
    return pos1[1] == pos2[1] and pos1[0] - 1 == pos2[0]


def isDifferentColor(x1, y1, x2, y2):
    pos1 = [x1, y1]
    pos2 = [x2, y2]
    isLeftRight = isLeft(pos1, pos2) or isRight(pos1, pos2)
    isUpDown = isUpper(pos1, pos2) or isDowner(pos1, pos2)
    return isUpDown or isLeftRight


def start():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    if isDifferentColor(x1, y1, x2, y2):
        print("NO", end='')
    else:
        print("YES", end='')


if __name__ == '__main__':
    start()
