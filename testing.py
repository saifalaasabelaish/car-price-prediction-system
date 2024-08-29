import pandas as pd
import pickle
import warnings

# Suppress specific sklearn warnings
warnings.filterwarnings("ignore", message="X has feature names")

# Load the CSV header (assuming it has the same structure as your model's input)
data_template = pd.read_csv("head.csv")

# Load the trained model
pickle_file = "model.sav"
model = pickle.load(open(pickle_file, "rb"))

def predict(json_data):
    # Extract features from JSON-like input dictionary
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

    # Initialize all values to 0 (except for numerical fields which you update directly)
    data = pd.DataFrame(0, index=[0], columns=data_template.columns)

    # Update the relevant fields
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

    # Make the prediction
    prediction = model.predict(data)
    return prediction

if __name__ == "__main__":
    json_data = {
        "car_origin_private": 1,
        "seating_capacity": 5,
        "car_brand": "بيحو",
        "car_model": "206",
        "year": 2013,
        "gear_type": "اوتوماتيك",
        "gas_type": "سولار",
        "odometer": 45000,
        "engine_power": 150,
        "sunroof": 0
    }
    
    # Call the predict function with the input data
    prediction_result = predict(json_data)
    print(f"Predicted car price: {int(prediction_result)}")
