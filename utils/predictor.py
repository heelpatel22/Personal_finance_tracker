import pickle
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(base_dir, 'ml', 'model.pkl')
vectorizer_path = os.path.join(base_dir, 'ml', 'vectorizer.pkl')

model = pickle.load(open(model_path,'rb'))
vectorizer = pickle.load(open(vectorizer_path,'rb'))

def predict_category(description):
    text = [description]
    text_vector = vectorizer.transform(text)
    prediction = model.predict(text_vector)

    return prediction[0]