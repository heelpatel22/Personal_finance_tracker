import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

data = pd.read_csv('ml/dataset.csv')

X = data['description']
y = data['category']

vectorizer = TfidfVectorizer()

X_vectorized = vectorizer.fit_transform(X)

model = LogisticRegression()

model.fit(X_vectorized,y)

pickle.dump(model, open('ml/model.pkl','wb'))

pickle.dump(vectorizer, open('ml/vectorizer.pkl','wb'))

print('Model trained and saved successfully.')