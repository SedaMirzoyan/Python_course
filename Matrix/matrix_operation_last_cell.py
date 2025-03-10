def endpoints(matrix):
    n = len(matrix)
    m = len(matrix[0])
    j = 0
    i = 0
    directions = { "right": [i, j+1], "down": [i+1, j], "left": [i, j-1], "up": [i-1, j] }
    dir_key = "right"

    while((i >= 0 and j < m) and (i < n and j >=0)):
        if(matrix[i][j] == 1):
            matrix[i][j] = 0
            if(dir_key == "right"):
                dir_key = "down"
            elif(dir_key == "down"):
                dir_key = "left"
            elif(dir_key == "left"):
                dir_key = "up"
            elif(dir_key == "up"):
                dir_key = "right"

        i += directions[dir_key][0]  
        j += directions[dir_key][1]  

        coords = (i- directions[dir_key][0], j-directions[dir_key][1])

    return coords

            

def main():
    matrix = [[0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 0, 0]]


    print(matrix)
    print(endpoints(matrix))

if __name__ == "__main__":
    main()
