import pandas as pd
from sklearn.model_selection import train_test_split
from model import train_model, evaluate_model, save_model
from preprocess import preprocess_data

# Load the data
df = pd.read_csv('data/sentiment140.csv', encoding='latin-1', header=None)

# Rename the columns
df.columns = ['target', 'id', 'date', 'flag', 'user', 'text']

# Preprocess the data
vectors, labels = preprocess_data(df)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(vectors, labels, test_size=0.2, random_state=42)

# Train the model
model = train_model(X_train, y_train)

# Evaluate the model
evaluate_model(model, X_test, y_test)

# Save the model
save_model(model, 'models/logistic_regression.pkl')
