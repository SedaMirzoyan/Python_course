def checkStatus(num1, num2, flag):
    if ((num1 >= 0 or num2 >= 0) and flag == False):
        return True
    elif ((num1 < 0 and num2 < 0) and flag == True):
        return True
    return False
    
print(checkStatus(-5, -8, True))
print(checkStatus(8, 0, False))
print(checkStatus(-5, 0, True))
print(checkStatus(0, 0, False))
print(checkStatus(3, 3, True))
