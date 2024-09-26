from flask import Flask, render_template, request
from sklearn.preprocessing import StandardScaler
import numpy as np
import joblib
import csv

model = joblib.load("rf.pkl")
scaler = joblib.load("scaler.pkl")

app = Flask(__name__, template_folder="Templates")

def read_csv(file_path):
    data = []
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

@app.route("/")
def home():
    csv_data = read_csv("delaney_solubility_with_descriptors.csv")
    return render_template("index.html", choices=csv_data)

@app.route("/predict", methods=["POST"])
def predict():
    csv_data = read_csv("delaney_solubility_with_descriptors.csv")

    # Get user inputs for the features
    input_features = [
        float(request.form["MolLogP"]),
        float(request.form["MolWt"]),
        float(request.form["NumRotatableBonds"]),
        float(request.form["AromaticProportion"])
    ]

    # Scale the user inputs
    input_features_array = np.array([input_features])
    input_features_scaled = scaler.transform(input_features_array)

    # Make a prediction using the model
    predicted_logS = round(model.predict(input_features_scaled)[0], 2)

    # Format the prediction message
    prediction = f"The solubility of this molecule (logS) is: {predicted_logS}"

    return render_template("index.html", prediction_text=prediction, choices=csv_data)

if __name__ == "__main__":
    app.run(debug=True)
