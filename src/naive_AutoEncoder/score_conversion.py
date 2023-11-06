import pandas as pd
import os

# Define path
INPUT_CSV_PATH = "./../data/teamrc4dsa_dataset0_1.csv"
OUTPUT_CSV_PATH = "./../data/teamrc4dsa_dataset0_1.csv"

print("Reading CSV file...")
# Read the CSV file
df = pd.read_csv(INPUT_CSV_PATH)
print(f"CSV file with {len(df)} rows read successfully.")

# Define a function to compute the product for each bag
def compute_harmonic_mean(group):
    n = len(group)
    # If any score in the group is 0, the harmonic mean is undefined. Hence return 0.
    if 0 in group['score'].values:
        return pd.Series({'score': 0})
    else:
        return pd.Series({
            'score': n / sum(1.0 / x for x in group['score'])
        })

print("Computing products for each transcript_id and transcript_position pair...")
# Group by transcript_id and transcript_position and compute the product
result_df = df.groupby(['transcript_id', 'transcript_position']).apply(compute_harmonic_mean).reset_index()
print(f"Computed products for {len(result_df)} unique transcript_id and transcript_position pairs.")

print(f"Saving results to {OUTPUT_CSV_PATH}...")
# Save to a new CSV
result_df.to_csv(OUTPUT_CSV_PATH, index=False)
print("Finished! Check the output file for results.")
