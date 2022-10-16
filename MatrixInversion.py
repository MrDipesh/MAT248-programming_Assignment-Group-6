# Name     : Solanki Dipesh A.
# Roll no. : AU2140150
# Question : (a). Inverse of a Matrix


def small_matrix(omt, row, col):
    # creating a sub-matrix :-)
    smatrix = [i[:col] + i[col+1:] for i in (omt[:row] + omt[row+1:])]
    return smatrix

def Determinate(matrix):
    # determinate for matrix :-)
    if (len(matrix) == len(matrix[0])):  # check for valid matrix :-)

        nr = len(matrix)
        for i in range(nr):
            if nr != len(matrix[i]):
                print("Invalid matrix :-( ")
                return 0        
        if(nr == 2): # determinate for 2x2 matrix and breaking condition for recursion :-)
            delta = (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])
            return delta
        
        else:
            delta = 0
            for i in range(nr):

                delta += ((-1)**i)*(matrix[0][i])*(Determinate(small_matrix(matrix,0,i)))

            return delta
    else:
        print("Invalid matrix :-( ")
        return 0

def Inversion_mat(matrix):

    delta = Determinate(matrix)
    if(delta != 0): # If matrix is an invertible matrix :-)
        delta = abs(delta)
        nr = len(matrix)
        nc = len(matrix[0])
        for i in range(nr):
            if nr != len(matrix[i]):
                print("Invalid matrix :-( ")
                return 0

        inverseM = [[[0] for j in range(nc)] for i in range(nr)]

        if (nr==2):
            # if the matrix is 2x2 matrix :-)
            inverseM[0][0] = matrix[1][1]/Determinate(matrix)
            inverseM[1][1] = matrix[0][0]/Determinate(matrix)
            inverseM[0][1] = (-1)*matrix[1][0]/Determinate(matrix)
            inverseM[1][0] = (-1)*matrix[0][1]/Determinate(matrix)

        else:
            # calculating the cofactors of at ith,jth position and transposing with jth,ith position :-) 
            for i in range(nr):

                for j in range(i,nc):
                    inverseM[i][j] = ((-1)**(i+j))*(float)(Determinate(small_matrix(matrix, i, j)))*(1/delta)
                    inverseM[j][i] = ((-1)**(i+j))*(float)(Determinate(small_matrix(matrix, j, i)))*(1/delta)
                    
                    if(i !=j):
                        tmp = inverseM[i][j]
                        inverseM[i][j] = inverseM[j][i]
                        inverseM[j][i] = tmp

        return inverseM
    
    else:
        print(" => This matrix is not invertible : ")
        return -1


# Demo_Matrix = [[0,1],[2,1]]
# print(Determinate(Demo_Matrix))
# inm = Inversion_mat(Demo_Matrix)
# for i in range(len(inm)):
#     for j in range(len(inm[0])):
#         print((inm[i][j]),end =" , ")
#     print("\n")