# 🌾 Crop Recommendation System (Machine Learning Project)

An intelligent **Machine Learning web application** that recommends the most suitable crop based on soil nutrients and environmental conditions. This project is built using **Python, Scikit-learn, and Streamlit**, and provides a simple and interactive interface for farmers and researchers to make data-driven agricultural decisions.

---
## 🚀 Live Demo
👉 **Try the App Here:**
🔗 https://crops-recomendation-system-ml-project.streamlit.app/
---

## 📌 Project Overview

This project uses a **Random Forest Classifier** trained on agricultural data to predict the best crop based on:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* pH level
* Rainfall

The model analyzes soil conditions and predicts the most suitable crop with confidence scores.

---

## 🧠 Machine Learning Workflow

1. Data Collection (`Crop_recommendation.csv`)
2. Data Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Selection
5. Model Training (Random Forest Classifier)
6. Model Evaluation
7. Deployment using Streamlit

---

## 🛠️ Tech Stack

* Python 🐍
* Pandas & NumPy
* Matplotlib & Seaborn
* Scikit-learn
* Streamlit (for web app)
* Pickle (for model saving)

---

## 📊 Features

* 🌱 Predict best crop based on input soil conditions
* 📈 View dataset statistics and visualizations
* 🎯 Displays top 3 crop recommendations with probabilities
* 📉 Feature importance visualization
* 🔍 Model performance evaluation (accuracy, confusion matrix)
* ⚡ Interactive Streamlit web interface

---

## 🖥️ Web App Interface

* Sidebar inputs for soil parameters
* Real-time prediction results
* Dataset preview and insights
* Visual analytics dashboard

---

## 📁 Project Structure

```
Crops_Recomendation_System_ML_Project/
│
├── App.py                   # Streamlit web application
├── Crop_recommendation.csv  # Dataset
├── df.pkl                   # Pickle file
├── pipe.pkl                 # Trained ML model
├── requirements.txt         # Requirement.txt file
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Muhammad-Musharraf/Crops_Recomendation_System_ML_Project.git
cd Crops_Recomendation_System_ML_Project
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app

```bash
streamlit run App.py
```

---

## 📈 Model Performance

* Model Used: Random Forest Classifier
* Accuracy: ~95%+ (varies based on dataset split)
* Evaluation Metrics:

  * Accuracy Score
  * Classification Report
  * Confusion Matrix

---

## 🎯 Future Improvements

* Add Deep Learning models
* Deploy on cloud (AWS / Streamlit Cloud)
* Add weather API integration
* Improve UI/UX design
* Add multilingual support

---

## 👨‍💻 Author

**Muhammad Musharraf**
GitHub: [Muhammad-Musharraf](https://github.com/Muhammad-Musharraf)

---

## ⭐ Show Your Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 📢 Share it

---

## 📌 Repository Link

👉 [Crop Recommendation System ML Project](https://github.com/Muhammad-Musharraf/Crops_Recomendation_System_ML_Project/tree/main)



