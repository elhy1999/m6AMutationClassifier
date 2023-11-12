# Datasets and Predictions

## File Structure:
```
.
├── raw
│    ├── bag.meta.csv
│    ├── data.info.csv
│    └── dataset2
└── curated
     ├── teamrc4dsa_dataset1.csv
     ├── teamrc4dsa_dataset2.csv
     ├── teamrc4dsa_dataset3.csv
     ├── fully_mutated.csv
     ├── SGNex_A549_directRNA_replicate5_run1_predictions.csv
     ├── SGNex_A549_directRNA_replicate6_run1_predictions.csv
     ├── SGNex_Hct116_directRNA_replicate3_run1_predictions.csv
     ├── SGNex_Hct116_directRNA_replicate3_run4_predictions.csv
     ├── SGNex_Hct116_directRNA_replicate4_run3_predictions.csv
     ├── SGNex_HepG2_directRNA_replicate5_run2_predictions.csv
     ├── SGNex_HepG2_directRNA_replicate6_run1_predictions.csv
     ├── SGNex_K562_directRNA_replicate4_run1_predictions.csv
     ├── SGNex_K562_directRNA_replicate5_run1_predictions.csv
     ├── SGNex_K562_directRNA_replicate6_run1_predictions.csv
     ├── SGNex_MCF7_directRNA_replicate3_run1_predictions.csv
     └── SGNex_MCF7_directRNA_replicate4_run1_predictions.csv
```


1. **bag.meta.csv** - This file contain metadata about bags in the context of this multiple instance learning problem. It contains columns for bag_id, gene_id, transcript_id, transcript_position, label, and n_reads. The 'label' and 'n_reads' columns will be used for a classification task, where 'label' denotes the class, and 'n_reads' refer to the number of reads supporting a given transcript.

2. **data.info.csv** - This file contains information about gene_id, transcript_id, transcript_position, and label. It provides a simple mapping between these entities for reference.

3. **fully_mutated.csv** - Table of 141 significant (transcript ID, transcript positions) with mutations across all datasets. Results of Analysis 1.

4. **teamrc4dsa_dataset.csv**: These files contain the random forest's prediction on datasets 1, 2, and 3.

5. **SGNex_[CellLine]_directRNA_replicate[Number]_run[Number]_predictions.csv**
  - These files represent the predictions from direct RNA sequencing experiments.
  - Each file is labeled according to the cell line used (e.g., A549, Hct116, HepG2, K562, MCF7), the replicate number, and the run number.
  - The content within these files is tabulated in three main columns:
    - `transcript_id`: The unique identifier for the transcript.
    - `transcript_position`: The numeric position of the transcript.
    - `score`: The predicted probability that the given bag has an m6A mutation. This prediction is made by the Random Forest model.

### Example File Details

- **SGNex_A549_directRNA_replicate6_run1_predictions.csv**
  - **transcript_id**: `ENST00000602323`
  - **transcript_position**: `244`
  - **score**: `0.032`
  - The above line from the example file indicates that for transcript `ENST00000602323` at position `244`, the prediction score is `0.032`.

### Cellines
- A549: A human lung carcinoma cell line.
- Hct116: A human colorectal carcinoma cell line.
- HepG2: A human liver cancer cell line.
- K562: A human chronic myelogenous leukemia cell line.
- MCF7: A human breast cancer cell line.

