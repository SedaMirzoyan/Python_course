def add_elems(matrix1, matrix2):
    row = len(matrix1)
    col = len(matrix1[0])
    sum_list = [] 

    elem = [[matrix1[i][j] + matrix2[i][j] for j in range(0,col)] for i in range(0,row)]

    for i in elem:
        sum_list.append(i)
     
    return sum_list


def sub_elems(matrix1, matrix2):
    row = len(matrix1)
    col = len(matrix1[0])
    sub_list = [] 

    elem = [[matrix1[i][j] - matrix2[i][j] for j in range(0,col)] for i in range(0,row)]

    for i in elem:
        sub_list.append(i)
     
    return sub_list


A = [[1,2],[3,4], [5, 8]]
B = [[4,5],[6,7], [9, 3]]
print(add_elems(A, B))
print(sub_elems(A, B))