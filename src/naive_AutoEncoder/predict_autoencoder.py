import os
import sys
import argparse
import pandas as pd
import numpy as np
from sklearn.metrics import roc_auc_score
import joblib

pd.set_option('display.float_format', lambda x: '%.3f' % x)

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_path', default="./../model/autoencoder")
    parser.add_argument('--scaler_path', default="./../model/autoencoder_scaler")
    parser.add_argument('--test_path', default="./../data/curated/test_data.csv")
    return parser.parse_args()

def check_arguments(args):
    # model_path
    if (bool(args.model_path)):
        file_exists = os.path.exists(args.model_path)
        if (not file_exists):
            print("Please input a valid model_path. Received:", args.model_path)
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
    test_features = test_set.drop(columns=['gene_id', 'label'])  # Assuming 'label' column exists
    test_set_scaled = scaler.transform(test_features)
    print("Read completed!\n")

    # Making predictions
    print("Making predictions...")
    predictions = autoencoder.predict(test_set_scaled)
    mse = np.mean(np.power(test_features - scaler.inverse_transform(predictions), 2), axis=1)
    print("Predictions made!\n")

    # AUROC Calculation
    auroc = roc_auc_score(test_set['label'], mse)  # Assuming 'label' column exists
    print("AUROC:", auroc)
