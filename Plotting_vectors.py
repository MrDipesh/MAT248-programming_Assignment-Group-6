from turtle import color
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def Vectorsplot(matrix):
    if(len(matrix[0]) == 3):

        fig_plot = plt.figure()
        # Defining 3d plotting projection
        axis = plt.axes(projection='3d')

        # X, Y, Z axis labelling
        axis.set_xlabel('X - Axis')
        axis.set_ylabel('Y - Axis')
        axis.set_zlabel('Z - Axis')

        x = []
        y = []
        z = []

        for i in range(len(matrix)):
            x.append(np.linspace(0,matrix[i][0],100))
            y.append(np.linspace(0,matrix[i][1],100))
            z.append(np.linspace(0,matrix[i][2],100))
    
            if(matrix[i][1]==0):
                axis.plot3D(x[i],z[i],zs=0,zdir ='y', color = 'red')
            elif(matrix[i][2]==0):
                axis.plot3D(x[i],y[i],zs=0,zdir ='z', color = 'red')
            elif(matrix[i][0]==0):
                axis.plot3D(y[i],z[i],zs=0,zdir ='x', color = 'green')
            else:
                axis.plot3D(x[i], y[i], z[i], 'red')
        plt.show()

