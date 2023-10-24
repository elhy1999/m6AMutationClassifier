import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import auc

FEATURE_NAMES = feature_names = [pos + "_" + stat for pos in ["left", "mid", "right"] for stat in ["dwell", "std", "mean"]]

def calculate_tpr_fpr(predictions, observations):
    TP = sum((p == 1 and o == 1) for p, o in zip(predictions, observations))
    FN = sum((p == 0 and o == 1) for p, o in zip(predictions, observations))
    FP = sum((p == 1 and o == 0) for p, o in zip(predictions, observations))
    TN = sum((p == 0 and o == 0) for p, o in zip(predictions, observations))

    TPR = TP / (TP + FN)
    FPR = FP / (FP + TN)

    return TPR, FPR

def generate_roc_curve(model, X, y, thresholds = None, plot = False):
    if (thresholds == None):
        thresholds = np.arange(0,1.01,0.01)

    predictions = model.predict(X)
    
    tpr = []
    fpr = []
    for threshold in thresholds:
        classifications = (predictions >= threshold).astype(int)
        statistics = calculate_tpr_fpr(classifications, y)
        tpr.append(statistics[0])
        fpr.append(statistics[1])
    
    if plot:
        plt.plot(fpr, tpr)
        plt.xlabel("FPR")
        plt.ylabel("TPR")
        plt.title("ROC Curve")
        plt.show()
    
    auroc = auc(fpr, tpr)
    
    return tpr, fpr, auroc