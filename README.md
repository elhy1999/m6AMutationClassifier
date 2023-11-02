# TeamRC4DSA

## Genomics Project: Prediction of m6A RNA modifications from direct RNA-Seq data

File Structure:
```
.
├─── README.md
├─── src
├─── notebooks
├─── data
│    └─── raw
│         ├─── data.info
│         └─── dataset0.json
├─── docs
├─── model
├─── reference
│    ├─── deliverables
│    |    ├─── handout_project2_RNAModifications.html
│    |    └─── Student_evaluation_guideline.html
│    └─── literature
├─── requirements.txt
└─── .gitignore
```

**Note: Git LFS has been configured for this project. To install Git LFS, follow the installation steps below:**

*MacOS:*

1. `brew install git-lfs`
2. `git lfs install`

*Windows:*

Follow the instructions [here](https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage).


# Team Tasks:

- [X] Data parsing (src/data_parser.py)
- [X] EDA

      * Do we need to clean the data?
      * How should we prepare the data for building the model? (OHE for categorical features?)
      * What genes should we use in the train/valid/test sets?
- [X] Research on models to use
- [X] Model building and evaluation
- [X] Compiling results
- [ ] Reproducibility on AWS EC2 - Aaron
- [ ] Video Presentation (10 minutes)
- [ ] Prediction of m6A sites in [all SG-NEx direct RNA-Seq samples](http://sg-nex-data.s3-website-ap-southeast-1.amazonaws.com/#data/processed_data/m6Anet/)
- [ ] Repository Documentation - Ernest
- [ ] Model evaluation (for team report)
- [ ] (Optional) Train the model on all data in the SG-NEx AWS S3 bucket
