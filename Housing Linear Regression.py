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

#create arrays for the data
x = np.array(newFile)
y = np.array(prediction)


#seperate data into training data and data to test model on NOTE: testing size is 10% of total data so 545 x 0.1
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size= 0.1)

#choose model to use
model = linear_model.LinearRegression()

#fit training data to model
model.fit(x_train, y_train)

#main while loop to restart to inputs if user desires
keepGoing = True
while keepGoing == True:

    #try and except block for invalid entries, if except is triggered it goes
    #down to ask if you want to enter another house
    try:

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
        predictedAmount = str(np.round(predictHousePrice).astype(int))
        predictedStripped = predictedAmount.strip("[]")


        print("This house is estimated to cost: $" + predictedStripped)
        print("==================================================")

    except:
        print("==================================================")
        print("There was an error, one of your inputs was not a number")

    #while loop to keep looping and asking if they want another house in case
    #of bad input
    userRetry = True
    while userRetry:
        #try and except block for bad input
        try:
            while True:
                answer = int(input("Do you want to check another house? If yes press '1' if no press '2' "))

                if answer == 1:
                    keepGoing
                    userRetry = False
                    break
                elif answer == 2:
                    keepGoing = False
                    userRetry = False
                    break

                else:
                    continue
        except:
            print("Invalid Entry please select 1 or 2")
            userRetry
