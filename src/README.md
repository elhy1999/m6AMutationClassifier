# m6A Prediction Models

This repository contains two different modeling approaches. We have implemented a Random Forest (RF) classifier to tackle this prediction problem. We also attempted to train an AutoEncoder model, but decided not to develop it further due to its poor initial performance, though the code remains here for archival purposes.

## Directory Structure
```
.
├── src
│ ├── data_preparation.R
│ ├── naive_RF
│ │ ├── build_naive_RF.py
│ │ ├── data_normalization.py
│ │ ├── data_parser.py
│ │ ├── naive_RF_feature_engineering.py
│ │ ├── predict_naive_RF.py
│ │ ├── RF_testing_pipeline.py
│ │ └── RF_training_pipeline.sh
│ ├── make_all_predictions.sh
│ ├── archived
│ │ ├── AutoEncoder
│ │ │ ├── build_autoencoder.py
│ │ │ └── predict_autoencoder.py
```

## Models Overview

- `data_preparation.R`: Prepares the data to be fed into the model.

### naive_RF
- `build_naive_RF.py`: Builds the Random Forest model.
- `data_normalization.py`: Normalizes the data using MinMaxScaler or other scaling methods.
- `data_parser.py`: Parses input data and prepares it for the model.
- `naive_RF_feature_engineering.py`: Performs feature engineering to enhance the RF model performance.
- `predict_naive_RF.py`: Predicts outcomes using the trained RF model.
- `RF_testing_pipeline.py`: Evaluates the RF model on the testing set.
- `RF_training_pipeline.sh`: Script to run the entire RF training pipeline.
- `make_all_predictions.sh`: A utility script to run predictions across multiple datasets.

### AutoEncoder
- `build_autoencoder.py`: Constructs and trains the AutoEncoder model.
- `predict_autoencoder.py`: Predicts outcomes using the trained AutoEncoder model.


For more detailed information on each component, please refer to the specific files and notebooks within the respective directories.