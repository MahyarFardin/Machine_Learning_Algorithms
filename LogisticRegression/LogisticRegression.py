import math
import numpy as np

class LogisticRegression:
    def _sigmoid(self, x):
        return 1/(1+ math.exp(x))

    def __init__(self, lr=.1, n_iter=1000):

        self.lr=lr
        self.n_iter=n_iter
        self.weights=None
        self.bias=None

    def fit(self , x , y):
        n_samples, n_features= x.shape
        self.weights=np.zeros(n_features)
        self.bias=0

        for _ in range(self.n_iter):
            model = np.dot(x, self.weights) + self.bias
            predict=self._sigmoid(model)

            dw=1/(n_samples)*(np.dot(x.T, predict-y))
            db=1/(n_samples)*(np.sum(predict-y))

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, x):
        model = np.dot(x, self.weights) + self.bias
        predict=self._sigmoid(model)

        predict=[1 if i > 0.5 else 0 for i in predict]

        return predict


# Test
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

breast_canser = datasets.load_breast_cancer()
x, y= breast_canser.data, breast_canser.target
xtrain ,xtest, ytrain ,ytest= train_test_split(x, y)

lr=LogisticRegression()
lr.fit(xtrain, ytrain)
prediction= lr.predict(xtest)

classification_report(prediction, ytest)    