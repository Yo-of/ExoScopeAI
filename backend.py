from flask import Flask, request, jsonify
import pandas as pd
import numpy as np

def dummy_predict(X):
    return np.random.randint(0, 2, size=(X.shape[0], 1))

def preprocess_csv(data, seq_length=100):
    light_curve = data['flux'].values
    X = []
    for i in range(len(light_curve)-seq_length):
        X.append(light_curve[i:i+seq_length])
    X = np.array(X).reshape(len(X), seq_length, 1)
    return X

app = Flask(__name__)

@app.route("/predict", methods=['POST'])
def predict():
    file = request.files['file']
    data = pd.read_csv(file)
    X = preprocess_csv(data)
    pred = dummy_predict(X)
    return jsonify({'prediction': pred.tolist()})

if __name__ == "__main__":
    app.run(debug=True)