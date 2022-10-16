import time
import MatrixInversion
import Rankofmatrix
class Matrixops():
    #Extra required functions
    # 1.Defining a matrix
    def Matrix(self, r):
        self.mat = r
        self.rows = len(self.mat)
        self.cols = len(self.mat[0])
        return self.mat
        
    # 2.Displaying the matrix
    def disp(self, m):
        for i in range(0, len(self.mat)):
            print(self.mat[i])

    # 3.Transpose of the matrix (Used for calculating Norm)
    def transpose(self, m):
        self.mat = m
        self.rows = len(self.mat)
        self.cols = len(self.mat[0])
        self.B = [[0 for i in range(self.rows)] for j in range(self.cols)]
        for i in range(0,self.cols):
            for j in range(0, self.rows):
                self.B[i][j] = self.mat[j][i]
        return self.B
    
    # Assignment functions
    # (a) Inverse of a matrix
    def Inverse(self, m):
        print("\nThe Inverse of the given matrix is:-\n")
        MatrixInversion.Determinate(m)
        inm = MatrixInversion.Inversion_mat(m)
        for j in range(0,len(inm)):
            print(inm[j])
        
    # (b) Multiplication of two matrices
    def Multiply(self, m1,m2):
        self.rows = len(m1)
        self.cols = len(m1[0])
        rn2 = len(m2)
        cp2 = len(m2[0])
        if(self.cols == rn2):
            multi = [[0 for i in range(cp2)] for j in range(self.rows)]
            for i in range(self.rows):
                for j in range(cp2):
                    for k in range(self.cols):
                        multi[i][j] = multi[i][j]  + (m1[i][k]*m2[k][j])
            return multi
        else:
            print("Invalid matrix")
            return
    
    # (c) System of linear equations
    def sol(self,m):
        import Solutionofinearsystem
        Solutionofinearsystem.finalsol(m)

    # (d) Plotting 2D and 3D vectors
    def plots(self,m):
        import Plotting_vectors
        print("Plotting function output\nYour Input vectors are:-")
        for k in range(0,len(m)):
            print(m[k])
        Plotting_vectors.Vectorsplot(m)
    
    # (e) Norm of a matrix
    def Norm(self, m):
        sum =0
        row = len(m)
        col = len(m[0])
        for i in range(row):
            for j in range(col):
                sum = sum + math.pow(m[i][j],2)
    
        return math.sqrt(sum)
    
    # (f) Row reduction of a matrix (RREF)
    def rref(self,matrix):
        print("Row Reduced Echelon Form\nAuthor - Ved Nayi\n")
        
        import rowreducedechelon
        rowreducedechelon.Row_Reduced_Echelon_Form(m)
    # (g) Rank of a matrix    
    def Rank(self, m):
        print("Rank\nAuthor - Parv Patel")
        Rankofmatrix.Row_Reduced_Echelon_Form(m)
        Rankofmatrix.Rank_of_matrix(m)
    

m1 = Matrixops()
m = m1.Matrix([[0,1,3],[2,1,2],[1,2,3]])
# m1.disp([[1,2,3],[3,2,1],[4,3,2]])
print(m1.Norm([[1,0],[1,1]]))
# print(time.process_time())
m1.Inverse(m)
print("\n")
m1.plots([[1,2,0],[3,2,0]])
print("\n")
m1.Rank(m)
print("\n")
m1.rref(m)
print("\n")
m1.sol(m)
