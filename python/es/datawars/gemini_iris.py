import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix

# Load the iris dataset
data = pd.read_csv("iris.csv")

# Extract features and target variable
X = data.drop("species", axis=1)
y = data["species"]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define a dictionary of machine learning models
models = {
    "Logistic Regression": LogisticRegression(),
    "K-Nearest Neighbors": KNeighborsClassifier(),
    "Support Vector Machine": SVC(),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier()
}

# Iterate over each model and evaluate its performance
for model_name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Calculate performance metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average="weighted")
    recall = recall_score(y_test, y_pred, average="weighted")
    f1 = f1_score(y_test, y_pred, average="weighted")

    # Print the evaluation results
    print(f"\n{model_name}:")
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1-score:", f1)
    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))

# Hyperparameter tuning (optional)
# You can use techniques like GridSearchCV or RandomizedSearchCV to optimize
# hyperparameters for each model. Here's an example using GridSearchCV:
# from sklearn.model_selection import GridSearchCV
# param_grid = {'n_neighbors': range(1, 11)}
# knn = KNeighborsClassifier()
# grid_search = GridSearchCV(knn, param_grid, cv=5)
# grid_search.fit(X_train, y_train)
# best_params = grid_search.best_params_
# best_knn = grid_search.best_estimator_
# # Evaluate the best KNN model