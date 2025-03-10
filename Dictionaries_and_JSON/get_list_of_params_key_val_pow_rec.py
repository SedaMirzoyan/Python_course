#get parameter list
def get_params_list(*args): 
    sqr = [ i*i for i in args]
    return sqr
    

#keyword arguments
def get_key_val_pair(**kwargs):
    cube = { pow(v, 3) for k, v in kwargs.items()}
    return cube


#Function that Accept Variable Length Key Value Pair as Arguments
def get_stud_info(**kwargs):
    info = { k: (v, len(k))  for k, v in kwargs.items()}
    return info
    

#find the power of a number using recursion
def num_pow(num, power):
    if( power <= 1):
        return num
    
    return num * num_pow(num, power-1)
    


def main():
    print(get_params_list(1, 2, 3, 4, 5, 6))
    print(get_key_val_pair(a= 1, b= 2, c= 3, d= 4, e=5))
    print(get_stud_info(name = "Roger", country = "USA", mark = "95", university = "Harvard"))
    print(num_pow(5, 3))

    #print multiple arguments
    
    name = input("Please enter name of John's friend's name:")
    age = int(input("Please enter friend's age:"))
    print(f"There is a short dialogue between John and {name}")
    print(f"John: Hello {name}, how old are you?")
    print(f"{name}: Hii John, I am {age} years old")
    
    


if __name__=="__main__":
    main()
