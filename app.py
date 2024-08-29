from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle
import warnings


data_template = pd.read_csv("head.csv")

# Load the trained model
pickle_file = "model.sav"
model = pickle.load(open(pickle_file, "rb"))

app = Flask(__name__)

def predict(json_data):
    car_origin_private = json_data.get("car_origin_private", 0)
    seating_capacity = json_data.get("seating_capacity", 0)
    car_brand = json_data.get("car_brand", "")
    car_model = json_data.get("car_model", "")
    year = json_data.get('year', 0)
    gear_type = json_data.get("gear_type", "")
    gas_type = json_data.get("gas_type", "")
    odometer = json_data.get("odometer", 0)
    engine_power = json_data.get("engine_power", 0)
    sunroof = json_data.get("sunroof", 0)

    data = pd.DataFrame(0, index=[0], columns=data_template.columns)

    if "car_model_" + car_model in data.columns:
        data['car_model_' + car_model] = 1
    data["engine_power"] = engine_power
    data['odometer'] = odometer
    data['seating_capacity'] = seating_capacity
    data["sunroof"] = sunroof
    if "gas_type_" + gas_type in data.columns:
        data["gas_type_" + gas_type] = 1
    if "gear_type_" + gear_type in data.columns:
        data["gear_type_" + gear_type] = 1
    data["Year"] = year
    data["car_origin_private"] = car_origin_private
    if "car_brand_" + car_brand in data.columns:
        data["car_brand_" + car_brand] = 1

    prediction = model.predict(data)
    return prediction[0]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_route():
    data = request.json
    prediction_result = predict(data)
    return jsonify({"predicted_price": int(prediction_result)})

if __name__ == "__main__":
    app.run(debug=True)
