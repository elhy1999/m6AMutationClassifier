import os
import sys
import argparse
import pandas as pd
import numpy as np
import joblib

pd.set_option('display.float_format', lambda x: '%.7f' % x)

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_path', default="./../model/autoencoder")
    parser.add_argument('--scaler_path', default="./../model/autoencoder_scaler")
    parser.add_argument('--test_path', default="./../data/raw/dataset.csv")
    parser.add_argument('--output_path', default="./../data/teamrc4dsa_dataset0_1.csv")  # Modified output path
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

def compute_bag_probability(predictions):
    """Compute the probability that all instances in a bag are not mutated."""
    return np.prod(1 - predictions)

if __name__ == "__main__":

    # Parsing command line arguments
    args = get_arguments()
    # Checking arguments validity
    check_arguments(args)

    # Reading saved files
    print("Reading from disk...")
    scaler = joblib.load(args.scaler_path)
    autoencoder = joblib.load(args.model_path)
    test_df = pd.read_csv(args.test_path)  # Renamed to test_df for consistency
    print(args.test_path)
    print(test_df.head())
    print(test_df.shape)

    print("Read completed!\n")

    # Predict and generate desired output
    print("Predicting using autoencoder on test set...")

    # List of columns to keep
    selected_columns = [
        'transcript_id','transcript_position', 'left_dwell', 'left_std', 'left_mean',
        'mid_dwell', 'mid_std', 'mid_mean',
        'right_dwell', 'right_std', 'right_mean'
    ]

    # Predict and generate desired output

    test_df_features = test_df[selected_columns].drop(columns=['transcript_id', 'transcript_position'])
    test_df_scaled = scaler.transform(test_df_features)

    test_df_scaled = scaler.transform(test_df_features)
    predicted = autoencoder.predict(test_df_scaled)
    reconstruction_error = np.mean(np.power(test_df_scaled - predicted, 2), axis=1)
    score = (reconstruction_error - np.min(reconstruction_error)) / (np.max(reconstruction_error) - np.min(reconstruction_error))
    output_df = pd.DataFrame({
        'transcript_id': test_df['transcript_id'].values,
        'transcript_position': test_df['transcript_position'].values,
        'score': score
    })
    output_df.to_csv(args.output_path, index=False)
    print(f"Results saved to {args.output_path}.")

    # test_df_features = test_df[selected_columns].drop(columns=['transcript_id', 'transcript_position'])
    # test_df_scaled = scaler.transform(test_df_features)

    # # Here, assuming autoencoder's prediction is giving P(instance is mutated | features)
    # predicted = autoencoder.predict(test_df_scaled)

    # # Compute probabilities for each bag (unique combination of transcript_id and transcript_position)
    # bags = test_df[['transcript_id', 'transcript_position']].drop_duplicates().values
    # bags = bags[0]
    # bag_probabilities = []

    # print("Calculating based on bags...")
    # # for bag in bags:
    # #     bag_indices = test_df[(test_df['transcript_id'] == bag[0]) & (test_df['transcript_position'] == bag[1])].index
    # #     bag_predictions = predicted[bag_indices]
    # #     bag_prob = compute_bag_probability(bag_predictions)
    # #     bag_probabilities.append(bag_prob)
    # for bag in bags:
    #     condition = (test_df['transcript_id'] == bag[0]) & (test_df['transcript_position'] == bag[1])
    #     bag_indices = test_df.loc[condition].index
    #     bag_predictions = predicted[bag_indices]
    #     bag_prob = compute_bag_probability(bag_predictions)
    #     bag_probabilities.append(bag_prob)
    
    # print("Done with bag calculations, extracting data...")
    # output_df = pd.DataFrame({
    #     'transcript_id': bags[:, 0],
    #     'transcript_position': bags[:, 1],
    #     'probability': bag_probabilities
    # })

    # print("Done with extracting data, saving data...")
    # output_df.to_csv(args.output_path, index=False)
    # print(f"Results saved to {args.output_path}.")



