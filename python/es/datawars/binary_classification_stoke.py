'''binary classification decision tree and knn'''
#Importing required libraries
#import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
#load dataset
df = pd.read_csv('healthcare-dataset-stroke-data.csv')
df.info()
print(df.head())

#preprocessing data
#dropping missing values
percent_missing = round(df.isnull().sum() * 100 / len(df),3)
missing_value_df = pd.DataFrame({'Missing_Percentage': percent_missing})
missing_value_df.sort_values(by="Missing_Percentage",ascending=False).head(5)
print(missing_value_df)
df.dropna(inplace=True)

#dropping Unnecessary Features
df.drop(["id"], axis=1, inplace=True)

#Categorical variables
cat_variables = ["gender","hypertension","heart_disease",
                 "ever_married","work_type","Residence_type","smoking_status"]
# for i in cat_variables:
#     fig_dims = (10, 4)
#     fig, ax = plt.subplots(figsize=fig_dims)
#     sns.countplot(x=i, hue="stroke", ax=ax, data=df,
#       palette="RdBu",order=df[i].value_counts().index)
#     plt.xticks(rotation=90)
#     plt.legend(loc='upper right')
#     plt.show()

corr = df.corr(numeric_only=True)
corr.style.background_gradient(cmap='coolwarm').format(precision=2)

sns.set_palette("RdBu")
sns.countplot(data=df, x='stroke')
print(df.stroke.value_counts())

non_stroke=df.loc[df.stroke==0].sample(df.loc[df.stroke==1].shape[0],random_state=1)
stroke=df.loc[df.stroke==1]
frames = [stroke,non_stroke]
result = pd.concat(frames)
result.sample(frac=1,random_state=1)
result.head()
#sample the data set
variables=["stroke","gender","hypertension","heart_disease",
           'ever_married','work_type','Residence_type','smoking_status']
X=result.drop(columns =variables)
y=result.stroke

#train and test split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#decision tree

# Train the decision tree model with a maximum depth 3
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(X_train, y_train)

# Make predictions on the data
y_pred_train = dt.predict(X_train)
y_pred_test= dt.predict(X_test)
# Calculate the accuracy of the model
train_accuracy = accuracy_score(y_train, y_pred_train)
test_accuracy = accuracy_score(y_test, y_pred_test)
print('accuracy train', train_accuracy)
print('accuracy test', test_accuracy)

#K-Nearest Neighbors (KNN)

# Create a KNN classifier with different values of k
scaler = StandardScaler()
scaler=scaler.fit(X_train)
# standardization
X_train_scaler = scaler.transform(X_train)
X_test_scaler = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaler, y_train)
# Make predictions on the data
y_pred_train = knn.predict(X_train_scaler)
y_pred_test= knn.predict(X_test_scaler)
# Calculate the accuracy of the model
train_accuracy = accuracy_score(y_train, y_pred_train)
test_accuracy = accuracy_score(y_test, y_pred_test)
print('accuracy train', train_accuracy)
print('accuracy test', test_accuracy)
