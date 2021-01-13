#---------------Predict housing prices based on area, number of bedrooms, bathrooms, stories and parking spots available-----------------------

import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib as plt


file = pd.read_csv("Housing.csv")

newFile = file[["area", "bedrooms", "bathrooms", "stories", "parking"]]

prediction = file["price"]

x = np.array(newFile)
y = np.array(prediction)

#seperate data into training data and data to test model on NOTE; testing size is 10% of total data so 545 x 0.1
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size= 0.1)

#choose model to use
model = linear_model.LinearRegression()

#train model using training data
model.fit(x_train, y_train)

keepGoing = True
while keepGoing == True:

    #Take input from user about the deciding factors for house prices
    areaInput = input("How many acres of land does the property have? ")
    bedroomInput = input("How many bedrooms does the house have? ")
    bathroomInput = input("How many bathrooms does the house have? ")
    storyInput = input("How many stories is this house? ")
    parkingInput = input("How many parking spaces does this house have? ")

    #put user information as an integer into a 5x1 matrix
    userArray = np.array([[int(areaInput), int(bedroomInput), int(bathroomInput), int(storyInput), int(parkingInput)]])

    #feed user input into model and geta  prediction
    predictHousePrice = model.predict(userArray)

    #make user information more readible
    predAmount = str(np.round(predictHousePrice).astype(int))
    predStripped = predAmount.strip("[]")


    print("This house is estimated to cost: $" + predStripped)


    while True:
        answer = int(input("Do you want to check another house? If yes press '1' if no press '2' "))

        if answer == 1:
            keepGoing
            break
        elif answer == 2:
            keepGoing = False
            break

        else:
            continue





