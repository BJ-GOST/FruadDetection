#making all needed imports
import pandas as pd
import numpy as np 
from sklearn.tree import DecisionTreeClassifier #this is used to train our model
from sklearn.metrics import accuracy_score #this is used to test for accuracy of the trained model
from sklearn.model_selection import train_test_split #this is used to split the dataset into training and testing seys
import joblib


#creating a dataframe from the csv file
credit_dataset = pd.read_csv('creditcard.csv')
#print(credit_dataset) to view dataset in terminal

#checking our dataset information to confirm irregularities
data_info = credit_dataset.info()

#checking for null values
null_values = credit_dataset.isnull().sum()

#checking for the distribution of legal transactions and fraudulent transactions
#this line of code returns the total number of legal transactions and fraudulent transactions
#0--> represents the legal data
#1--> represents fraudulent transactions
value_count = credit_dataset['Class'].value_counts()
#print(value_count)
#this dataset is imbalanced with the legal transactions covering about 90% of the total data and therefore has to be balanced


#to balance the data we have to first divide the values of the 'Class' column into two variables; legal, fraud, for further analysis
legal_dataset = credit_dataset[credit_dataset.Class==0]
fraud_dataset = credit_dataset[credit_dataset.Class==1]


#getting statistics for the two variables by getting the data of the 'amount' in each of them
legal_dataset.Amount.describe()
fraud_dataset.Amount.describe()
#this can be displayed on the terminal using the 'print()' function


#compare the values for both transactions
credit_dataset.groupby('Class').mean()
#this compares the mean of fraud and legal transactions across all columns


#after data analysis we are going to undersample
#undersampling is the building of a minor dataset from the original dataset
#in this case we are going to build a dataset with normal distributions of legal and fraud transactions
"""because our fraud transactions consist of 492 values we are going to randomly select 492 values from
the legal transactions and join them to the fraud transactions to create a new dataset"""

legal_sample = legal_dataset.sample(n=492)#creating a legal sample
legal_fraud_dataset = pd.concat([legal_sample, fraud_dataset], axis=0)#joining the two datasets
#print(legal_fraud_dataset) to display in terminal

#analyzing the new datasets
#number of values for each of fraud and legal transactions
lf_value_count = legal_fraud_dataset['Class'].value_counts()
#print(lf_value_count)

#the mean comparison between the two transactions
lf_mean_comparison = legal_fraud_dataset.groupby('Class').mean()
#print(lf_mean_comparison)


#splitting the data into features and targets for training
X= legal_fraud_dataset.drop(columns='Class', axis=1)
Y= legal_fraud_dataset['Class']

#Split the data into training data and testing data
X_train,X_test,Y_train,Y_test = train_test_split(X,Y, test_size=0.2,stratify=Y,random_state=2) 
#print(X.shape,X_train.shape,X_test.shape)

#instantiating the model for training the data
model = DecisionTreeClassifier()
model.fit(X_train,Y_train)

#testing accuracy
X_train_prediction = model.predict(X_train)

#the variable containing the accuracy
training_data_accuracy = accuracy_score(X_train_prediction,Y_train)

#display the accuracy of the prediction
print("Accuracy :",training_data_accuracy)

#saving the model to a file where it can be later accessed
joblib.dump(model, 'FraudPrediction.joblib')
