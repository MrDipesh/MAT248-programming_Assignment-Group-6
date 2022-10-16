def finalsol(Matrix):
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
        
    for h in range(len(Matrix)):
        for j in range(h,len(Matrix[0])-1):
            if Matrix[h][j] == 1:
                print("x",h+1," = ",Matrix[h][len(Matrix[0])-1])
                break
            if Matrix[h][j] == 0:
                print("x",h+1, " is a free variable!!")
                break
            elif Matrix[len(Matrix)-1][Matrix[0]-1] == 0 and Matrix[h][len(Matrix[0])-1] !=0 :
                print("This is the inconsitent system!!")
            elif Matrix[len(Matrix)-1][Matrix[0]-1] == 0 and Matrix[h][len(Matrix[0])-1] ==0 :
                print("x",h+1, " is a free variable!!")




    
