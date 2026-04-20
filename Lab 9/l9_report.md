
# **Lab 9 Report**  
##### CSCY 4742: Cybersecurity Programming and Analytics, Spring 2026  

**Name & Student ID**: [Your Full Name], [Your Student ID]  

---

# **Task 1: Dataset Investigation and Understanding Decision Trees (10 pts)**

---

## **🔹 Questions**:
1. Explain the feature "Redirecting using `//`".  
2. Explain the feature "Domain registration length".  
3. Explain the feature "Subdomains and multiple subdomains".  
   - Provide an example of a suspicious domain.
4. Identify the three most differentiating features and justify your choice.  
5. Explain the concept of information gain in Decision Trees.

---

# **Task 2: Python Environment Setup and Module Explanations (10 pts)**

---

## **🔹 Questions**:
1. What is the `scikit-learn` module and what is its role in this lab?  
2. What is the `numpy` module and how is it used for data analysis?

---

# **Task 3: Loading the Dataset and Creating Training/Test Splits (10 pts)**

---

## **🔹 Questions**:
1. What should you put in place of the missing `training_size` calculation?  
2. Explain why calculating training size correctly is important.

---

# **Task 4: Training the Decision Tree Classifier and Evaluating Accuracy (10 pts)**

---

## **🔹 Questions**:
1. Explain the differences between Accuracy, Precision, and Recall.  
2. In what situations is Precision more important than Accuracy? Give a phishing detection example.

---

# **Task 5: Adding Precision, Recall, and F1-Score Evaluations (10 pts)**

---

## **🔹 Deliverables**:
- Paste your code section that calculates Precision, Recall, and F1-Score.

## **🔹 Questions**:
1. Why is F1-Score preferred on imbalanced datasets?  
2. How can Precision and Recall improve phishing detection evaluation?

---

# **Task 6: Randomized Train/Test Split Using `train_test_split` (10 pts)**

---

## **🔹 Step 1 Questions**:
1. What does `train_test_split` do?  
2. What does the `train_size=0.8` parameter mean?  
3. What is the purpose of `random_state=40`?

## **🔹 Step 2 Questions**:
- Provide a table comparing performance metrics **before** and **after** random splitting.  
- Did model performance change after using random splits?  
- Why does random splitting give a better evaluation?

---

# **Task 7: Training and Comparing Random Forest and Decision Tree Classifiers (10 pts)**

---

## **🔹 Questions**:
1. What is a Random Forest classifier? Briefly explain its operation.  
2. Table comparing Decision Tree vs Random Forest metrics:  

| Classifier    | Accuracy | Precision | Recall | F1-Score |
| ------------- | -------- | --------- | ------ | -------- |
| Decision Tree |          |           |        |          |
| Random Forest |          |           |        |          |

3. Which classifier has higher overall accuracy?  
4. Which classifier has better recall?  
5. Why might Random Forests outperform a single Decision Tree?

---

# **Task 8: ROC Curve and AUC Analysis for Classifier Performance (10 pts)**

---

## **🔹 Questions**:
1. Copy/paste your ROC AUC values for Decision Tree and Random Forest.  
2. Which classifier has a higher AUC?  
3. Based on ROC and AUC, which model would you choose for phishing detection? Justify.

## **🔹 Required Screenshots**:
- Decision Tree ROC Curve plot  
- Random Forest ROC Curve plot  
- Console showing AUC values

---

# **Task 9: Threshold Tuning and Performance Analysis (10 pts)**

---

## **🔹 Questions**:
- Provide a table summarizing metrics at different thresholds:

| Threshold | Accuracy (%) | Precision (%) | Recall (%) | F1-Score (%) |
| --------- | ------------ | ------------- | ---------- | ------------ |
| 0.4       |              |               |            |              |
| 0.5       |              |               |            |              |
| 0.6       |              |               |            |              |
| 0.7       |              |               |            |              |

- Which threshold achieved the highest accuracy?  
- Which threshold achieved the best recall?  
- Discuss the trade-offs when lowering or raising the threshold.

---

# **Task 10: Feature Importance Analysis (10 pts)**

---

## **🔹 Questions**:
1. List the top three most important features for the Decision Tree.  
2. List the top three most important features for the Random Forest.  
3. Discuss:  
   - Do the two classifiers agree on the important features?  
   - Why might feature importance rankings differ between models?

## **🔹 Required Screenshots**:
- Screenshot showing Decision Tree feature importance output  
- Screenshot showing Random Forest feature importance output

---

# **Bonus Section (Optional)**

---

## **Bonus Task 1: 5-Fold Cross-Validation**

- Implementation explanation  
- Table with per-fold metrics (Accuracy, Precision, Recall)  
- Final averages and standard deviations

---

## **Bonus Task 2: DummyClassifier and Logistic Regression Comparison**

- Metrics for DummyClassifier and Logistic Regression  
- Short paragraph explaining the importance of baseline comparisons

---

## **Bonus Task 3: Overfitting Reflection**

- Short paragraph addressing:
  1. Evidence of overfitting in your Decision Tree?  
  2. Hyperparameters to tune against overfitting?  
  3. How overfitting could harm phishing detection performance on unseen data?

