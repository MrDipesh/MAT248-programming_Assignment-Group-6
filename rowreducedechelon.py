
def Row_Reduced_Echelon_Form(Matrix):
    if not Matrix: 
        return

    lead = 0
    rowCount = len(Matrix)
    columnCount = len(Matrix[0])

    for row in range(rowCount):
        if lead >= columnCount:
            return
        i = row
        while Matrix[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = row
                lead += 1
                if columnCount == lead:
                    return
        Matrix[i],Matrix[row] = Matrix[row],Matrix[i]
        lv = Matrix[row][lead]
        Matrix[row] = [ mrx / float(lv) for mrx in Matrix[row]]
        for i in range(rowCount):
            if i != row:
                lv = Matrix[i][lead]
                Matrix[i] = [ iv - lv*rv for rv,iv in zip(Matrix[row],Matrix[i])]
        lead += 1

    for k in range(0,len(Matrix)):
        for p in range(0,len(Matrix[0])):
            Matrix[k][p] = round(Matrix[k][p],1)
        
    for u in range(0,len(Matrix)):
        print(Matrix[u])



# Row_Reduced_Echelon_Form( my_matrix )

# print("Row reduced echelon form of matrix is given below:\n")
# for i in range(len(my_matrix)):
#     for j in range(len(my_matrix[0])):
#         if my_matrix[i][j] == 0:
#             print("0  ",end=' ')
#         else:
#             print(my_matrix[i][j],'  ',end=' ')
#     print()