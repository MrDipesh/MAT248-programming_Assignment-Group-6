def Multiply(m1,m2):
    # mxn1 matrix-1
    rm1 = len(m1) # m
    cn1 = len(m1[0]) # n1

    # n2xp matrix-2
    rn2 = len(m2) # n2
    cp2 = len(m2[0]) # p

    # Checking validation for matrix multiplication
    if(cn1 == rn2):
        multi = [[0 for i in range(cp2)] for j in range(rm1)]

        # M1 matrix ith row
        for i in range(rm1):

            # M2 matrix jth column
            for j in range(cp2):

                # sum of product of (m1 matrix ith row and kth column) and (m2 matrix kth row and jth column)
                for k in range(cn1):
                    multi[i][j] = multi[i][j]  + (m1[i][k]*m2[k][j])
                
        return multi
    
    else:
        print("Invalid matrix")
        return

Matrix1 = [[1,0],[1,1]]
Matrix2 = [[1,1],[0,1]]

ans = Multiply(Matrix1,Matrix2)
print(ans)
