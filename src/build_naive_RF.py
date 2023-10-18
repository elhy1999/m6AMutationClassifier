# Usage: 
#   python build_naive_RF.py [--n_trees number_of_tress] [--seed random_seed] [--save_path model_save_path] [--train_path train_dataset_path]
# Default values for optional arguments:
#   n_trees: 1000
#   seed: 1
#   save_path: ./../model/rf
# Examples:
#   python build_naive_RF.py
#   python build_naive_RF.py --n_trees 1000 --seed 1 --save_path ./../model/rf --train_path ./../data/curated/train_data.csv

# This file builds a random forest model on summarized feature statistics for each bag.

# **Note: Ensure that you have the following required dataset(s) in your project folders:
#   1) ../data/curated/bag_data.csv: A table containing summary statistics for each feature in each bag (See: `./naive_RF_feature_engineering.py`)

# Reading command line arguments
import os
import sys
import argparse
# Data manipulation packages
import pandas as pd
# Require machine learning tools
from sklearn.ensemble import RandomForestRegressor
import joblib

pd.set_option('display.float_format', lambda x: '%.3f' % x)

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--n_trees', default='1000')
    parser.add_argument('--seed', default='1')
    parser.add_argument('--save_path', default="./../model/rf")
    parser.add_argument('--train_path', default="../data/curated/train_data.csv")
    return parser.parse_args()

def check_arguments(args):
    # n_trees
    if (bool(args.n_trees)):
        if (not args.n_trees.isdigit()):
            print("Please input an integer for n_trees. Received:", args.n_trees)
            sys.exit()

    # seed
    if (bool(args.seed)):
        if (not args.seed.isdigit()):
            print("Please input an integer for seed. Received:", args.seed)
            sys.exit()

    # save_path
    if (bool(args.save_path)):
        file_exists = os.path.exists(args.save_path)
        can_write = os.access(os.path.dirname(args.save_path), os.W_OK)
        if (not file_exists and not can_write):
            print("Please input a valid save_path. Received:", args.save_path)
            sys.exit()
    
    # train_path
    if (bool(args.train_path)):
        file_exists = os.path.exists(args.train_path)
        can_write = os.access(os.path.dirname(args.train_path), os.W_OK)
        if (not file_exists and not can_write):
            print("Please input a valid train_path. Received:", args.train_path)
            sys.exit()

if __name__ == "__main__":

    # Parsing command line arguments
    args = get_arguments()
    # Checking arguments validity
    check_arguments(args)
    args.n_trees = int(args.n_trees)
    args.seed = int(args.seed)
    
    print("Reading data from", args.train_path + "...")
    train_data = pd.read_csv(args.train_path).iloc[:,1:]
    print("Data read completed!\n")
    
    # Training the model
    print(f"Training Random Forest model...\nn_trees: {args.n_trees}\nseed: {args.seed}")
    rf = RandomForestRegressor(n_estimators = args.n_trees, random_state = args.seed)
    rf.fit(train_data.iloc[:,2:], train_data.iloc[:,1])
    print("Model training completed!\n")

    # Saving model
    print("Saving model at:", args.save_path)
    joblib.dump(rf, args.save_path)
    print("Model saved!")
