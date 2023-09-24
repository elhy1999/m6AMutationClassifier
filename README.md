# TeamRC4DSA

## Genomics Project: Prediction of m6A RNA modifications from direct RNA-Seq data

File Structure:
```
.
├─── README.md
├─── src
├─── data
│    └─── raw
│         ├─── data.info
│         └─── dataset0.json
├─── docs
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
- [ ] EDA
      * Do we need to clean the data?
      * How should we prepare the data for building the model? (OHE for categorical features?)
      * What genes should we use in the train/valid/test sets?
- [ ] Research on models to use
- [ ] Model building and evaluation
- [ ] Compiling results
