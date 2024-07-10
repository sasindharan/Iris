from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np


app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('knn_model.pkl')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({'prediction': prediction.tolist()})


if __name__ == '__main__':
    app.run(debug=True)
