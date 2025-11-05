from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_digits
import pandas as pd
import matplotlib.pyplot as plt

# Load in the dataset from CSV using Pandas
data = pd.read_csv("iris.csv")

X = data.drop(["species"], axis=1)
y = data["species"]

# Split data into training samples and test samples
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create a decision tree classifier
dt = DecisionTreeClassifier()

# Train Decision Tree Classifier
dt_model = dt.fit(X_train, y_train)

# Test the model against the test data
dt_pred = dt_model.predict(X_test)

print(f"Decision Tree accuracy is {accuracy_score(y_test, dt_pred)}")

# ------- New example with KNN, using same dataset -----

# Create a KNN classifier
neigh = KNeighborsClassifier(n_neighbors=3)

knn_model = neigh.fit(X, y)

knn_pred = knn_model.predict(X_test)

print(f"KNN accuracy is {accuracy_score(y_test, knn_pred)}")

# Random Forest
rfcl = RandomForestClassifier(n_estimators=10)
rfModel = rfcl.fit(X_train, y_train)

rfPrediction = rfcl.predict(X_test)

print(f"Random Forest accuracy is {accuracy_score(y_test, rfPrediction)}")

# SVM
svm = SVC()
svmModel = svm.fit(X_train, y_train)

svmPrediction = svm.predict(X_test)

print(f"SVM accuracy is {accuracy_score(y_test, svmPrediction)}")

# Neural Network
mlpClassifier = MLPClassifier(hidden_layer_sizes=2, activation="relu", max_iter=10000)
mlpModel = mlpClassifier.fit(X_train, y_train)

mlpPrediction = mlpClassifier.predict(X_test)

print(f"MLP accuracy is {accuracy_score(y_test, mlpPrediction)}")

# Matplotlib Example

digits = load_digits()
X, y = digits.data, digits.target
fig, axes = plt.subplots(1, 5, figsize=(10, 3))

for i, ax in enumerate(axes):
    ax.imshow(digits.images[i], cmap='gray')
    ax.set_title(f"Label: {digits.target[i]}")
    ax.axis('off')
plt.show()