async function predictPrice() {
    const data = {
        "car_origin_private": document.querySelector('input[name="car_origin_private"]:checked').value,
        "seating_capacity": document.getElementById('seating_capacity').value,
        "car_brand": document.getElementById('car_brand').value,
        "car_model": document.getElementById('car_model').value,
        "year": document.getElementById('year').value,
        "gear_type": document.querySelector('input[name="gear_type"]:checked').value,
        "gas_type": document.querySelector('input[name="gas_type"]:checked').value,
        "odometer": document.getElementById('odometer').value,
        "engine_power": document.getElementById('engine_power').value,
        "sunroof": document.getElementById('sunroof').checked ? 1 : 0
    };

    const response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    document.getElementById('result').textContent = "Predicted Car Price: " + result.predicted_price;
}
