def confusion_matrix(prediction, ytest):
    matrix=[]
    n=0
    dim=[]

    for i in ytest:
        if not dim.__contains__(i):
            n += 1
            dim.append(i)


    for i in range(len(dim)):
        matrix.append([])

        for j in range(len(dim)):
            matrix[n].append([])
        
        n += 1

    for i in prediction:
        matrix[prediction[i]][ytest[i]] += 1
    
    return matrix


#def classification_report():
#def mean_squarred_error:

x=[1,1,2,3,4,4,5]
y=[1,2,2,3,3,5,5]
print(confusion_matrix(x, y))