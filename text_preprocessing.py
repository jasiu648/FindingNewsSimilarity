import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from collections import Counter

def to_bag_of_words(text):
   
    # Tokenization: Split the text into words or tokens
    tokens = word_tokenize(text)

    # Lowercasing: Convert tokens to lowercase
    tokens = [word.lower() for word in tokens]

    # Removing Punctuation: Remove non-alphanumeric characters
    tokens = [word for word in tokens if word.isalnum()]

    # Removing Stopwords: Remove common words (e.g., 'the', 'is', 'a') that may not carry meaningful information
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]

    # Stemming: Reduce words to their base or root form
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

    # Lemmatization: Reduce words to their base form using WordNet lemmatizer
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word, wordnet.VERB) for word in stemmed_tokens]

    word_counts = Counter(lemmatized_tokens)

    return word_counts
