import numpy as np
import tkinter as tk
from tkinter import ttk
from phishing_detector import model, vectorizer
from datetime import datetime

history = []

# ===================================
# |      FUNCTIN TO CHECK EMAIL     |
# ===================================

def check_email():
    email = email_text.get("1.0", tk.END).strip()

    if email == "":
        result_label.config(text = "Please enter an email.", fg = "orange")
        return
    
    email_vector = vectorizer.transform([email])
    prediction = model.predict(email_vector)

    probability = model.predict_proba(email_vector)
    confidence = max(probability[0]) * 100
    risk_bar["value"] = confidence

    if prediction[0] == 1:
        result_label.config(
            text=f"⚠️ PHISHING EMAIL\nConfidence: {confidence:.2f}%",
            fg="red"
        )
    else:
        result_label.config(
            text=f"✅ SAFE EMAIL\nConfidence: {confidence:.2f}%",
            fg="green"
        )
    
    time = datetime.now().strftime("%H:%M:%S")
    history.append(f"{time} - {result_label.cget('text')}")
    history_box.insert(tk.END, history[-1])

# ===================================
# |        CLEAR FUNCTION           |
# ===================================

def clear_text():
    email_text.delete("1.0", tk.END)
    result_label.config(text = "")
    risk_bar["value"] = 0

# ===================================
# |      CREATE MAIN WINDOW         |
# ===================================

root = tk.Tk()
root.title("Phishing Email Detector")
root.geometry("700x750")
root.configure(bg = "white")

# ===================================
# |              TITLE               |
# ===================================

title = tk.Label(
    root,
    text = "Phishing Email Detector",
    font = ("Arial", 22, "bold"),
    bg = "white",
    fg = "darkblue"
)

title.pack(pady = 20)

# ===================================
# |           LABEL                 |
# ===================================

email_label = tk.Label(
    root,
    text = "Enter Email Message : ",
    font = ("Arial", 14),
    bg = "white"
)

email_label.pack()

# ===================================
# |            TEXT BOX             |
# ===================================

email_text = tk.Text(
    root,
    width = 70,
    height = 10,
    font = ("Arial", 12)
)

email_text.pack(pady = 10)

# ===================================
# |         CHECK BUTTON            |
# ===================================

check_button = tk.Button(
    root,
    text = "Check Email",
    font = ("Arial", 14, "bold"),
    bg = "blue",
    fg = "white",
    command = check_email
)

check_button.pack(pady = 10)

# ===================================
# |          CLEAR BUTTON           |
# ===================================

clear_button = tk.Button(
    root,
    text = "Clear Email",
    command = clear_text,
    font = ("Arial", 14, "bold"),
    bg = "blue",
    fg = "white"
)

clear_button.pack(pady = 5)

# ===================================
# |            RESULT               |
# ===================================

result_label = tk.Label(
    root,
    text = "",
    font = ("Arial", 16, "bold"),
    bg = "white",
)

result_label.pack(pady = 20)

risk_label = tk.Label(
    root,
    text = "Risk Score",
    font = ("Arial", 12, "bold"),
    bg = "white"
)

risk_label.pack()

risk_bar = ttk.Progressbar(
    root,
    orient = "horizontal",
    length = 300,
    mode = "determinate"
)

risk_bar.pack(pady = 10)

# ==================================
# |         HISTORY SECTION        |
# ==================================

history_label = tk.Label(root, text = "Detection History", font = ("Arial", 12, "bold"))
history_label.pack()

history_box = tk.Listbox(root, width = 60, height = 5)
history_box.pack(pady = 5)

root.mainloop()