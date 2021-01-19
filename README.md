# HousingPricesMultipleRegression
This project is basically a linear regression project with multiple variables. I used a random data set supplied by Kaggle.com (can be found here: https://www.kaggle.com/ashydv/housing-dataset?select=Housing.csv) that had lots of data about housing including the price of houses, the area of the house, whether or not there is a basement in the house, whether the house has air conditioning or not etc. I used only the data that had a numerical value attached to it as this was what I intended to do. With this data I was able to create a program that predicts the housing price with user inputs.



**Process**

At first the data needs to be read in, I used the pandas library to read in the file into python. After that the data needs to be filtered to the columns that you want to use. The next step is to put that data into a matrix or array so operations can be done on the data. I used the numpy library to put the data in arrays as this would make it easier to manipulate the data and perform operations on it. After the data is in the arrays the data needs to be split into data that will be used to train the model and data that will be used to test the model. The test data is going to be something that the model has never seen and is supposed to mimick how the model would would perform in real life. Next the training data is fit to the model. After this I made the program take in user input for the features or variables that determine the house price (area, number of bedrooms, number of bathrooms etc). Near the end of the code I made sure to check for any undesired inputs such as letters and other characters that are not numbers. If there is undesired input the program would read that there was an error in one of your inputs and the user would be prompted to attempt inputting the values again. However, if the inputs are desired (numbers) they are put into a 1x5 row vector which is then used to predict the price of the house that has been described by the user. Once the price is printed I made a prompt to ask the user if they would like to predict another house price. Again I made sure to check for any undesired inputs. If the user chooses they dont want to see the price of another house the program will end. If the user wants to enter another set of features the program restarts but the same training data is still used (there is no new data that is fitted to the model). This way the user wont get a different price prediction if they enter the same features 2 times in a row. 
