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

def Rank_of_matrix(my_matrix):      #function to find out the rank of the given matrix 
    count =0
    for h in range(len(my_matrix)):
        for k in range(len(my_matrix[0])):
            if my_matrix[h][k] == 1:        #compare the element is 1 then increment 1 and break the inner for loop
                count+=1
                break
    for y in range(0,len(my_matrix)):
        for z in range(0,len(my_matrix[0])):
            my_matrix[y][z] = round(my_matrix[y][z],2)
    
    for g in range(0,len(my_matrix)):
        print(my_matrix[g])
    print("The rank of the matrix is :", count)
    

# my_matrix = [ 
#     [ 1, 27, 1, -4],
#     [ 1, 27, 1, -4],
#     [ 0, 3, 0, 1]]

# Row_Reduced_Echelon_Form( my_matrix )
    
# Rank_of_matrix(my_matrix)