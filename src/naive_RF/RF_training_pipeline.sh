#!/bin/bash
MODEL_PATH="./../../model/rf-ntrees-1000"
TRAIN_PATH="./../../data/curated/bag_data.csv"

echo "Stage 0/4: Checking if dataset0.json has been uncompressed..."
cd ./../../data/raw/
if [ ! -f dataset0.json ]; then gzip -d dataset0.json.gz; fi
echo "dataset0.json prepared"
echo ""

cd ./../../src/naive_RF/

echo "Stage 1/4: Parsing data files..."
python data_parser.py
echo "Data parsed!"
echo ""

echo "Stage 2/4: Performing data normalization..."
mkdir -p ../../data/curated/
python data_normalization.py
echo "Data normalization completed!"
echo ""

echo "Stage 3/4: Performing feature engineering for RF model..."
python naive_RF_feature_engineering.py
echo "Feature engineering for RF model completed!"
echo ""

echo "Stage 4/4: Building Naive RF model..."
python build_naive_RF.py --n_trees 1000 --seed 1 --save_path $MODEL_PATH --train_path $TRAIN_PATH
echo "RF Model trained!"
echo ""

echo "End of script"
