# Prediction of m6A RNA modifications from direct RNA-Seq data

Welcome to TeamRC4DSA's repository! This repository contains the code, our findings, as well as the references we used. Feel free to poke around, but take note that most of our findings are documented within the `README.md` file in the `/notebooks` directory.

> [!NOTE]
> *To student testers for DSA4266, while you are free to roam around the repository, note that you will find the `/deployment` and `/notebooks` folders to be of greater relevance to you.*

## File Structure:
```
.
├─── src
│    ├─── naive_Autoencoder
│    |    ├─── build_autoencoder.py
│    |    ├─── predict_autoencoder.py
│    |    ├─── probability_autoencoder.py
│    |    └─── score_conversion.py
│    ├─── naive_RF
│    |    ├─── build_naive_RF.py
│    |    ├─── data_normalization.py
│    |    ├─── data_parser.py
│    |    ├─── naive_RF_feature_engineering.py
│    |    ├─── predict_naive_RF.py
│    |    ├─── RF_testing_pipeline.py
│    |    └─── RF_training_pipeline.sh
│    ├─── util.py
│    ├─── significant_transcripts_positions.R
│    ├─── make_all_predictions.sh
│    └─── README.md
├─── notebooks
│    ├─── Autoencoder
│    |    ├─── autoencoder_experimentation.ipynb
│    ├─── Random Forest
│    |    ├─── Model Evaluation.ipynb
│    |    ├─── Naive RF Model.ipynb
│    |    └─── Naive RF Prediction Pipeline.ipynb
│    ├─── Data Analysis
│    |    ├─── Analysis with PCA.ipynb
│    |    ├─── Analysis - Identifier Transcripts.ipynb
│    |    ├─── Data Parsing.ipynb
│    |    ├─── Dataset Normalization.ipynb
│    |    ├─── EDA.ipynb
│    |    └─── Feature Extraction.ipynb
├─── data
│    ├─── raw
│    |    ├─── bag_meta.csv
│    |    ├─── data.info
│    |    ├─── dataset0.json.gz
│    |    └─── dataset2.json
│    └─── curated
│         ├─── dataset1_naiveRF_predictions.csv
│         └─── dataset2_naiveRF_predictions.csv
├─── deployment
│         ├─── data/raw
│         |    └─── dataset2.json
│         ├─── model
│         |    └─── minmaxscaler
│         ├─── src
│         |    ├─── util.py
│         |    └─── RF
|         |         ├─── RF_testing_pipeline.py
|         |         ├─── RF_training_pipeline.py
|         |         ├─── build_naive_RF.py
|         |         ├─── data_normalization.py
|         |         ├─── data_parser.py
|         |         ├─── naive_RF_feature_engineering.py
|         |         └─── predict_naive_RF.py
│         ├─── Dockerfile
│         ├─── docker_installation.sh
│         └─── requirements.txt
├─── model
│    ├─── autoencoder
│    ├─── autoencoder_scalar
│    ├─── minmaxscaler
│    ├─── rf-ntrees_10
│    └─── rf-ntrees_100
├─── reference
│    ├─── deliverables
│    |    ├─── handout_project2_RNAModifications.html
│    |    └─── Student_evaluation_guideline.html
│    └─── research
├─── README.md
├─── .gitignore
└─── .gitattributes
```

> [!NOTE]
> **Git LFS has been configured for this project. To install Git LFS, follow the installation steps below:**
> 
> *MacOS:*
> 1. `brew install git-lfs`
> 2. `git lfs install`
>
> *Windows:*
> 1. Follow the instructions [here](https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage).
