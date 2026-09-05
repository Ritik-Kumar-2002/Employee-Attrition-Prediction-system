📊 **Employee Attrition Prediction & HR Analytics Dashboard**

🎯 Project Overview
--------------------------------------------------------------------------------------------------------------------------------------------------------

Employee attrition is a major challenge for organizations, as unexpected employee turnover can impact productivity, workforce stability, recruitment costs, and overall business performance.

To address this problem, I developed an end-to-end Machine Learning-based Employee Attrition Prediction and HR Analytics system using the IBM HR Analytics Employee Attrition dataset.

The system performs data preprocessing, feature selection, categorical encoding, exploratory analysis, multi-model training, performance evaluation, and probability-based employee attrition prediction, all integrated into an interactive Streamlit HR Analytics Dashboard.

The application enables HR teams to analyze workforce patterns and identify employees who may be at a higher risk of leaving the organization, supporting proactive and data-driven retention strategies.

📂 Dataset
--------------------------------------------------------------------------------------------------------------------------------------------------------
Dataset: IBM HR Analytics Employee Attrition Dataset
Original Shape: 1470 rows × 35 columns

The dataset contains employee demographic, job-related, compensation, satisfaction, and work-environment attributes that can be used to understand factors associated with employee attrition.

Tech Used
--------------------------------------------------------------------------------------------------------------------------------------------------------
Python
NumPy and Pandas
Matplotlib and Plotly
Scikit learn
Streamlit
Git - Git Hub
Machine Learning
Artifical Neural Network

🔄 ML Pipeline Workflow
--------------------------------------------------------------------------------------------------------------------------------------------------------

			Raw IBM HR Dataset
							↓
			Data Cleaning
							↓
			Feature Selection
							↓
			Categorical Encoding
			(Binary + One-Hot Encoding)
							↓
			Train / Test Split
							↓
			Feature Scaling
							↓
			5 ML Models
			 ┌──────┼────────┐────────┐────────┐
			 ↓      ↓        ↓				↓				 ↓
			LR     SVM      KNN       RF       DT
							↓
			Model Evaluation
			(Accuracy | Precision | Recall | F1)
							↓
			Best Model Selection
							↓
			Employee Attrition Prediction
							↓
			Stay / Leave Probability
							↓
			Streamlit HR Analytics Dashboard

Models Implemented
--------------------------------------------------------------------------------------------------------------------------------------------------------

Five classification algorithms were trained and evaluated:

-Logistic Regression
-Support Vector Machine (SVM)
-K-Nearest Neighbors (KNN)
-Random Forest Classifier
-Decision Tree Classifier

🏆 Best Model Selection Criteria
--------------------------------------------------------------------------------------------------------------------------------------------------------

ince employee attrition is an imbalanced classification problem, relying solely on Accuracy can be misleading.

Therefore, I designed a weighted evaluation strategy that gives higher importance to Recall and F1 Score, ensuring that the model is better aligned with the objective of identifying employees who are at risk of leaving.

⚖️ Weighted Evaluation
--------------------------------------------------------------------------------------------------------------------------------------------------------
| Metric    | Weight |
| --------- | -----: |
| Accuracy  |    10% |
| Precision |    20% |
| Recall    |    30% |
| F1 Score  |    40% |


Model Score = (0.10 × Accuracy) + (0.20 × Precision) + (0.30 × Recall) + (0.40 × F1 Score)
F1 Score and Recall is important in the imbalance class dataset

📊 Model Evaluation Scores
--------------------------------------------------------------------------------------------------------------------------------------------------------
	| Model                  | Weighted Score |
| ---------------------- | -------------: |
| 🥇 Logistic Regression |     **0.5635** |
| 🥈 SVM                 |     **0.5379** |
| 🥉 KNN                 |     **0.4103** |
| Random Forest          |     **0.3226** |
| Decision Tree          |     **0.2620** |

🏅 Best Performing Model
--------------------------------------------------------------------------------------------------------------------------------------------------------
Logistic Regression achieved the highest weighted evaluation score of:
0.5635

Therefore, Logistic Regression was selected as the best-performing model for employee attrition prediction based on the defined evaluation strategy

🔮 Employee-Level Attrition Prediction
--------------------------------------------------------------------------------------------------------------------------------------------------------
The selected model is integrated into the Streamlit application to provide real-time employee-level predictions.

Users can enter an employee's relevant attributes through the dashboard, after which the system predicts:

🟢 Likely to Stay
🔴 Likely to Leave
📈 Probability of Staying
📉 Probability of Leaving
⚠️ Attrition Risk Level

📊 Interactive HR Analytics Dashboard
--------------------------------------------------------------------------------------------------------------------------------------------------------
The project is implemented using Streamlit to provide an interactive interface for HR analytics and employee attrition prediction.

Dashboard capabilities include:
📌 HR workforce KPIs
📊 Model performance comparison
🔥 Correlation/heatmap analysis
👥 Employee-level analysis
🎯 Attrition prediction
📈 Stay vs. Leave probability
⚠️ Employee attrition risk assessment

The dashboard makes the ML results easier to interpret and provides a practical interface for exploring HR-related insights.

DemoLink
--------------------------------------------------------------------------------------------------------------------------------------------------------
https://drive.google.com/file/d/1bYa0dr3iPiG3eGFTM71LCBU7UR90fQ18/view?usp=sharing

🎯 Future Scope – Explainable AI (XAI)
--------------------------------------------------------------------------------------------------------------------------------------------------------
Future work includes integrating Explainable AI (XAI) techniques to interpret the model's predictions and identify the key factors influencing an employee's likelihood of leaving the organization. This will improve model transparency and help HR teams make data-driven employee retention decisions.
