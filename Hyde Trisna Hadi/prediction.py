import joblib
import numpy as np

def predict(sepal_l, sepal_w, petal_l, petal_w):
    input_data = np.array([[sepal_l, sepal_w, petal_l, petal_w]])
    prediction = model.predict(input_data)
    return prediction[0]
