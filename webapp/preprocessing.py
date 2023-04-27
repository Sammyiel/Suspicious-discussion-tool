import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def preprocess_text(text):
    # Remove URLs and special characters
    text = re.sub(r'http\S+|www\S+|[^a-zA-Z]', ' ', text)

    # Convert text to lowercase
    text = text.lower()

    # Tokenize text
    words = nltk.word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # Lemmatize words
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]

    # Join words back into a single string
    text = ' '.join(words)

    return text
