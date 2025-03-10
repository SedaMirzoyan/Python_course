#Create an n x n square matrix, where all the sub-matrix have the sum of opposite corner elements as even
import numpy as np

def check_submatrix(n):
    num_list = np.arange(1, (n**2)+1).reshape(n,n)
    print(num_list)

    temp_row = num_list[0]
    num_list_new = []

    for i in range(0, n):
        for j in range(0, n):
            if(i%2 == 1):
                if(j == i):
                    temp_row = np.flipud(num_list[i]) 
            else:
                temp_row = num_list[i]
        num_list_new.append(temp_row)

    out = np.array(num_list_new).tolist()

    return out


def main():
    num = 4
    print(check_submatrix(num))

if __name__=="__main__":
    main()