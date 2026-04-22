
# **Lab 9 Report**  
##### CSCY 4742: Cybersecurity Programming and Analytics, Spring 2026  

**Name & Student ID**: [Your Full Name], [Your Student ID]  

---

# **Task 1: Dataset Investigation and Understanding Decision Trees (10 pts)**

---

## **🔹 Questions**:
1. Explain the feature "Redirecting using `//`".

*The "Redirecting using `//`" feature checks whether a URL uses double slashes (//) beyond the standard protocol part (like http://). In legitimate URLs, // typically appears only once after the protocol. If it appears later in the path, it may indicate redirection to another site, which attackers use to mislead users.
   Legitimate: No extra // in the path
   Suspicious: // appears in an unusual position, suggesting possible redirection
   Phishing: Clear misuse of // to redirect users to a malicious page*
  
2. Explain the feature "Domain registration length".

*The "domain registration length" feature measures how long a domain is registered for. Legitimate businesses usually register domains for longer periods, while phishing sites tend to use short-term registrations.
   Legitimate: Domain registered for more than a year
   Suspicious: Registration length is borderline or unclear
   Phishing: Domain registered for a very short period (e.g., less than a year)*
 
3. Explain the feature "Subdomains and multiple subdomains".  
   - Provide an example of a suspicious domain.
  
*This feature looks at how many subdomains exist in a URL. While normal websites may use one subdomain (like www), phishing sites often stack multiple subdomains to mimic legitimate domains and confuse users.
   Legitimate: Few or no subdomains
   Suspicious: Multiple subdomains
   Phishing: Excessive or misleading subdomains*

*Example of a suspicious domain: "login.security.bank.example.verify-user.com"
    This uses multiple subdomains to appear trustworthy but is actually misleading.*

4. Identify the three most differentiating features and justify your choice.

*Top three most differentiating features (opinion)
   Domain age/registration length – Phishing sites are often short-lived, making this a strong indicator.
   URL structure (like subdomains and redirects) – Attackers manipulate URL complexity to deceive users.
   Presence of HTTPS or security indicators – Although not always reliable alone, combined with other signals it helps distinguish legitimate sites.*
- These features stand out due to directly reflecting attacker behavior making them harder to fake consistently as time passes.
 
5. Explain the concept of information gain in Decision Trees.

*Decision trees use information gain to decide which feature to split on at each step. Information gain measures how much uncertainty (entropy) is reduced after splitting the data based on a feature. The goal is to choose the feature that best separates the data into distinct classes. In simple terms, the tree evaluates all features and selects the one that creates the clearest separation between classes (e.g., phishing vs. legitimate). A higher information gain means the feature provides more useful information for classification. As the tree grows, it repeatedly applies this process: selecting the feature with the highest information gain, splitting the dataset, and continuing until the data is well classified or no further meaningful splits can be made. This is how the model gradually builds a structure that can make predictions on new data.*

---

# **Task 2: Python Environment Setup and Module Explanations (10 pts)**

---

## **🔹 Questions**:
1. What is the `scikit-learn` module and what is its role in this lab?
The scikit-learn module is a widely used open-source Python library built on top of NumPy and SciPy that provides simple and efficient tools for machine learning and data analysis. It includes algorithms for classification, regression, clustering, dimensionality reduction, model selection, and preprocessing, making it especially useful for building predictive models, evaluating performance, and preparing datasets in a consistent workflow. In this lab, it's role is to help train a machine on detecting phishing websites through analysis of datasets, and enable it to predict with accuracy when a website is a phishing website, or a legitimate website.

2. What is the `numpy` module and how is it used for data analysis?
NumPy is a foundational Python library for numerical computing that provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on them efficiently. In data analysis, NumPy is used for fast computations, data manipulation, linear algebra operations, and as the underlying structure for many other libraries (like pandas and scikit-learn), enabling efficient handling of numerical datasets.

---

# **Task 3: Loading the Dataset and Creating Training/Test Splits (10 pts)**

---

## **🔹 Questions**:
1. What should you put in place of the missing `training_size` calculation?

`int(len(inputs) * (cv_fold_n - 1) / cv_fold_n)`
  
2. Explain why calculating training size correctly is important.

*Calculating the training size correctly matters because it directly affects how well your model learns and how reliably you can evaluate it. If you allocate too much data to training, your model may perform well on familiar data but give an overly optimistic evaluation since the test set is too small to represent real-world variation. On the other hand, if the training set is too small, the model won’t have enough examples to learn meaningful patterns, leading to poor performance. Using the correct proportion (like 80/20 for 5-fold splitting) ensures a good balance: enough data for the model to learn effectively, and enough unseen data to fairly assess how well it generalizes to new inputs.*

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

