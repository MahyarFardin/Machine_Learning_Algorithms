import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

class KNierestRegressor:

    def Euclidean_distance(first_point, second_point): # This function will loop through whole dimensions and will calculate euclidean distance between two points
        sum=0
        for i in range(len(first_point)):
            sum += (first_point[i]-second_point[i])**2
        return (sum)**0.5

    def predict(xtrain, ytrain, xtest, k):
        answere=[]

        for i in xtest:
            dist=[]
            for j in range(len(xtrain)):
                dist.append([KNierestRegressor.Euclidean_distance(i, xtrain[j]), ytrain[j]])
        
            dist=sorted(dist) # Time stamp sort
            
            dist= dist[:k] # Just considering the k neighbors    
            
            answere.append(np.sum(dist)/k) # This will calculate the average of the k nierest points

        return answere

data=datasets.make_regression(n_samples=400, noise=.4)

xtrain, xtest, ytrain, ytest=train_test_split(data[0], data[1])

answere=KNierestRegressor.predict(xtrain, ytrain, xtest, 5)

print(mean_squared_error(answere, ytest))
