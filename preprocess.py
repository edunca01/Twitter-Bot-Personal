import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    """Clean the input text."""
    # Remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
    # Remove special characters and digits
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\d', ' ', text)
    # Remove single characters
    text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text, flags=re.I)
    # Convert to lowercase
    text = text.lower()
    return text

def tokenize_and_remove_stopwords(text):
    """Tokenize the text and remove stopwords."""
    tokens = nltk.word_tokenize(text)
    tokens = [token for token in tokens if token not in stop_words]
    return tokens

def preprocess_data(df):
    """Preprocess the input DataFrame."""
    # Clean the text data
    df['text'] = df['text'].apply(clean_text)
    # Tokenize the text data and remove stopwords
    df['text'] = df['text'].apply(tokenize_and_remove_stopwords)
    # Vectorize the text data
    vectorizer = TfidfVectorizer(tokenizer=lambda x: x, preprocessor=lambda x: x)
    vectors = vectorizer.fit_transform(df['text'])
    return vectors, df['target']
