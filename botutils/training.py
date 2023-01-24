import tensorflow as tf
import pandas as pd

# Load the dataset
data = pd.read_csv("tweets.csv")

# Clean and preprocess the data

data['text'] = data['text'].apply(lambda x: ' '.join([word for word in x.split() if word.isalpha()])) #Remove numbers

# Tokenize the tweets
tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(data['text'])
sequences = tokenizer.texts_to_sequences(data['text'])

# Create training and test sets
train_data = sequences[:int(len(sequences)*0.8)]
test_data = sequences[int(len(sequences)*0.8):]
