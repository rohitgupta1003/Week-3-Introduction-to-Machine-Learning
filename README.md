# Week 3 - Introduction to Machine Learning

This repository has my work for **Week 3** of my AI internship. In this week I learned the basics of Machine Learning: what it is, how to prepare a dataset, how to split data into training and testing sets, how to train a simple model, and how to check its accuracy.

## Folder Structure

```
Week 3 - AI
│
├── Week3_Report.pdf        # Task 1 - ML fundamentals report
├── Week3_ML.ipynb          # Tasks 2, 3 and 4 - notebook
├── Dataset.csv             # Student performance dataset
├── Screenshots/            # Output screenshots of all tasks
└── Mini_Project/           # Task 5 - Student Performance Prediction
    ├── Student_Performance_Prediction.ipynb
    ├── student_performance.py
    ├── student_performance.csv
    └── Mini_Project_Report.pdf
```

## Tasks

### Task 1: Machine Learning Fundamentals
A 2-page PDF report (`Week3_Report.pdf`) that explains:
- What is Machine Learning
- AI vs ML vs Deep Learning
- Dataset, features and labels
- Training data and testing data
- Supervised vs unsupervised learning
- Classification vs regression
- Real-world applications of ML

### Task 2: Dataset Preparation
Done in `Week3_ML.ipynb` using Pandas. I loaded the student dataset, checked the first 5 rows, shape and data types, found and filled the missing values (with the column mean), and then separated the data into **X (features)** and **y (target)**.

### Task 3: Train-Test Split and Preprocessing
Done in `Week3_ML.ipynb` using Scikit-learn.
- Split the data into 80% training and 20% testing (`test_size=0.2`)
- Explained why we split the data: **Training Data → Model Learning → Testing Data → Prediction**
- Encoded the target (Fail = 0, Pass = 1)
- Scaled the features with `StandardScaler` (fitted on training data only)

### Task 4: First Machine Learning Model
Done in `Week3_ML.ipynb`.
- **Logistic Regression** on the student data to predict Pass/Fail (accuracy: 85%)
- **Decision Tree** on the Iris dataset (accuracy: about 97%)
- Includes predictions, a confusion matrix and an explanation of how each model works

### Task 5: Mini Project - Student Performance Prediction
Inside the `Mini_Project` folder. The model predicts whether a student will **Pass or Fail** using Study Hours, Attendance, Previous Marks and Assignment Score.

Steps: load data → clean data → select features and target → split → train Logistic Regression → predict → calculate accuracy → test with new students.

**Accuracy: 85%** on the test data.

Example prediction:

```
Study Hours     : 6
Attendance      : 85%
Previous Marks  : 72
Assignment Score: 70
Prediction      : PASS
```

## Dataset
The dataset has 200 student records with these columns: `Student_ID`, `Study_Hours`, `Attendance`, `Previous_Marks`, `Assignment_Score` and `Result` (Pass/Fail). It is a sample dataset created for practice, and it contains some missing values on purpose to practice data cleaning.

## Libraries Used
- pandas
- numpy
- matplotlib
- scikit-learn

## How to Run

1. Install the libraries:
   ```
   pip install pandas numpy matplotlib scikit-learn jupyter
   ```
2. Open the notebook:
   ```
   jupyter notebook Week3_ML.ipynb
   ```
3. For the mini project, open `Mini_Project/Student_Performance_Prediction.ipynb`, or run the script from inside the `Mini_Project` folder:
   ```
   python student_performance.py
   ```

## What I Learned
- The basic ML workflow: **Load → Clean → Split → Train → Predict → Evaluate**
- The difference between features and labels
- Why we keep a separate test set (to avoid overfitting)
- How classification models like Logistic Regression and Decision Tree work
- How to measure a model with accuracy and a confusion matrix

## Author
Rohit Kumar Gupta
