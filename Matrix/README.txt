1. Assigning Subsequent Rows to Matrix first row elements
Given a (N + 1) * N Matrix, assign each column of 1st row of matrix, the subsequent row of Matrix.

Input : test_list = [[5, 8, 10], [2, 0, 9], [5, 4, 2], [2, 3, 9]] 
Output : {5: [2, 0, 9], 8: [5, 4, 2], 10: [2, 3, 9]} 

Input : test_list = [[5, 8], [2, 0], [5, 4]] Output : {5: [2, 0], 8: [5, 4]} 
Explanation : 5 paired with 2nd row, 8 with 3rd.

2. Adding and Subtracting Matrices 

3. Group similar elements into Matrix

Input : test_list = [1, 3, 4, 4, 2, 3] 
Output : [[1], [2], [3, 3], [4, 4]] 

Input : test_list = [1, 3, 4, 2] 
Output : [[1], [2], [3], [4]]

4. Create an n x n square matrix, where all the sub-matrix have the sum of opposite corner elements as even

Input: 4 
Output:
1 2 3 4
8 7 6 5
9 10 11 12
16 15 14 13

5. Row-wise element Addition in Tuple Matrix

Input : test_list = [[(‘Gfg’, 3)], [(‘best’, 1)]] cus_eles = [1, 2] 
Output : [[(‘Gfg’, 3, 1)], [(‘best’, 1, 2)]] 

Input : test_list = [[(‘Gfg’, 6), (‘Gfg’, 3)]] cus_eles = [7] 
Output : [[(‘Gfg’, 6, 7), (‘Gfg’, 3, 7)]]