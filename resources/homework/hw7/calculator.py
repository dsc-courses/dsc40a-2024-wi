#!/usr/bin/env python
# coding: utf-8

# <h1><center>Classifying Neutrino Signal from Noise in HPGe Detector</center></h1>

# This notebook will guide you through the second extra credit opportunity. Start out by reading the problem descriptions in the main homework assignment before you work through this notebook.
# 
# We have three imports for this assignment. Please do not import any other packages.

# In[ ]:


import numpy as np
import pandas as pd
from itertools import combinations


# <h2> Problem 6: Prediction Competition<h2>

# Your task is to modify the `predict` function given below. 
# 

# In[ ]:


def predict(row):
    '''Function that returns the predicted score for a given row of the waveform features
    row will be a 1-d array of [tDrift50, tDrift90, tDrift100, blnoise, tslope, Energy, Current_Amplitude]
    please change the return 0 to return a prediction score where:
    * Higher score means the data point is more likely to be a signal (label 1)
    * Lower score means the data point is more likely to be a noise (label 0)
    Note the score doesn't have to be between 0 and 1
    '''
    return row[-1]


# Don't modify the functions given below. This tests how well your predictions perform on a given dataset.

# In[ ]:


def roc_auc(label, score):
    score = np.array(score)
    label = np.array(label)
    dsize = len(score)
    minscore = min(score)
    maxscore = max(score)
    if minscore == maxscore:
        return 0.5
    tpr = []
    fpr = []
    sigscore = score[label==1]
    bkgscore = score[label==0]
    for thr in np.linspace(minscore,maxscore,10000):
        tpr.append(np.sum(sigscore>=thr)/len(sigscore))
        fpr.append(np.sum(bkgscore>=thr)/len(bkgscore))
    
    return np.trapz(tpr,1-np.array(fpr))


# In[ ]:


def calculate_AUC(df):
    '''Compute ROC_AUC_score of the predictions corresponding to each row of the given dataframe'''
    n = df.shape[0]
    total_squared_error = 0
    pred_array = []
    label_array = np.array(df.get('Label'))
    for i in np.arange(n):
        pred_array += [predict(df.iloc[i].drop('Label'))]
    return roc_auc(label_array, pred_array)


# You can test out your predictions on the training dataset provided. We'll also test your predictions on a hidden test dataset.

# In[ ]:


waveforms = pd.read_csv('training_classification.csv')


# In[ ]:


# An example prediction
example_row = waveforms.iloc[0].drop("Label")
predict(example_row)


# In[ ]:


print(calculate_AUC(waveforms))


# <h3> To Submit </h3>
# 
# In the top left corner, in the File menu, select Download as Python (.py). 
# 
# You must save your file as `hw4code.py` for the Gradescope autograder to run. Then, upload this file to the assignment called Homework 4 Code on Gradescope. Problems 4b, 4c, and 5 will be autograded, so you don't need to turn in any written explanation for these questions.

# In[ ]:




