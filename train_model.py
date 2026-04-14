import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import os

# Load dataset
data_path = os.path.join(os.path.dirname(__file__), "..", "data", "language.csv")
df = pd.read_csv(data_path)

# Features and labels
X = df["text"]
y = df["language"]

# Convert text to numerical features
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression()
model.fit(X_vec, y)

# Save model and vectorizer
os.makedirs("saved_model", exist_ok=True)

pickle.dump(model, open("saved_model/model.pkl", "wb"))
pickle.dump(vectorizer, open("saved_model/vectorizer.pkl", "wb"))

print("✅ Model trained and saved successfully!")