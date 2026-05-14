import numpy as np
from sklearn.ensemble import IsolationForest

def detect_anomaly(amounts,new_amount):

    if len(amounts) < 5:
        return False
    
    X = np.array(amounts).reshape(-1,1)

    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(X)

    prediction = model.predict([[new_amount]])

    return prediction[0] == -1