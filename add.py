A=[[4,5,5],
        [3,6,7],
        [4,9,7]]
B=[[3,5,6],
   [2,4,9],
   [4,9,6]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j]+B[i][j]

for r in result:
    print(r)