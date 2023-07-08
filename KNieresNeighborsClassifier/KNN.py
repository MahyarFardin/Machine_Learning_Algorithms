def Euclidean_distance(first_point, second_point): # This function will loop through whole dimensions and will calculate euclidean distance between two points
    sum=0
    for i in range(len(first_point)):
        sum += (first_point[i]-second_point[i])**2
    return (sum)**0.5

def Frequent(data): # This function will find the most frequent classes
    freq=0
    maximum=0
    for i in data:
        counter=0
        for j in data:
            if i==j:
                counter += 1
        if counter > maximum:
            maximum=counter
            freq = i 

    return freq

def predict(xtrain, ytrain, xtest, k):
    answere=[]
    for i in xtest:
        dist=[]
        for j in range(len(xtrain)):
            dist.append([Euclidean_distance(i, xtrain[j]), ytrain[j]]) # This is for calculating all of the distances and appending them with their classes
        
        dist=sorted(dist) # Time stamp sort
        
        dist= dist[:k] # Just considering the k neighbors

        labels=[x[1] for x in dist] # seperating labels from distances

        answere.append(Frequent(labels))

    return answere

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

iris=load_iris()

x=iris.data
y=iris.target

xtrain, xtest, ytrain, ytest=train_test_split(x,y)

answere=predict(xtrain, ytrain, xtest, 5)

print(confusion_matrix(answere, ytest))
print(classification_report(answere, ytest))

'''
[[11  0  0]
 [ 0 10  1]
 [ 0  2 14]]
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        11
           1       0.83      0.91      0.87        11
           2       0.93      0.88      0.90        16

    accuracy                           0.92        38
   macro avg       0.92      0.93      0.92        38
weighted avg       0.92      0.92      0.92        38
'''