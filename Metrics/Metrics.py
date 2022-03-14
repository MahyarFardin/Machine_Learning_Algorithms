from matplotlib.pyplot import axis
import numpy as np

def confusion_matrix(prediction, ytest, type):
    
    n=0
    dim=[]

    for i in ytest:
        if not dim.__contains__(i):
            n += 1
            dim.append(i)

    matrix=np.zeros((len(dim), len(dim)))

    for i in range(len(ytest)):
        matrix[prediction[i]-1][ytest[i]-1] += 1
    
    if type==0:
        return matrix
    else:
        return matrix, dim


def classification_report(prediction, ytest):
    matrix, dim=confusion_matrix(prediction, ytest, 1)
    vert_sum=np.sum(matrix, axis=0)
    hor_sum=np.sum(matrix, axis=1)

    print(matrix)

    print("\tprecision  recall  f1-score  support\n")
    
    for i in dim:
        
        print(" "+str(i)+"\t"+str(round(matrix[i-1][i-1]/hor_sum[i-1], 2))+"\t"+
        str(round(matrix[i-1][i-1]/vert_sum[i-1], 2))+"\t"+"Temp"+"\t"+str(np.sum(hor_sum[i-1])))

    diagonal_sum = [matrix[x][x] for x in range(len(matrix))]
    diagonal_sum = sum(diagonal_sum)

    print()
    print("accuracy: "+18*" "+str(round(diagonal_sum/np.sum(matrix), 2)))
#def mean_squarred_error:

x=[1,1,2,3,3,1,4]
y=[1,2,2,3,3,4,4]
print(classification_report(x, y))