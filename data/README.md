# Datasets and Predictions

## File Structure:
```
.
├── data
│ ├── raw
│ │ ├── bag.meta.csv
│ │ ├── data.info.csv
│ │ ├── dataset.csv
│ │ ├── dataset0.json
│ │ └── dataset0.json.gz (removed, because file too lage)
│ │ ├── dataset1.json
│ │ └── dataset1.json.gz (removed, because file too lage)
│ │ ├── dataset2.json
│ │ └── dataset2.json.gz (removed, because file too lage)
├── curated
│ ├── dataset1_naiveRF_predictions.csv
│ ├── dataset2_naiveRF_predictions.csv
│ ├── SGNex_A549_directRNA_replicate5_run1_predictions.csv
│ ├── SGNex_A549_directRNA_replicate6_run1_predictions.csv
│ ├── SGNex_Hct116_directRNA_replicate3_run1_predictions.csv
│ ├── SGNex_Hct116_directRNA_replicate3_run4_predictions.csv
│ ├── SGNex_Hct116_directRNA_replicate4_run3_predictions.csv
│ ├── SGNex_HepG2_directRNA_replicate5_run2_predictions.csv
│ ├── SGNex_HepG2_directRNA_replicate6_run1_predictions.csv
│ ├── SGNex_K562_directRNA_replicate4_run1_predictions.csv
│ ├── SGNex_K562_directRNA_replicate5_run1_predictions.csv
│ ├── SGNex_K562_directRNA_replicate6_run1_predictions.csv
│ ├── SGNex_MCF7_directRNA_replicate3_run1_predictions.csv
│ └── SGNex_MCF7_directRNA_replicate4_run1_predictions.csv
```


1. **bag.meta.csv** - This file contain metadata about bags, which refer to a "bagging" method in machine learning or a collection method in bioinformatics. It contains columns for bag_id, gene_id, transcript_id, transcript_position, label, and n_reads. The 'label' and 'n_reads' columns will be used for a classification task, where 'label' denotes the class, and 'n_reads' refer to the number of reads supporting a given transcript.

2. **data.info.csv** - This file is detailing more information about the genetic data, with gene_id, transcript_id, transcript_position, and label. It provides a simple mapping between these entities for reference.

3. **dataset.csv** - These files are the most complex, containing actual feature vectors for machine learning. It includes gene_id, transcript_id, transcript_position, k-mer (a substring of k characters), and various statistical measures (like mean, standard deviation, and dwell times) of these k-mers. The 'label' column is present here as well, which means this dataset might be used for supervised learning. The last few columns labeled D1, D2, R, HJ, H2 are additional features from extraction of the RNA.

4. **SGNex_[CellLine]_directRNA_replicate[Number]_run[Number]_predictions.csv**
  - These files represent the predictions from direct RNA sequencing experiments.
  - Each file is labeled according to the cell line used (e.g., A549, Hct116, HepG2, K562, MCF7), the replicate number, and the run number, ensuring traceability and organization of the experimental data.
  - The content within these files is tabulated in three main columns:
    - `transcript_id`: The unique identifier for the transcript.
    - `transcript_position`: The numeric position of the transcript.
    - `score`: The predicted value or measurement obtained from the analysis.
  - The files' standardized naming and structured format facilitate comparative analysis and data management across different experimental runs.

### Example File Details

- **SGNex_A549_directRNA_replicate6_run1_predictions.csv**
  - **transcript_id**: `ENST00000602323`
  - **transcript_position**: `244`
  - **score**: `0.032`
  - The above line from the example file indicates that for transcript `ENST00000602323` at position `244`, the prediction score is `0.032`.

### Cellines
A549: A human lung carcinoma cell line.
Hct116: A human colorectal carcinoma cell line.
HepG2: A human liver cancer cell line.
K562: A human chronic myelogenous leukemia cell line.
MCF7: A human breast cancer cell line.

