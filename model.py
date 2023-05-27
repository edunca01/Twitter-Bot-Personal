import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def train_model(X_train, y_train):
    """Train a logistic regression model on the input data."""
    model = LogisticRegression(max_iter=100000)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate the model's performance on the test data."""
    predictions = model.predict(X_test)
    print(classification_report(y_test, predictions))

def save_model(model, path):
    """Save the trained model to a file."""
    with open(path, 'wb') as f:
        pickle.dump(model, f)

def load_model(path):
    """Load a trained model from a file."""
    with open(path, 'rb') as f:
        model = pickle.load(f)
    return model