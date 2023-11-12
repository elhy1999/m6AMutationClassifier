# Notebooks

## File Structure:
```
.
notebooks
├── Autoencoder
│   └── autoencoder_experimentation.ipynb
├── Data Analysis
│   ├── Analysis - Identifier Transcripts.ipynb
│   ├── Analysis with PCA.ipynb
│   ├── Data Parsing.ipynb
│   ├── Dataset Normalization.ipynb
│   ├── EDA.ipynb
│   └── Feature Extraction.ipynb
└── Random Forest
    ├── Model Evaluation.ipynb
    ├── Naive RF Model.ipynb
    └── Naive RF Prediction Pipeline.ipynb
```

# Welcome to `/notebooks`!

This folder contains the code written to perform experimentation and analysis. The finalized code in this directory are written to form scripts saved under the `/src` directory

## Autoencoder

- `autoencoder_experimentation.ipynb`: This notebook includes an implementation of the autoencoder model.

## Data Analysis

- `Analysis - Identifier Transcripts.ipynb`: The notebook which Analysis 2 of the report used.

- `Analysis_with_PCA.ipynb`: Principal Component Analysis (PCA) is applied to the dataset to identify the most important features and visualize the separation between bags of different labels.

- `Data_Parsing.ipynb`: This notebooks consists of code that convert the JSON-formatted dataset from the SG-NEx project into CSV files.

- `Dataset_Normalization.ipynb`: This notebook contains code that normalizes the features of the dataaset for model building.

- `EDA.ipynb`: Exploratory Data Analysis (EDA) is conducted to summarize the main characteristics of the data with visualizations.

- `Feature_Extraction.ipynb`: Methods for extracting meaningful features for training the autoencoder model.

## Random Forest

- `Model_Evaluation.ipynb`: Evaluation methods such as K-Fold Cross Validation are used to assess the performance of the Random Forest model.

- `Naive_RF_Model.ipynb`: The building of the Random Forest model.

- `Naive_RF_Prediction_Pipeline.ipynb`: A pipeline for making predictions with the Random Forest model.
