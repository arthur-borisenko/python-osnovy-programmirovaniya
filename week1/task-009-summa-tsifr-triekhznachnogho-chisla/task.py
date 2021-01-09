number=int(input())
def fasterFunc(n):
    stringN=str(n)
    intN1=int(stringN[0])
    intN2 = int(stringN[1])
    intN3 = int(stringN[2])
    return intN1+intN2+intN3
def naiveFunc(n):
    res=0
    for i in range(len(str(n))):
        el=int(str(n)[i])
        res+=el
    return res
print(fasterFunc(number))
