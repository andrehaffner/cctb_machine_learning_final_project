## DEAC109: Machine Learning
# Final Project Description 
Students: Andre Haffner and Caio Rossi
Instructor: Ron Li

# URL Link - YouTube Video: https://www.youtube.com/watch?v=csFn3EErcTA

# Dataset: https://archive.ics.uci.edu/ml/machine-learning-databases/00383/risk_factors_cervical_cancer.csv

# Project Overview: 

We worked with a dataset focused on cervical cancer risk factors, aiming to develop a logistic regression model to predict the likelihood of cervical cancer. The dataset contains various features, including age, which we believe to be crucial in understanding the risk factors associated with cervical cancer. To address this problem, we followed a systematic approach. Firstly, we sampled the dataset to manage its size while maintaining its representativeness. Next, we performed data preprocessing by dividing the dataset into input features and the target variable, with a specific emphasis on the age feature.

Afterwards, we conducted a train-test split to evaluate the model's performance accurately. To ensure compatibility with the logistic regression algorithm, we applied one-hot encoding to the categorical features, excluding age, which was already in a suitable numerical format. Following the encoding step, we trained the logistic regression model using the prepared training set, allowing it to learn the patterns and associations between the features and the target variable. Finally, we assessed the model's accuracy by making predictions on the test set and comparing them against the true labels. This project aimed to provide insights into the relationship between age and the risk of cervical cancer by leveraging a logistic regression model trained on the given dataset.

# Team Contribution Information: 

Andre Haffner: Machine Learning and Flask
Caio Rossi: Machine Learning