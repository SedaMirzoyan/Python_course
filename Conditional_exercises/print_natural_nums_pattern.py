def natural_nums_pattern(n):  
    nums = []
    for i in range(1, n+1):
        nums.append(i)
    str_nums = map(str,nums)

    for_print = " + ".join(str_nums)
    sum_nums = str(sum(nums))

    out = for_print + " = " + sum_nums
    
    return out

def main():
    n = 5

    i = 1
    while (i <= n):
        print(natural_nums_pattern(i))
        i += 1

if __name__ == "__main__":
    main()
