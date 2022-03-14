def Euclidean_distance(first_point, second_point): # This function will loop through whole dimensions and will calculate euclidean distance between two points
    sum=0
    for i in range(len(first_point)):
        sum += (first_point[i]-second_point[i])**2
    return (sum)**0.5

def Frequent(data):
    return max(set(data), key = data.count)


def predict(xtrain, ytrain, xtest):
    answere=[]
    for i in xtest:
        dist=[]
        for j in range(len(xtrain)):
            dist.append([Euclidean_distance(i, xtrain[j]), ytest[i]]) # This is for calculating all of the distances
        dist=sorted(dist)
        answere.append(Frequent(dist))

    return answere

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

iris=load_iris()

x=iris.data
y=iris.target

xtrain, xtest, ytrain, ytest=train_test_split(x,y)

answere=predict(xtrain, ytrain, xtest)


print(confusion_matrix(answere, ytest))
