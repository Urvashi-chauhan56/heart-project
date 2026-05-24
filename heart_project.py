# HEART DISEASE PREDICTION PROJECT


# Step 1: Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Step 2: Load Dataset


df = pd.read_csv('heart.csv')


# Step 3: Show Dataset Information


print("\nFirst 5 Rows of Dataset:\n")
print(df.head())

print("\nDataset Shape:")
print(df.shape)


# Step 4: Separate Features and Target

X = df.drop("target", axis=1)
y = df["target"]


# Step 5: Split Dataset


X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)


# Step 6: Create Logistic Regression Model


model = LogisticRegression(max_iter=1000)


# Step 7: Train Model


model.fit(X_train, y_train)

# Step 8: Test Model


y_pred = model.predict(X_test)


# Step 9: Accuracy


accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")


# Step 10: User Input Section


print("\n==========================================")
print(" ENTER PATIENT DETAILS ")
print("==========================================")

age = int(input("\nAge (20-100): "))

sex = int(input("""
Sex:
1 = Male
0 = Female
Enter value: """))

cp = int(input("""
Chest Pain Type:
0 = Typical Angina
1 = Atypical Angina
2 = Non-anginal Pain
3 = Asymptomatic
Enter value (0-3): """))

trestbps = int(input("""
Resting Blood Pressure:
Normal Range = 90-200
Enter value: """))

chol = int(input("""
Cholesterol Level:
Typical Range = 100-600
Enter value: """))

fbs = int(input("""
Fasting Blood Sugar:
1 = Greater than 120 mg/dl
0 = Normal
Enter value (0 or 1): """))

restecg = int(input("""
Rest ECG:
0 = Normal
1 = ST-T Wave Abnormality
2 = Left Ventricular Hypertrophy
Enter value (0-2): """))

thalach = int(input("""
Maximum Heart Rate Achieved:
Typical Range = 60-220
Enter value: """))

exang = int(input("""
Exercise Induced Angina:
1 = Yes
0 = No
Enter value (0 or 1): """))

oldpeak = float(input("""
Oldpeak (ST Depression):
Typical Range = 0.0 to 6.0
Example = 1.5
Enter value: """))

slope = int(input("""
Slope of Peak Exercise ST Segment:
0 = Upsloping
1 = Flat
2 = Downsloping
Enter value (0-2): """))

ca = int(input("""
Number of Major Vessels Colored by Fluoroscopy:
Range = 0 to 3
Enter value: """))

thal = int(input("""
Thal:
0 = Normal
1 = Fixed Defect
2 = Reversible Defect
Enter value (0-2): """))

# Step 11: Prepare Input Data

input_data = [[
    age,
    sex,
    cp,
    trestbps,
    chol,
    fbs,
    restecg,
    thalach,
    exang,
    oldpeak,
    slope,
    ca,
    thal
]]


# Step 12: Prediction


prediction = model.predict(input_data)


# Step 13: Result


print("\n==========================================")
print(" PREDICTION RESULT ")
print("==========================================")

if prediction[0] == 1:
    print("\nPerson is LIKELY to have Heart Disease")
else:
    print("\nPerson is NOT likely to have Heart Disease")

print("\n==========================================")
print(" THANK YOU ")
print("==========================================")