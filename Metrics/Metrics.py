import numpy as np

def confusion_matrix(prediction, ytest, type):
    
    n=0
    dim=[]

    for i in ytest:
        if not dim.__contains__(i): # getting the classes
            n += 1
            dim.append(i)

    matrix=np.zeros((len(dim), len(dim))) # Making a square matrix with the size of classes

    for i in range(len(ytest)):
        matrix[prediction[i]-1][ytest[i]-1] += 1  # Making the matrix
    
    if type==0: # This partition is for classification_report usage
        return matrix   
    else:
        return matrix, dim


def classification_report(prediction, ytest):

    matrix, dim=confusion_matrix(prediction, ytest, 1)
    vert_sum=np.sum(matrix, axis=0) # sum of columns
    hor_sum=np.sum(matrix, axis=1) # sum of rows

    precision=[]
    recall=[]

    print(matrix)

    print("\tprecision  recall  f1-score  support\n")
    
    for i in dim:
        precision.append(round(matrix[i-1][i-1]/hor_sum[i-1], 2))
        recall.append(round(matrix[i-1][i-1]/vert_sum[i-1], 2))
        
        print(" "+str(i)+"\t"+str(precision[i-1])+"\t"+str(recall[i-1])+"\t"+str(round(2*((precision[i-1]*recall[i-1])/(precision[i-1]+recall[i-1])),2))+"\t"+str(np.sum(hor_sum[i-1])))

    diagonal_sum = [matrix[x][x] for x in range(len(matrix))]
    diagonal_sum = sum(diagonal_sum)

    print()
    print("accuracy:\t\t"+str(round(diagonal_sum/np.sum(matrix), 2))+"\t"+str(sum(hor_sum)))

    print("macro avg:\t"+str(round(sum(precision)/len(dim), 2))+"\t"+str(round(sum(recall)/len(dim), 2))+"\t"+str(round(diagonal_sum/np.sum(matrix), 2)))
    

def mean_squarred_error(x , y):
    sum=0
    for i, j in zip(x,y):
        sum += ((i-j)**2) # Squaring the differance rate
    return sum/(len(x)) # Averaging the sum


x=[1,1,2,3,3,1,4]
y=[1,2,2,3,3,4,4]
print(mean_squarred_error(x, y))


""" 
===========================================================class rep

        precision  recall  f1-score  support

 1      0.33    1.0     0.5     3.0
 2      1.0     0.5     0.67    1.0
 3      1.0     1.0     1.0     2.0
 4      1.0     0.5     0.67    1.0

accuracy:               0.71    7.0
macro avg:      0.83    0.75    0.71


===========================================================mse

1.4285714285714286

"""


