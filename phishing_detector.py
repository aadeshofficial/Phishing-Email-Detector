import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

# ===================================
# |         LOAD DATASET            |
# ===================================

data = pd.read_csv("phishing_email.csv")

# ===================================
# |       INIPUT AND OUTPUT         |
# ===================================

X = data["text_combined"]
y = data["label"]

# ===================================
# |     CONVERT TEXT INTO NUMBERS   |
# ===================================

vectorizer = TfidfVectorizer(stop_words = "english")
X = vectorizer.fit_transform(X)

# ===================================
# |         SPLIT DATASET           |
# ===================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size = 0.2,
    random_state = 42
)

# ===================================
# |          TRAIN MODEL            |
# ===================================

model = MultinomialNB()
model.fit(X_train, y_train)

joblib.dump(model, "phishing_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

# ===================================
# |          PREDICTIONS            |
# ===================================

y_pred = model.predict(X_test)

# ===================================
# |          ACCURACY               |
# ===================================

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy : ", accuracy)

print("\nConfusion Matrix : ")
print(confusion_matrix(y_test, y_pred))

# ===================================
# |      TEST WITH YOUR EMAIL       |
# ===================================

if __name__ == "__main__":
    print("\n==============================")
    print("Phishing Email Detector")
    print("==============================")

    email = input("Enter an email message : ")

    email_vector = vectorizer.transform([email])

    prediction = model.predict(email_vector)

    if prediction[0] == 1:
        print("\n⚠️ Result : PHISHING EMAIL")
    else:
        print("\n✅ Result : SAFE EMAIL")