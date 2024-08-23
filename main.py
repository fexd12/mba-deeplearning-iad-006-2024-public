from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

with open('models/random_forest.pkl', 'rb') as file:
    modelo = pickle.load(file)

# @app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    print(data)
    prediction = modelo.predict([data['input']])
    return jsonify({'prediction': prediction.tolist()})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)