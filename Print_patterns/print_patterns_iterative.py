#print patterns iterative

def full_pyramid(n):
    for i in range(1, n+1):
        for j in range(1,n-i+1):
            print(" ", end="")
        for j in range(1, 2*i):
            print("*", end="")
        print("")
   

def full_pyramid_alphabets(n):
    ch_num = ord('A')
    for i in range(1, n+1):
        for j in range(1,n-i+1):
            print(" ", end="")
        for j in range(1, i+1):
            print(chr(ch_num + j -1) + " ", end="")
        print("") 


def full_pyramid_nums(n):
    for i in range(1, n+1):
        for j in range(1,n-i+1):
            print(" ", end="")
        for j in range(1, 2*i):
            print(j, end="")
        print("")


def inv_full_pyramid(n):        
    for i in range(n, 0, -1):
        for j in range(1, n-i+1):
            print(" ", end="")
        for j in range(1, 2*i):
            print("*", end="")
        print("")



def full_hollow_pyramid(n):     
    for i in range(1, n+1):
        for j in range(1, 2*n):
            if(i == n or j == n-i+1 or j == n+i-1):
                print("*", end="")
            else:
                print(" ", end="")
        print("")

        
def half_pyramid(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print('* ', end="")
        print("")


def half_pyramid_with_nums(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print("")


def half_pyramid_alphabets(n):
     #ch = 'A'
     ch_num = ord('A')
     #print(ch_num)
     
     for i in range(0, n):
        for j in range(0, i + 1):
            print(chr(ch_num + i), end="")
        print("")  
    

def inv_half_pyramid(n):
    for i in range(0, n + 1):
        for j in range(0, n - i): #n-i-1
            print('*', end="")
        print("")



def inv_half_hollow_pyramid(n): 
    for i in range(1, n+1):   
        for j in range(1, n+1): 
            #print("j ", j)
            if(j == i or j == n or i == 1):
                print("*", end="")
            else:
                print(" ", end="")
        print("")
   
                  
         
def main():
    half_pyramid(5)
    half_pyramid_with_nums(5)
    half_pyramid_alphabets(5)
    inv_half_pyramid(5)
    full_hollow_pyramid(5)
    full_pyramid(5)
    full_pyramid_alphabets(5)
    full_pyramid_nums(5)
    inv_full_pyramid(5)
    inv_half_hollow_pyramid(5)


if __name__ == "__main__":
    main()