# Usage: 
#   python RF_data_preparation.py

# This script summarizes the statistics of each feature in each bag. The summary statistics consists of
# the following quantiles for each feature: [0, 0.05, 0.25, 0.5, 0.75, 0.95, 1]. In other words, for each
# bag, we calculate the abovementioned quantiles for each feature. These quantiles are the newly-engineered
# features that are used to train the naive Random Forest model. 
# The newly-engineered features will be written to "/data/curated/bag_data.csv".

# **Note: This method removes all information about the interaction effects between features in an instance.
# It is due to this reason that we call it a naive Random Forest model.

import pandas as pd
import random

pd.set_option('display.float_format', lambda x: '%.3f' % x)

DATA_PATH = "../../data/curated/dataset_scaled.csv"
BAG_DATA_PATH = "../../data/curated/bag_data.csv"
TRAIN_DATA_PATH = "../../data/curated/train_data.csv"
TEST_DATA_PATH = "../../data/curated/test_data.csv"

FEATURE_NAMES = ['left_dwell 0.0', 'left_dwell 0.05',
       'left_dwell 0.25', 'left_dwell 0.5', 'left_dwell 0.75',
       'left_dwell 0.95', 'left_dwell 1.0', 'left_std 0.0', 'left_std 0.05',
       'left_std 0.25', 'left_std 0.5', 'left_std 0.75', 'left_std 0.95',
       'left_std 1.0', 'left_mean 0.0', 'left_mean 0.05', 'left_mean 0.25',
       'left_mean 0.5', 'left_mean 0.75', 'left_mean 0.95', 'left_mean 1.0',
       'mid_dwell 0.0', 'mid_dwell 0.05', 'mid_dwell 0.25', 'mid_dwell 0.5',
       'mid_dwell 0.75', 'mid_dwell 0.95', 'mid_dwell 1.0', 'mid_std 0.0',
       'mid_std 0.05', 'mid_std 0.25', 'mid_std 0.5', 'mid_std 0.75',
       'mid_std 0.95', 'mid_std 1.0', 'mid_mean 0.0', 'mid_mean 0.05',
       'mid_mean 0.25', 'mid_mean 0.5', 'mid_mean 0.75', 'mid_mean 0.95',
       'mid_mean 1.0', 'right_dwell 0.0', 'right_dwell 0.05',
       'right_dwell 0.25', 'right_dwell 0.5', 'right_dwell 0.75',
       'right_dwell 0.95', 'right_dwell 1.0', 'right_std 0.0',
       'right_std 0.05', 'right_std 0.25', 'right_std 0.5', 'right_std 0.75',
       'right_std 0.95', 'right_std 1.0', 'right_mean 0.0', 'right_mean 0.05',
       'right_mean 0.25', 'right_mean 0.5', 'right_mean 0.75',
       'right_mean 0.95', 'right_mean 1.0']

if __name__ == "__main__":
    print("Reading data...")
    data = pd.read_csv(DATA_PATH).iloc[:, 1:] # exclude the first column as it is the index
    print("Data read completed!\n")

    print("Generating bag-level statistics...")
    bag_data = data.groupby(["bag_id", "label"]).quantile([0, 0.05, 0.25, 0.5, 0.75, 0.95, 1])
    bag_data = bag_data.reset_index().pivot(index = ['bag_id', 'label'], 
                                            columns=['level_2'], 
                                            values=['left_dwell', 'left_std', 'left_mean',
                                                    'mid_dwell', 'mid_std', 'mid_mean',
                                                    'right_dwell', 'right_std', 'right_mean']
                                        )
    new_colnames = [(c[0] + " " + str(c[1])).strip() for c in bag_data.reset_index().columns]
    bag_data = bag_data.reset_index()
    bag_data.columns = new_colnames
    print("Statistics generated!\n")

    # Generating test samples
    print("Performing train-test-split...")
    print("Train: 80%, Test: 20%")
    random.seed(1)
    test_indices = random.sample(range(0, bag_data.shape[0]), bag_data.shape[0] // 5)
    test_set = bag_data.iloc[test_indices, :].reset_index(drop = True)
    train_set = bag_data.drop(index = test_indices).reset_index(drop = True)
    print("Train-test-split completed!\n")

    print("Writing data files to disk...")
    bag_data.to_csv(BAG_DATA_PATH)
    train_set.to_csv(TRAIN_DATA_PATH)
    test_set.to_csv(TEST_DATA_PATH)
    print("Write completed!")
