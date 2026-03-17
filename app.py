from flask import Flask, request, jsonify
import pickle  # si ton model et vectorizer sont sauvegardés
import os

app = Flask(__name__)

# Charger ton modèle et vectorizer depuis des fichiers .pkl
# Assure-toi que ces fichiers sont dans le même dossier que app.py
MODEL_FILE = "model.pkl"
VECTORIZER_FILE = "vectorizer.pkl"

if os.path.exists(MODEL_FILE) and os.path.exists(VECTORIZER_FILE):
    with open(MODEL_FILE, "rb") as f:
        model = pickle.load(f)
    with open(VECTORIZER_FILE, "rb") as f:
        vectorizer = pickle.load(f)
else:
    # Pour éviter les erreurs si les fichiers manquent
    model = None
    vectorizer = None
    print("⚠️ Model or vectorizer not found. Add your model.pkl and vectorizer.pkl.")

@app.route("/predict", methods=["POST"])
def predict():
    if not model or not vectorizer:
        return jsonify({"error": "Model or vectorizer not loaded"}), 500
    
    data = request.json
    if "email" not in data:
        return jsonify({"error": "Missing 'email' in request"}), 400
    
    text = data["email"]
    vector = vectorizer.transform([text])
    prediction = model.predict(vector)
    
    return jsonify({"classe": prediction[0]})

if __name__ == "__main__":
    # Ne pas mettre de test requests ici ! Seulement démarrer le serveur
    app.run(host="0.0.0.0", port=5000)
