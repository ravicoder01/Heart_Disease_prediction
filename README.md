💓 Heart Disease Prediction Web App

A machine learning–powered web application that predicts the likelihood of heart disease based on medical input data.
This project uses a trained ML model integrated with Flask as a backend and a clean web UI for user interaction.

🌐 Live Demo: https://heart-disease-prediction-2o96.onrender.com

🚀 Features

🔍 Predicts heart disease likelihood based on medical parameters

🧠 Trained Machine Learning model (saved as model.pkl)

🌐 Flask backend API integrated with a simple web interface

📊 Clean and minimal HTML form for data input

☁️ Deployed live using Render

🧩 Tech Stack
Component	Technology Used
Machine Learning	Scikit-learn
Backend	Flask
Frontend	HTML, CSS
Deployment	Render
Language	Python 3
⚙️ How It Works

User fills the input form with medical details like Age, Cholesterol, etc.

Data is sent to the Flask /predict route via POST request.

The model processes the data and returns:

1 → ⚠️ Heart Disease Likely

0 → ✅ No Heart Disease

The prediction is displayed instantly on the webpage.

## 📁 Project Structure

```
heart_failure_prediction/
│
├── model.pkl               # Trained ML model
├── columns.json            # Feature names used during training
│
├── app.py                  # Flask backend
│
├── index.html              # Frontend (user input form)
├── requirements.txt        # Required dependencies
└── README.md               # Project documentation
```

🧠 Model Details

Dataset used: Heart Disease UCI Dataset (Kaggle / open source)

Preprocessing: Label Encoding, One-Hot Encoding, Feature Scaling

Algorithm: Decision Tree, RandomForest,One-hot encoding

Accuracy: Decision Tree (86%)
          RandomForest (87.50%)

🧰 Installation & Run Locally

If you want to run this app locally:

# 1️⃣ Clone the repository
git clone https://github.com/yourusername/heart_failure_prediction.git

# 2️⃣ Navigate to the project folder
cd heart_failure_prediction

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the app
python app.py


Visit http://127.0.0.1:5000 in your browser 🚀

🌍 Deployment

The app is deployed using Render free web service.

To deploy yourself:

Create a Render account

Connect your GitHub repo

Set Start Command → python app.py

Deploy and wait for it to go live 🌐

📸 Preview

<img width="700" height="987" alt="image" src="https://github.com/user-attachments/assets/62c61b95-b5ce-451a-a69a-9f698f0337ed" />

👨‍💻 Author

Ravi Roy
🎓 CSE (AI/ML) Student | IILM University
💡 Passionate about  Machine Learning & AI
🔗 LinkedIn https://www.linkedin.com/in/ravi-raj-03226b240/
 | GitHub  https://github.com/ravicoder01
