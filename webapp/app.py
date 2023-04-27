from flask import Flask, render_template, request
import numpy as np
from joblib import load
from preprocessing import preprocess_text
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

model = load('../saved_models/suspicious_discussion_model.joblib')
vectorizer = load('../saved_models/vectorizer.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        preprocessed_message = preprocess_text(message)
        data = vectorizer.transform([preprocessed_message])
        prediction = model.predict(data)
        result = int(prediction[0])
        
        print(result)

        return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)
