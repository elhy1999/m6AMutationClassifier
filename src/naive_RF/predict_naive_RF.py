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
# Data manipulation packages
import pandas as pd
import numpy as np
# Require machine learning tools
from sklearn.metrics import auc
import joblib
from naive_RF_feature_engineering import FEATURE_NAMES

pd.set_option('display.float_format', lambda x: '%.3f' % x)

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--save_path', default="./../../model/rf")
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

def calculate_tpr_fpr(predictions, observations):
    TP = sum((p == 1 and o == 1) for p, o in zip(predictions, observations))
    FN = sum((p == 0 and o == 1) for p, o in zip(predictions, observations))
    FP = sum((p == 1 and o == 0) for p, o in zip(predictions, observations))
    TN = sum((p == 0 and o == 0) for p, o in zip(predictions, observations))

    TPR = TP / (TP + FN)
    FPR = FP / (FP + TN)

    return TPR, FPR

def generate_roc_curve(model):
    predictions = model.predict(test_set.loc[:,FEATURE_NAMES])
    
    tpr = []
    fpr = []
    for threshold in thresholds:
        classifications = (predictions >= threshold).astype(int)
        observations = test_set.label
        statistics = calculate_tpr_fpr(classifications, observations)
        tpr.append(statistics[0])
        fpr.append(statistics[1])
        
    auroc = auc(fpr, tpr)
    
    return tpr, fpr, auroc

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
    thresholds = np.arange(0,1.01,0.01)
    tpr, fpr, auroc = generate_roc_curve(rf)
    print("AUROC:", auroc)


    
