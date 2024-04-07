import pandas as pd
from sklearn.linear_model import LinearRegression

# Student data
data = {
    "Sr. No.": [428, 215, 221, 159, 247, 146, 222, 449, 225, 257, 299, 315, 329, 460, 507, 171, 232, 249, 389, 484, 485, 506, 63, 141, 280, 324, 492, 400, 34],
    "T1": [17, 15, 16, 15, 14, 15, 12, 14, 18, 17, 13, 10, 13, 15, 9, 14, 13, 13, 14, 9, 12, 15, 13, 15, 2, 0, 11, 8, 3],
    "T2": [15, 18, 20, 16, 15, 17, 11, 13, 18, 13, 15, 12, 15, 10, 16, 14, 15, 17, 10, 9, 8, 7, 8, 12, 10, 0, 3, 13, 1],
    "T3": [28, 30, 23, 28, 29, 25, 29, 28, 25, 23, 20, 24, 20, 26, 20, 25, 15, 23, 18, 24, 19, 16, 15, 17, 17, 22, 16, 8, 18],
    "T4": [29, 27, 31, 28, 32, 31, 24, 23, 23, 26, 29, 27, 28, 22, 27, 22, 28, 21, 19, 16, 20, 20, 23, 22, 14, 9, 12, 13, 12],
    "G": [10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and target
X = df[['T1', 'T2', 'T3', 'T4']]
y = df['G']

# Initialize and train the model
model = LinearRegression()
model.fit(X, y)

# Students to predict
students_to_predict = {
    "Sr. No.": [127, 365, 210, 34],
    "T1": [10, 13, 18, 3],
    "T2": [7, 15, 18, 1],
    "T3": [15, 25, 28, 18],
    "T4": [20, 18, 27, 12]
}

# Convert to DataFrame
df_to_predict = pd.DataFrame(students_to_predict)

# Predict grades
predicted_grades = model.predict(df_to_predict[['T1', 'T2', 'T3', 'T4']])

# Add predicted grades to DataFrame
df_to_predict['Predicted_G'] = predicted_grades

print(df_to_predict[['Sr. No.', 'Predicted_G']])