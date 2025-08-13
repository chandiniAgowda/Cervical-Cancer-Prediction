from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow cross-origin requests

# Load the model and scaler
with open('cancer_model.pkl', 'rb') as f:
    model, scaler = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the data from the request
        data = request.get_json()

        # Validate the input data
        required_fields = [
            'age', 'sexualPartners', 'firstIntercourse', 'pregnancies', 'smokes',
            'smokesYears', 'smokesPacks', 'hormonalContraceptives',
            'hormonalContraceptivesYears', 'iud', 'iudYears', 'std', 'stdNumber',
            'stdCondylomatosis', 'stdGenitalHerpes', 'stdTrichomoniasis',
            'stdPelvicInflammatoryDisease', 'stdGenitalWarts',
            'stdMolluscumContagiosum', 'stdAIDS', 'stdHIV', 'stdHepatitisB',
            'stdHepatitisC', 'stdSyphilis', 'stdFirstDiagnosis', 'stdLastDiagnosis'
        ]
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400

        # Convert data to a numpy array in the correct order
        input_data = [data[field] for field in required_fields]
        input_array = np.array([input_data])

        # Scale the input data
        scaled_data = scaler.transform(input_array)

        # Make the prediction
        prediction = model.predict(scaled_data)

        # Return the result
        return jsonify({'result': int(prediction[0])})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
