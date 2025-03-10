def print_full_pyramid(i, n): 
    if(i > n):
        return -1
    
    num = int((n-i)/2)
    print(num * " " + i * "*")
    
    return print_full_pyramid(i+2, n)


def print_half_pyramid(i, n): 
    if(i > n):
        return -1
    
    print(i * "*")
    
    return print_half_pyramid(i+1, n)


print("full pyramid pattern")
print_full_pyramid(1, 7)
print("half pyramid pattern")
print_half_pyramid(1, 5)