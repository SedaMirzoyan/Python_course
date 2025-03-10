def printIncreasingPower(num):
    result, res = 1, 1
    while(res < num):
        result = pow(res, 2)
        print(result)
        res += 1

printIncreasingPower(5)
