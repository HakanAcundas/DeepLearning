import sklearn
import numpy as np
import pandas as pd
from sklearn import linear_model

data = pd.read_csv("diamonds(1).csv", sep=",")


data = data[["carat", "cut", "color","price"]]
predict = "price"
print(data.head())

X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

linear = linear_model.LinearRegression()
linear.fit(x_train, y_train)
acc = linear.score(x_test, y_test)
print(acc)

"""IMPORTANT NOTES: First I changed the data type string to INT. Cut 1-5, Color type is 1 or 2(On internet I saw 
D-E-F is colorless class, and G-H-I-J are near colorless (Colorless = 1, NearColorless = 2). Second I decided the 
price column by 1000 because I got an error that values are too large(18.823 = 18823). Also I erase some NONE(Empty) 
lines and columns. In excel sheet I Sorted from small to large. That's why when in the console you can see only 
higher values. """