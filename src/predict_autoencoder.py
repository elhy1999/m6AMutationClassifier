# Usage: 
#   python predict_autoencoder.py [--save_path model_save_path] [--test_path test_dataset_path]
# Default values for optional arguments:
#   save_path: ./../model/autoencoder
#   test_path: ./../data/curated/test_data.csv
# Examples:
#   python predict_naive_RF.py
#   python predict_naive_RF.py --save_path ./../model/rf --test_path ./../data/curated/test_data.csv

# This file uses an autoencoder model to predict on a new dataset.

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

pd.set_option('display.float_format', lambda x: '%.3f' % x)

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_path', default="./../model/autoencoder")
    parser.add_argument('--scaler_path', default="./../model/autoencoder_scaler")
    parser.add_argument('--test_path', default="./../data/curated/test_data.csv")
    return parser.parse_args()

def check_arguments(args):
    # save_path
    if (bool(args.model_path)):
        file_exists = os.path.exists(args.model_path)
        if (not file_exists):
            print("Please input a valid save_path. Received:", args.model_path)
            sys.exit()
        else:
            print("Model found at:", args.model_path)

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

def generate_roc_curve(predictions):
    
    tpr = []
    fpr = []
    for threshold in thresholds:
        classifications = (predictions >= threshold).astype(int)
        observations = test_features_to_scale["label"]
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
    scaler = joblib.load(args.scaler_path)
    autoencoder = joblib.load(args.model_path)
    test_set = pd.read_csv(args.test_path)
    test_features_to_scale = test_set.drop(columns=['gene_id'])
    test_set_scaled = scaler.transform(test_features_to_scale)
    print("Read completed!\n")

    # Making predictions
    print("Making predictions...")
    predictions = autoencoder.predict(test_set_scaled)
    predictions_inverse_transform = scaler.inverse_transform(predictions)
    print("Predictions made!\n")

    # # Calculate MSE
    # error = np.mean(np.square(test_features_to_scale - predictions_inverse_transform), axis=1)
    # print('Mean Squared Error:', round(np.mean(error), 2))

    # test_features_to_scale["label"] = 0

    # # Calculating AUROC
    # thresholds = np.arange(0,1.01,0.01)
    # tpr, fpr, auroc = generate_roc_curve(predictions_inverse_transform)
    # print("AUROC:", auroc)

    