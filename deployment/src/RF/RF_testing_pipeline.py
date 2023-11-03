#!/bin/python

import argparse
import os
import sys
sys.path.append('../')
import pandas as pd
import json
from tqdm import tqdm
import joblib
from util import FEATURE_NAMES

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--test_path')
    return parser.parse_args()

def check_arguments(args):
    # test_path
    if (not bool(args.test_path)): # If the test dataset's path is not specified
        print("Please input the path to the test dataset. E.g. python RF_testing_pipeline.py --test_path ../data/test_set.json")
    else:
        file_exists = os.path.exists(args.test_path)
        if (not file_exists):
            print("Could not locate the test dataset. Please input a valid test_path. Received:", args.test_path)
            sys.exit()

SCALER_SAVE_PATH = "./../../model/minmaxscaler"
MODEL_SAVE_PATH = "./../../model/rf-ntrees-1000"
PREDICTIONS_SAVE_PATH = "./../../data/curated/predictions.csv"

if __name__ == "__main__":
    # Parsing command line arguments
    args = get_arguments()
    # Checking arguments validity
    check_arguments(args)

    # Reading saved files
    print("Reading from disk...")
    rf = joblib.load(MODEL_SAVE_PATH)
    scaler = joblib.load(SCALER_SAVE_PATH)
    # Converting JSON file into a table
    dataset = []
    with open(args.test_path, 'r') as file:
        for line in tqdm(file):
            dataset.append(json.loads(line))
    processed_data = []
    for row in tqdm(dataset):
        transcript_id = list(row.keys())[0]
        transcript_position = list(row[transcript_id].keys())[0]
        k_mer = list(row[transcript_id][transcript_position].keys())[0]
        reads = row[transcript_id][transcript_position][k_mer]
        for read in reads:
            processed_data_row = [transcript_id, transcript_position, k_mer] + read
            processed_data.append(processed_data_row)
    columns = ["transcript_id", "transcript_position", "k_mer",
              "left_dwell"   , "left_std"           , "left_mean",
              "mid_dwell"    , "mid_std"            , "mid_mean",
              "right_dwell"  , "right_std"          , "right_mean"]
    processed_data_df = pd.DataFrame(processed_data, columns = columns)
    processed_data_df.transcript_position = processed_data_df.transcript_position.astype("int64")
    print("Read completed!\n")

    # Dataset normalization
    print("Normalizing input data...")
    normalized_features = pd.DataFrame(scaler.transform(processed_data_df.iloc[:, 3:]), columns = FEATURE_NAMES)
    normalized_data = pd.concat([processed_data_df.iloc[:, :2], normalized_features], axis = 1)
    print("Data normalization completed!")

    # Feature engineering
    print("Performing feature engineering for bags...")
    bag_data = normalized_data.groupby(["transcript_id", "transcript_position"]).quantile([0, 0.05, 0.25, 0.5, 0.75, 0.95, 1])
    bag_data = bag_data.reset_index().pivot(index = ["transcript_id", "transcript_position"], 
                                            columns=['level_2'], 
                                            values=['left_dwell', 'left_std', 'left_mean',
                                                    'mid_dwell', 'mid_std', 'mid_mean',
                                                    'right_dwell', 'right_std', 'right_mean']
                                          )
    new_colnames = [(c[0] + " " + str(c[1])).strip() for c in bag_data.reset_index().columns]
    bag_data = bag_data.reset_index()
    bag_data.columns = new_colnames
    print("Feature engineering completed!")

    # Making predictions
    # Use the forest's predict method on the test data
    print("Making predictions...")
    bag_data["score"] = rf.predict(bag_data.iloc[:,2:])
    predictions = bag_data.loc[:, ["transcript_id", "transcript_position", "score"]]
    predictions.to_csv(PREDICTIONS_SAVE_PATH, index=False)
    print("Predictions made!")
    print(f"Predictions saved to {PREDICTIONS_SAVE_PATH}\n")



















