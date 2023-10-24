# Usage: 
#   python predict_naive_RF.py [--save_path model_save_path] [--test_path test_dataset_path]
# Default values for optional arguments:
#   save_path: ./../model/rf
#   test_path: ./../data/curated/test_data.csv
# Examples:
#   python predict_naive_RF.py
#   python predict_naive_RF.py --save_path ./../model/rf --test_path ./../data/curated/test_data.csv

# This file uses a trained random forest model to predict on a new dataset.

# Reading command line arguments
import os
import sys
import argparse
sys.path.append('../')
# Data manipulation packages
import pandas as pd
import numpy as np
# Require machine learning tools
from sklearn.metrics import auc
import joblib
from naive_RF_feature_engineering import FEATURE_NAMES
from util import generate_roc_curve

pd.set_option('display.float_format', lambda x: '%.3f' % x)

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--save_path', default="./../../model/rf-ntrees-1000")
    parser.add_argument('--test_path', default="./../../data/curated/bag_data.csv")
    return parser.parse_args()

def check_arguments(args):
    # save_path
    if (bool(args.save_path)):
        file_exists = os.path.exists(args.save_path)
        if (not file_exists):
            print("Please input a valid save_path. Received:", args.save_path)
            sys.exit()
        else:
            print("Model found at:", args.save_path)

    # test_path
    if (bool(args.test_path)):
        file_exists = os.path.exists(args.test_path)
        if (not file_exists):
            print("Please input a valid test_path. Received:", args.test_path)
            sys.exit()
        else:
            print("Test data found at:", args.test_path, "\n")

if __name__ == "__main__":

    # Parsing command line arguments
    args = get_arguments()
    # Checking arguments validity
    check_arguments(args)

    # Reading saved files
    print("Reading from disk...")
    rf = joblib.load(args.save_path)
    test_set = pd.read_csv(args.test_path).loc[:, ["bag_id", "label"] + FEATURE_NAMES]
    print("Read completed!\n")

    # Making predictions
    # Use the forest's predict method on the test data
    print("Making predictions...")
    predictions = rf.predict(test_set.loc[:,FEATURE_NAMES])
    print("Predictions made!\n")
    test_set["predictions"] = predictions
    # Calculate the absolute errors
    errors = abs(test_set.predictions - test_set.label)
    # Print out the mean absolute error (mae)
    print('Mean Absolute Error:', round(np.mean(errors), 2))

    # Calculating AUROC
    tpr, fpr, auroc = generate_roc_curve(rf, test_set.loc[:, FEATURE_NAMES], test_set.label)
    print("AUROC:", auroc)


    
