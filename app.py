from flask import Flask, request, jsonify
# Initialiser Flask
app = Flask(name)  # name doit être avec double underscore

# Endpoint pour prédiction
@app.route("/predict", methods=["POST"])
def predict():
    # Récupérer le texte envoyé dans la requête JSON
    text = request.json["email"]
    
    # Transformer le texte en vecteur TF-IDF (le vectorizer doit être défini avant)
    vector = vectorizer.transform([text])
    
    # Prédire la classe avec le modèle Naive Bayes (le modèle doit être entraîné avant)
    prediction = model.predict(vector)
    
    # Retourner la classe prédite en JSON
    return jsonify({"classe": prediction[0]})

# Lancer le serveur Flask
if name == "main":
    app.run(host="0.0.0.0", port=5000)
