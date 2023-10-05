# Usage: python data_parser.py

# This file parses the data from `dataset0.json` and `data.info.csv`, and outputs a combined dataset that contains all features and labels in a single 
# dataset. This combined dataset is named `dataset.csv` and is written to the project's `data` directory.

# **Note: Ensure that you are in the project's `src` directory and the data files are in the project's `data` directory. Otherwise, the code will 
# fail due to inconsistent file paths**

# Setting things up
import pandas as pd
import json
from tqdm import tqdm

DATASET0_PATH = "./../data/raw/dataset0.json"
DATA_INFO_PATH = "./../data/raw/data.info.csv"
SAVE_PATH = "./../data/raw/dataset.csv"


# Converting dataset0.json into a dataframe
dataset0 = []
with open(DATASET0_PATH, 'r') as file:
    for line in tqdm(file):
        dataset0.append(json.loads(line))

processed_data = []
for row in tqdm(dataset0):
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


# Combining both datasets
data_info_df = pd.read_csv(DATA_INFO_PATH)
merged_df = pd.merge(processed_data_df, data_info_df)
# Reordering columns to move gene_id to the leftmost column
merged_df = merged_df[['gene_id', 'transcript_id', 'transcript_position', 'k_mer', 'left_dwell',
                       'left_std', 'left_mean', 'mid_dwell', 'mid_std', 'mid_mean',
                       'right_dwell', 'right_std', 'right_mean', 'label']]

# Dummy-encoding DRACH motifs
# D: A --> 10, G --> 01, T --> 00
merged_df['D1'], merged_df['D2'] = (merged_df['k_mer'].str[1] == 'A').astype(int), (merged_df['k_mer'].str[1] == 'G').astype(int)
# A if 1, G if 0
merged_df['R'] = (merged_df['k_mer'].str[2] == 'A').astype(int)
# A if 10, C if 01, T if 00
merged_df['H1'], merged_df['H2'] = (merged_df['k_mer'].str[5] == 'A').astype(int), (merged_df['k_mer'].str[5] == 'C').astype(int)

merged_df.to_csv(SAVE_PATH)