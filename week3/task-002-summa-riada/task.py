class Task:
    res = 0

    def __init__(self, n):
        self.run(n)

    @staticmethod
    def getRequestedValue(i) -> int:
        return 1 / i ** 2

    def for1(self, for_content, stop: int = 0, start: int = 1):
        i = start
        while i <= stop:
            for_content(i)
            i += 1

    def content(self, i):
        self.res += self.getRequestedValue(i)

    def run(self, n):
        self.for1(lambda i: self.content(i), n)
        return self.res


def startFile():
    n = int(input())
    print(round(Task(n).res, 5), end='')


if __name__ == '__main__':
    startFile()
