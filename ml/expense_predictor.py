import numpy as np

from sklearn.linear_model import LinearRegression

def predict_next_month(monthly_amounts):

    if len(monthly_amounts) < 2:
        return None
    
    X = np.arange(len(monthly_amounts)).reshape(-1,1)
    y = np.array(monthly_amounts)

    model = LinearRegression()
    model.fit(X,y)

    next_month = np.array([[len(monthly_amounts)]])

    prediction = model.predict(next_month)

    return round(float(prediction[0]), 2)