from flask import Flask, jsonify, request
from sklearn.externals import joblib
from flask_swagger_ui import get_swaggerui_blueprint
import json

app = Flask(__name__)
@app.route('/predict', methods=['POST'])

def predict():
     request_dict = request.get_json(force=True)
     request_list=[request_dict.values()]
     gnb = joblib.load('data/BC_gnb.pkl')
     prediction = gnb.predict(request_list)
     return jsonify({'prediction': list(prediction)})

if __name__ == '__main__':
    app.run(port=8080)
