# Usage: python data_normalization.py

# This script normalizes the raw dataset that have been parsed by the data_parser.py script for training machine learning models.

# **Note: The script writes to the "/data/curated/" folder. Ensure that you have previously created that folder.
# **Note: Ensure that you are in the project's `src/naive_RF` directory and the data files are in the project's `data` directory. Otherwise, the code will 
# fail due to inconsistent file paths**

# Setting things up
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib

DATA_READ_PATH = "./../../data/raw/dataset.csv"
DATA_WRITE_PATH = "./../../data/curated/dataset_scaled.csv"
BAG_META_PATH = "./../../data/raw/bag_meta.csv"
SCALER_SAVE_PATH = "./../../model/minmaxscaler"

if __name__ == "__main__":
    print("Reading data...")
    data = pd.read_csv(DATA_READ_PATH).iloc[:, 1:]
    print("Data read completed!")

    # Bringing in the bag_id column for each bag so that we can remove the gene_id, transcript_id,
    # and transcript_position columns for clarity
    bag_meta = pd.read_csv(BAG_META_PATH).iloc[:,1:]
    data = data.merge(bag_meta, on = ["gene_id", "transcript_id", "transcript_position", "label"])

    feature_names = [pos + "_" + stat for pos in ["left", "mid", "right"] for stat in ["dwell", "std", "mean"]]
    # feature_names is just the list of 9 features: ["left_dwell", "left_std", ..., "right_std", "right_mean"]
    data = data.loc[:, ["bag_id", "label"] + feature_names]

    # Normalization
    print("Performing normalization...")
    scaler = MinMaxScaler()
    scaler.fit(data.iloc[:, 2:])
    normalized_features = pd.DataFrame(scaler.transform(data.iloc[:, 2:]), columns = feature_names)
    normalized_data = pd.concat([data.iloc[:, :2], normalized_features], axis = 1)
    print("Normalization completed!")

    # Writing to disk
    print("Writing to disk...\nNote: The file will be written to:", DATA_WRITE_PATH)
    normalized_data.to_csv(DATA_WRITE_PATH)
    joblib.dump(scaler, SCALER_SAVE_PATH)
    print("Writing completed!")
