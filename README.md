# Ann-Classification-Churn
This project uses an Artificial Neural Network (ANN) to predict customer churn based on user data like age, balance, and tenure. It includes data preprocessing, model training using Keras, and deployment using Flask for real-time predictions. Helpful for business retention strategies.
📉 Customer Churn Prediction using Artificial Neural Network (ANN)
📌 Project Overview

Customer churn is one of the most critical challenges faced by businesses, especially in banking, telecom, SaaS, and subscription-based industries. Retaining existing customers is significantly more cost-effective than acquiring new ones.

This project implements an Artificial Neural Network (ANN) to predict customer churn based on demographic and behavioral features such as age, balance, tenure, credit score, and activity status.
The trained model is deployed using Flask, enabling real-time churn predictions via a web interface or API.

🎯 Objectives

Predict whether a customer is likely to churn (leave) or stay

Help businesses design data-driven retention strategies

Demonstrate an end-to-end ML lifecycle:

Data preprocessing

Model training

Evaluation

Deployment

🧠 Why ANN for Churn Prediction?

Handles non-linear relationships in customer behavior

Learns complex feature interactions

Scales well with larger datasets

Suitable for binary classification problems like churn

### 🛠️ Tech Stack
| Component            | Technology                 |
| -------------------- | -------------------------- |
| Programming Language | Python                     |
| ML Framework         | Keras (TensorFlow backend) |
| Data Processing      | Pandas, NumPy              |
| Visualization        | Matplotlib, Seaborn        |
| Model Deployment     | Flask                      |
| Frontend (Optional)  | HTML, CSS                  |
| Model Serialization  | Pickle / HDF5              |

📊 Dataset Description

The dataset contains customer-level information commonly found in banking or subscription datasets.

| Feature         | Description                               |
| --------------- | ----------------------------------------- |
| Age             | Customer age                              |
| Balance         | Account balance                           |
| Tenure          | Number of years with the company          |
| CreditScore     | Customer credit score                     |
| Geography       | Customer location                         |
| Gender          | Male/Female                               |
| IsActiveMember  | Activity status                           |
| NumOfProducts   | Number of products used                   |
| EstimatedSalary | Annual estimated salary                   |
| Exited          | Target variable (1 = Churn, 0 = Retained) |

🔢 Key Features

| Feature         | Description                               |
| --------------- | ----------------------------------------- |
| Age             | Customer age                              |
| Balance         | Account balance                           |
| Tenure          | Number of years with the company          |
| CreditScore     | Customer credit score                     |
| Geography       | Customer location                         |
| Gender          | Male/Female                               |
| IsActiveMember  | Activity status                           |
| NumOfProducts   | Number of products used                   |
| EstimatedSalary | Annual estimated salary                   |
| Exited          | Target variable (1 = Churn, 0 = Retained) |

🧪 Project Workflow
1️⃣ Data Preprocessing

Handling missing values

Encoding categorical variables

Feature scaling using StandardScaler

Train-test split

2️⃣ Model Building (ANN)

Input layer with customer features

Hidden layers with ReLU activation

Output layer with Sigmoid activation

Binary Cross-Entropy loss function

Adam optimizer

3️⃣ Model Training

Batch training

Validation split

Accuracy and loss monitoring

4️⃣ Model Evaluation

Accuracy score

Confusion matrix

Precision, Recall, F1-score

5️⃣ Deployment

Trained ANN model saved

Flask app for real-time predictions

User inputs customer data

Model returns churn probability

