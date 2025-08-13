# Cervical Cancer Prediction

A machine learning-based web application for early risk assessment of cervical cancer.  
The system predicts whether a person is at **Risk** or **No Risk** based on demographic, behavioral, and clinical attributes.  
Built with **Python, Flask, and XGBoost**, the model achieved **97% accuracy** in testing.


## 📌 Features
- **Web-based Interface** – Easy-to-use form for entering patient details.
- **Real-time Predictions** – Outputs “Risk” or “No Risk” instantly.
- **High Accuracy** – XGBoost classifier trained on cleaned and preprocessed dataset.
- **Scalable Architecture** – Modular design for easy upgrades.
- **Visual Feedback** – Clear results with sample output screenshots.

## 🛠️ Tech Stack
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Machine Learning:** XGBoost, Scikit-learn, Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Deployment Ready:** Model serialized using Pickle for fast loading


## 📊 Dataset
The dataset contains demographic and behavioral features such as:
- Age
- Number of sexual partners
- Number of pregnancies
- Smoking status
- Hormonal contraceptive use
- History of STDs

> ⚠️ If the dataset is not open-source, remove it before making the repository public.


## 🚀 Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/chandiniAgowda/Cervical-Cancer-Prediction.git
cd cervical-cancer-prediction/src
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Run the application
```bash
python app.py
```
4. Access in browser
```cpp
http://127.0.0.1:5000
```

## 📈 Results
- Accuracy: 97%
- Precision: 0.98
- Recall: 0.97
- F1-Score: 0.97



## 🔮 Future Enhancements
- Integration of HPV and Pap smear test results.
- Multi-class risk levels instead of binary classification.
- Mobile application version.
- Explainable AI with SHAP/LIME.
- Multilingual support for wider accessibility.

## 📜 License
This project is licensed under the MIT License.

