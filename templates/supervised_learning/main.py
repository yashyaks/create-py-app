from sklearn.datasets import load_iris


def load_data():
    data = load_iris()
    return data.data, data.target

X, y = load_data()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)