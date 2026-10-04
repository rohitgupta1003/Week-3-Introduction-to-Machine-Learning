# Student Performance Prediction - Mini Project (Week 3)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. load data
df = pd.read_csv("student_performance.csv")

# 2. clean data (fill missing values with mean)
features = ["Study_Hours", "Attendance", "Previous_Marks", "Assignment_Score"]
for col in features:
    df[col] = df[col].fillna(df[col].mean())

# 3. features and target
X = df[features]
y = df["Result"].map({"Fail": 0, "Pass": 1})

# 4. split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 5. scale
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

# 6. train
model = LogisticRegression()
model.fit(X_train_s, y_train)

# 7. accuracy
y_pred = model.predict(X_test_s)
print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")

# 8. predict for new students
new_students = [[6, 85, 72, 70], [1.5, 50, 40, 45], [4, 70, 58, 60], [8.5, 92, 85, 88]]
for s in new_students:
    p = model.predict(scaler.transform(pd.DataFrame([s], columns=features)))[0]
    print(s, "->", "PASS" if p == 1 else "FAIL")
