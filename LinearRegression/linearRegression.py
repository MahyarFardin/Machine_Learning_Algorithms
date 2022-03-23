import numpy as np

#below pakages are for test
from sklearn import datasets
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# model
class Linear_Regression:
    def __init__(self, lr=.001, iterations=1000):
        self.lr=lr
        self.iterations=iterations
        self.weight=None
        self.bias=None
    
    def fit(self, x, y):
        sample_number, feature_number= x.shape

        self.weight=np.zeros(feature_number)
        self.bias=0

        for _ in range(self.iterations):
            predict = np.dot(x, self.weight)+self.bias

            dw= (1/sample_number)*(np.dot(x.T, predict-y))
            db= (1/sample_number)*(np.sum(predict-y))

            self.weight -= self.lr*dw
            self.bias -= self.lr*db


    def predict(self, x):
        prediction = np.dot(x, self.weight)+ self.bias
        return prediction





# test
x, y= datasets.make_regression(n_samples=200, n_features=1)
xtrain , xtest, ytrain, ytest= train_test_split(x, y)

# my model
lr=Linear_Regression(lr=0.01)
lr.fit(xtrain, ytrain)
prediction_of_me=lr.predict(xtest)
print(mean_squared_error(prediction_of_me, ytest))

# sklearn model
lr2=LinearRegression()
lr2.fit(xtrain, ytrain)
prediction_of_sklearn_lr=lr2.predict(xtest)
print(mean_squared_error(prediction_of_sklearn_lr, ytest))

plt.scatter(xtrain, ytrain, c="green")
plt.scatter(xtest, ytest, c="blue")
plt.plot(xtest, prediction_of_me, c="black")
plt.plot(xtest, prediction_of_sklearn_lr, c="red")
plt.legend(["train","test","my_pred","sklearn_pred"])
plt.savefig("result.jpg")

# These are mse results

# 2.323200225998356e-05
# 1.8388446308314937e-28