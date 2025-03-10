def check_if_prime(num):
    if (num == 0):
        print("Zero is neither prime, nor composite")

    if(((num % 2 == 0) and (num != 2)) or ((num % 3 == 0) and (num != 3)) or ((num % 5 == 0) and num != 5)):
        return False
    return True


input_list = [ 5, 15, 1, 0, 25, 2, 11]

for i in input_list:
    print(check_if_prime(i))
