import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Load the dataset (ensure you use the correct CSV file)
data = pd.read_csv(r"C:\Users\NAGESH\Downloads\malware_data.csv")

# Fill missing values
data.fillna(0, inplace=True)

# Split features and target
X = data.drop('label', axis=1)  # Features (replace 'label' with your actual target column name)
y = data['label']  # Target variable

# One-hot encoding for categorical variables
X = pd.get_dummies(X, drop_first=True)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print(classification_report(y_test, y_pred))

# Save the model
joblib.dump(model, 'random_forest_model.pkl')
