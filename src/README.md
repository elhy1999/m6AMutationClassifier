# Welcome to `/src`!

This repository contains two different modeling approaches for the prediction of m6A. We have implemented a Random Forest (RF) and autoencoder (AE) model. However, due to the superior performance of the RF, the AE model is not used in our final model to make predictions, though the code remains here for archival purposes.

## Directory Structure
```
.
├── significant_transcripts_positions.R
├── make_all_predictions.sh
├── util.py
├── naive_RF
│   ├── build_naive_RF.py
│   ├── data_normalization.py
│   ├── data_parser.py
│   ├── naive_RF_feature_engineering.py
│   ├── predict_naive_RF.py
│   ├── RF_testing_pipeline.py
│   └── RF_training_pipeline.sh
└── archived
    └── AutoEncoder
        ├── build_autoencoder.py
        └── predict_autoencoder.py
```

## Models Overview

- `significant_transcripts_positions.R`: The notebook which Analysis 1 of the report used.

### naive_RF
- `build_naive_RF.py`: Builds the Random Forest model.
- `data_normalization.py`: Normalizes the data using MinMaxScaler.
- `data_parser.py`: Parses the JSON file into a CSV file and prepares the data for the model.
- `naive_RF_feature_engineering.py`: Engineers the bag-level feature to train the RF model.
- `predict_naive_RF.py`: Predicts outcomes using the trained RF model.
- `RF_testing_pipeline.py`: Evaluates the RF model on the testing set.
- `RF_training_pipeline.sh`: Script to run the entire RF training pipeline. This script orchestrates the entire training process by calling the other scripts within this folder in order.
- `make_all_predictions.sh`: This script uses the trained RF model to make predictions across all the datasets from the SG-NEx project.

### AutoEncoder
- `build_autoencoder.py`: Constructs and trains the AutoEncoder model.
- `predict_autoencoder.py`: Predicts outcomes using the trained AutoEncoder model.
