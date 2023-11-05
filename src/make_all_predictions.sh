#!/bin/bash

declare -a file_names=("SGNex_A549_directRNA_replicate5_run1" "SGNex_A549_directRNA_replicate6_run1" "SGNex_Hct116_directRNA_replicate3_run1" "SGNex_Hct116_directRNA_replicate3_run4" "SGNex_Hct116_directRNA_replicate4_run3" "SGNex_HepG2_directRNA_replicate5_run2" "SGNex_HepG2_directRNA_replicate6_run1" "SGNex_K562_directRNA_replicate4_run1" "SGNex_K562_directRNA_replicate5_run1" "SGNex_K562_directRNA_replicate6_run1" "SGNex_MCF7_directRNA_replicate3_run1" "SGNex_MCF7_directRNA_replicate4_run1")

for file_name in "${file_names[@]}"
do
    cd ~/Git/CancerMutationClassifier/data/raw/
    echo "Downloading data for $file_name"
    echo
    aws s3 cp --no-sign-request s3://sg-nex-data/data/processed_data/m6Anet/"$file_name"/data.json .
    cd ~/Git/CancerMutationClassifier/src/naive_RF
    echo "Making predictions"
    echo
    python RF_testing_pipeline.py --test_path ./../../data/raw/data.json
    cd ~/Git/CancerMutationClassifier/data/curated/
    mv predictions.csv "$file_name"_predictions.csv
done
