import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
import joblib


df = pd.read_csv("data/toxic_gas_dataset.csv")


le = LabelEncoder()
df["RiskLevel"] = le.fit_transform(df["RiskLevel"])  # Low=1, Moderate=2, High=0 (example)


X = df[["CO", "CH4", "H2S", "O2"]]
y = df["RiskLevel"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("📊 Classification Report:")
print(classification_report(y_test, y_pred, target_names=le.classes_))

# Save model & encoder
joblib.dump(model, "backend/risk_model.pkl")
joblib.dump(le, "backend/label_encoder.pkl")

print("✅ Model saved to backend/risk_model.pkl")
