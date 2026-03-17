from flask import Flask, request, jsonify
import requests
app = Flask(__name__)  
@app.route("/predict", methods=["POST"])
def predict():
    text = request.json["email"]
    vector = vectorizer.transform([text])
    prediction = model.predict(vector)  
    return jsonify({"classe": prediction[0]})
if name == "main":
    app.run(host="0.0.0.0", port=5000)

data = {"email": "urgent meeting tomorrow"}
response = requests.post("http://127.0.0.1:5000/predict", json=data)
print(response.json())
