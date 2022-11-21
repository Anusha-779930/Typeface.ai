M = [[1,0,0,1,1],[1,0,0,0,1],[1,0,0,1,1],[1,1,1,1,1]]
A = [255,255]
B = [255,0]
C = [0,255]
D = [0,0]
for i in range(len(M)):
    for j in range(len(M[0])):
        if M[i][j] == 0:
            if A[0] > i:
                A[0] = i
            if A[1] > j:
                A[1] = j
            if B[0] > i:
                B[0] = i
            if B[1] < j:
                B[1] = j
            if C[0] < i:
                C[0] = i
            if C[1] > j:
                C[1] = j
            if D[0] < i:
                D[0] = i
            if D[1] < j:
                D[1] = j

if A[1] != C[1]:
    A[1] = min(A[1],C[1])
    C[1] = min(A[1],C[1])
if A[0] != B[0]:
    A[0] = min(A[0],B[0])
    B[0] = min(A[0],B[0])
if B[1] != D[1]:
    B[1] = max(B[1],D[1])
    D[1] = max(B[1],D[1])
if C[0] != rb[0]:
    C[0] = max(C[0],D[0])
    D[0] = max(C[0],D[0])
print(A,B,C,D)
