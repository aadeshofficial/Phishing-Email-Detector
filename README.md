# 🛡️ Phishing Email Detector

A Machine Learning-based desktop application that detects whether an email is **Safe** or **Phishing** using Natural Language Processing (NLP) and a Multinomial Naive Bayes classifier. The application features an easy-to-use graphical interface built with Tkinter.

---

## 📌 Features

- Detects phishing and safe emails
- Machine Learning-based classification
- Displays prediction confidence
- Visual risk score indicator
- Detection history with timestamps
- User-friendly Tkinter GUI
- Clear email functionality

---

## 🛠️ Technologies Used

- Python 3
- Tkinter
- Scikit-learn
- Pandas
- Joblib
- NumPy

---

## 📂 Project Structure

```
Phishing-Email-Detector/
│── gui.py
│── phishing_detector.py
│── phishing_model.pkl
│── vectorizer.pkl
│── README.md
```

---

## 🚀 Installation

Install the required libraries:

```bash
pip install pandas scikit-learn numpy joblib
```

---

## ▶️ Run the Project

Run the application using:

```bash
python gui.py
```

---

## 📊 Application Features

- Email message input
- Safe/Phishing prediction
- Confidence percentage
- Risk score progress bar
- Detection history
- Clear email option

---

## 📌 Note

The original training dataset (`phishing_email.csv`) is not included in this repository because it exceeds GitHub's web upload size limit. The trained model (`phishing_model.pkl`) and vectorizer (`vectorizer.pkl`) are included, allowing the application to run without retraining.

---

## 👨‍💻 Author

**Aadesh Singh BK**

Internship Project