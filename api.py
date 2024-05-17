from flask import Flask, jsonify, request
import pandas as pd
import pickle

data = pd.read_csv("/head.csv")

pickle_file = "./model.sav"

model = pickle.load(open(pickle_file, "rb"))

app = Flask(__name__)
@app.route("/predict", methods=["POST"])
def predict():
    json_data = request.get_json()

    car_origin_private = json_data.get("car_origin_private")
    seating_capacity = json_data.get("seating_capacity")
    car_brand = json_data.get("car_brand")
    car_model = json_data.get("car_model")
    year = json_data.get('year')
    gear_type = json_data.get("gear_type")
    gas_type = json_data.get("gas_type")
    odometer = json_data.get("odometer")
    engine_power = json_data.get("engine_power")
    sunroof = json_data.get("sunroof")

    data['car_model_' + car_model] = 1
    data["engine_power"] = engine_power
    data['odometer'] = odometer
    data['seating_capacity'] = seating_capacity
    data["sunroof"] = sunroof
    data["gas_type_" + gas_type] = 1
    data["gear_type_" + gear_type] = 1
    data["Year"] = year
    data["car_origin_private"] = car_origin_private
    data["car_brand_" + car_brand] = 1

    prediction = model.predict(data)
    return jsonify({"prediction": list(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
