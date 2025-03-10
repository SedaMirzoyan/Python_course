
def neg(num):
    if (num < 0):
        print(f"Num {num} is negative, adding by 1")
        num += 1   
    else:
        print(f"Num {num} is not negative")
    
    while(num <= 0):
        print(num)
        num += 1

def pos(num):
    if (num >= 0):
        print(f"Num {num} is positive, subtracting by 1")
        num -= 1
    else:
        print(f"Num {num} is not positive")

    while(num >= 0):
        print(num)
        num -= 1

neg(5)
neg(-3)
pos(8)
pos(-7)
