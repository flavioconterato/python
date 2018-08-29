from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
from keras import optimizers
import numpy as np
import os
import pandas as pd
import sys, getopt
from optparse import OptionParser
from pathlib import Path


def train_model(train,truth):
    # Load dataset
    dataset_train = pd.read_csv(train)
    dataset_trainresults = pd.read_csv(truth)

    # Split into input (X) and output (Y) variables
    X_train = dataset_train.iloc[:, 1:21].values
    y_train = dataset_trainresults

    # Create slope model
    model_slope = Sequential()
    model_slope.add(Dense(12, input_dim=20, init='uniform', activation='linear'))
    model_slope.add(Dense(6, init='uniform', activation='linear'))
    model_slope.add(Dense(1, init='uniform', activation='linear'))
    # Compile slope model
    model_slope.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
    # Fit the slope model
    model_slope.fit(X_train, y_train['slope'], epochs=5, batch_size=10,  verbose=2)

    # Create intercept model
    model_intercept = Sequential()
    model_intercept.add(Dense(12, input_dim=20, init='uniform', activation='linear'))
    model_intercept.add(Dense(6, init='uniform', activation='linear'))
    model_intercept.add(Dense(1, init='uniform', activation='linear'))
    # Compile intercept model
    model_intercept.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
    # Fit the intercept model
    model_intercept.fit(X_train, y_train['intercept'], epochs=5, batch_size=10,  verbose=2)

    ## Just for test the predictions
    # Calculate predictions of slope
    #predictions = model_slope.predict(X_train)
    # round predictions
    #rounded_slope = [x[0] for x in predictions]
    #print(rounded)
    #np.savetxt("slope_predict_train.txt",rounded_slope)

    # calculate predictions of intercept
    #predictions2 = model_intercept.predict(X_train)
    # round predictions
    #rounded_intercept = [x[0] for x in predictions2]
    #print(rounded2)
    #np.savetxt("intercept_predict_train.txt",rounded_intercept)

    # serialize slope model to JSON
    model_slope_json = model_slope.to_json()
    with open("model_slope.json", "w") as json_file:
        json_file.write(model_slope_json)
    # serialize slope weights to HDF5
    model_slope.save_weights("model_slope.h5")

    # serialize intercept model to JSON
    model_intercept_json = model_intercept.to_json()
    with open("model_intercept.json", "w") as json_file:
        json_file.write(model_intercept_json)
    # serialize intercept weights to HDF5
    model_intercept.save_weights("model_intercept.h5")
    print("Saved model to disk")

def test_model(test):
    # Load json and create slope model
    json_file_slope = open('model_slope.json', 'r')
    loaded_model_json_slope = json_file_slope.read()
    json_file_slope.close()
    loaded_model_slope = model_from_json(loaded_model_json_slope)
    # Load slope weights into new model
    loaded_model_slope.load_weights("model_slope.h5")
    print("Loaded model slope from disk")

    # Load json and create intercept model
    json_file_intercept = open('model_intercept.json', 'r')
    loaded_model_json_intercept = json_file_intercept.read()
    json_file_intercept.close()
    loaded_model_intercept = model_from_json(loaded_model_json_intercept)
    # Load intercept weights into new model
    loaded_model_intercept.load_weights("model_intercept.h5")
    print("Loaded model intercept from disk")

    # Load dataset of test
    dataset_test = pd.read_csv(test)
    X_test = dataset_test.iloc[:, 1:21].values

    # Evaluate loaded model on test data
    loaded_model_slope.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
    slopes = loaded_model_slope.predict(X_test)
    # Saving the slope predict in file
    np.savetxt("slope_predict_test.txt",slopes)
    print("Slope of prediction save at: slope_predict_test.txt")

    # Evaluate loaded model on test data
    loaded_model_intercept.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
    intercept = loaded_model_intercept.predict(X_test)
    # Saving the intercept predict in file
    np.savetxt("intercept_predict_test.txt",intercept)
    print("Intercept of prediction save at: intercept_predict_test.txt")

def main(argv):
    
    traintruth = ''
    train = ''
    test = ''

    #Getting args (-t,-r,-n) and testing if is correctly
    try:        
        opts, args = getopt.getopt(argv,"h:t:r:n:",["train","traintruth","test"])
    except getopt.GetoptError:
        print('deepersystem.py -t <train.csv> -r <traintruth.csv> || -n <test.csv>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('deepersystem.py -t <train.csv> -r <traintruth.csv> || -n <test.csv>')
            sys.exit()
        elif opt in ("-t", "--train"):
            train = arg
        elif opt in ("-r", "--traintruth"):
            traintruth = arg
        elif opt in ("-n", "--test"):
            test = arg
            
    # If all args is null, so exit
    if (test == "" and traintruth=="" and train==""):
        print('deepersystem.py -t <train.csv> -r <traintruth.csv> || -n <test.csv>')
        sys.exit(2)
        
    # If all args is present, so exit too
    if (test != "" and traintruth!="" and train!=""):
        print('deepersystem.py -t <train.csv> -r <traintruth.csv> || -n <test.csv>')
        print('just -t and -r OR -n')
        sys.exit(2)
        
    # Verify if train arg and traintruth arg is correctly. If exist model, so dont enter to train, just to test
    if (train != "" and traintruth!=""): 
        if Path("model_slope.json").is_file() and Path("model_slope.h5").is_file() and Path("model_intercept.json").is_file() and Path("model_intercept.h5").is_file():
            print("Model already created, please use the test arg or delete the model_slope and model_intercept in both formats .h5 and .json")
        else:
            train_model(train,traintruth)
    elif (test != ""):
        if Path("model_slope.json").is_file() and Path("model_slope.h5").is_file() and Path("model_intercept.json").is_file() and Path("model_intercept.h5").is_file():
            test_model(test)
        else:
            print("Please, use the train to create a Model.")

if __name__ == "__main__":
    main(sys.argv[1:])
