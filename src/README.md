# m6A Prediction Models

This repository contains two different modeling approaches for the prediction of m6A, a type of methylation modification in RNA molecules. We have implemented a naive AutoEncoder and a Random Forest (RF) classifier to tackle this prediction problem.

## Directory Structure
```
.
├── src
│ ├── data_preparation.R
│ ├── naive_AutoEncoder
│ │ ├── build_autoencoder.py
│ │ ├── predict_autoencoder.py
│ │ ├── probability_autoencoder.py
│ │ └── score_conversion.py
│ ├── naive_RF
│ │ ├── build_naive_RF.py
│ │ ├── data_normalization.py
│ │ ├── data_parser.py
│ │ ├── naive_RF_feature_engineering.py
│ │ ├── predict_naive_RF.py
│ │ ├── RF_testing_pipeline.py
│ │ └── RF_training_pipeline.sh
│ └── make_all_predictions.sh
```

## Models Overview

- `data_preparation.R`: Prepares the data to be fed into the model.

### naive_AutoEncoder
- `build_autoencoder.py`: Constructs and trains the AutoEncoder model.
- `predict_autoencoder.py`: Generates predictions using the trained AutoEncoder model.
- `probability_autoencoder.py`: Converts the AutoEncoder outputs to probability scores.
- `score_conversion.py`: Post-processes the AutoEncoder scores for further analysis.

### naive_RF
- `build_naive_RF.py`: Builds the Random Forest model.
- `data_normalization.py`: Normalizes the data using MinMaxScaler or other scaling methods.
- `data_parser.py`: Parses input data and prepares it for the model.
- `naive_RF_feature_engineering.py`: Performs feature engineering to enhance the RF model performance.
- `predict_naive_RF.py`: Predicts outcomes using the trained RF model.
- `RF_testing_pipeline.py`: Evaluates the RF model on the testing set.
- `RF_training_pipeline.sh`: Script to run the entire RF training pipeline.
- `make_all_predictions.sh`: A utility script to run predictions across multiple datasets.


For more detailed information on each component, please refer to the specific files and notebooks within the respective directories. Note this our 
