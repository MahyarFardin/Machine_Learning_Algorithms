import numpy as np

class LogisticRegression:
    def _sigmoid(self, x):  # sigmoid function
        return 1/(1+ np.power(2.71828,-x))

    def __init__(self, lr=.1, n_iter=1000): # Constructor

        self.lr=lr
        self.n_iter=n_iter
        self.weights=None
        self.bias=None

    def fit(self , x , y):
        n_samples, n_features= x.shape
        self.weights=np.zeros(n_features)
        self.bias=0

        for _ in range(self.n_iter):    # Finding best power for the e in sigmoid using gradient descent
            model = np.dot(x, self.weights) + self.bias
            predict=self._sigmoid(model)

            dw=(1/n_samples)*(np.dot(x.T, (predict-y))) #Derivitive of weight
            db=(1/n_samples)*(np.sum(predict-y)) #Derivitive of bias

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, x):
        model = np.dot(x, self.weights) + self.bias
        predict=self._sigmoid(model)

        predict=[1 if i > 0.5 else 0 for i in predict]  # Applying the sigmoid part

        return predict



# Test
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

breast_canser = datasets.load_breast_cancer()
x, y= breast_canser.data, breast_canser.target
xtrain ,xtest, ytrain ,ytest= train_test_split(x, y)

plt.scatter(x[5], y)
plt.savefig("plot.jpg")

lr=LogisticRegression()
lr.fit(xtrain, ytrain)
prediction= lr.predict(xtest)

print(classification_report(prediction, ytest))  

"""
              precision    recall  f1-score   support

           0       0.76      0.97      0.85        35
           1       0.99      0.90      0.94       108

    accuracy                           0.92       143
   macro avg       0.87      0.93      0.90       143
weighted avg       0.93      0.92      0.92       143
"""
