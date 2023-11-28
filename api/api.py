from flask import Flask, json, request
from flask_cors import CORS
import threading, random, time

expected_air_flow, air_flow, pm25, pm10 = 0, 0, 0, 0
air_state = 'keep'

expected_water_flow, water_flow, tds = 0, 0, 0
water_state = 'keep'

def adjust_air_flow():
    global air_flow, air_state, expected_air_flow
    # while True:
    if expected_air_flow > 30:
        expected_air_flow = 30
    if expected_air_flow != air_flow:
        air_state = 'increase' if expected_air_flow > air_flow else 'decrease'
    elif expected_air_flow == air_flow:
        air_state = 'keep'
    if air_state != 'keep':
        change_factor = 5
        if abs(expected_air_flow - air_flow) < 10:
            change_factor = 1
        if air_state == 'increase':
            air_flow += change_factor
        if air_state == 'decrease':
            air_flow -= change_factor

def adjust_water_flow():
    global water_flow, water_state, expected_water_flow
    # while True:
    if expected_water_flow != water_flow:
        water_state = 'increase' if expected_water_flow > water_flow else 'decrease'
    elif expected_water_flow == water_flow:
        water_state = 'keep'
    if water_state != 'keep':
        change_factor = 5
        if abs(expected_water_flow - water_flow) < 10:
            change_factor = 1
        if water_state == 'increase':
            water_flow += change_factor
        if water_state == 'decrease':
            water_flow -= change_factor

def random_air_data():
    global air_flow, pm25, pm10, expected_air_flow
    print('hilo aire iniciado')
    while True:
        # air_flow = round(random.uniform(expected_air_flow*0.7, expected_air_flow*1.2), 2)
        adjust_air_flow()
        pm_factor = 0.1
        if water_flow == 0:
            pm_factor = 1
        pm25 = round(random.uniform(expected_air_flow*(1/((pm_factor*2)+water_flow)), expected_air_flow*(1/(pm_factor+water_flow)))*10, 2)
        pm10 = round(random.uniform(expected_air_flow*(1/((pm_factor*2)+water_flow)), expected_air_flow*(1/(pm_factor+water_flow)))*10, 2)
        time.sleep(1)

def random_water_data():
    global expected_water_flow, water_flow, tds
    print('hilo agua iniciado')
    while True:
        # water_flow = round(random.uniform(expected_water_flow*0.7, expected_water_flow*1.2), 2)
        adjust_water_flow()
        tds = round(random.uniform(expected_water_flow*15, expected_water_flow*18), 2)
        time.sleep(1)


api =  Flask(__name__)
CORS(api)

@api.route('/api/data', methods=['GET'])
def get_data():
    global expected_air_flow, expected_water_flow
    data = {
        'air_flow': air_flow,
        'pm25': pm25,
        'pm10': pm10,
        'water_flow': water_flow,
        'tds': tds,
        'expected_air': expected_air_flow,
        'expected_water': expected_water_flow
    }
    return json.dumps(data)

@api.route('/api/data/control', methods=['GET'])
def get_control_data():
    global expected_air_flow, expected_water_flow
    data = {
        'current_air_flow': expected_air_flow,
        'current_water_flow': expected_water_flow
    }
    return json.dumps(data)

@api.route('/api/control', methods=['POST'])
def set_control_params():
    global expected_air_flow, expected_water_flow

    data = request.json
    try:
        expected_air_flow = int(data['expected_air_flow'])
    except:
        pass

    try:
        expected_water_flow = int(data['expected_water_flow'])
    except:
        pass

    response = {"message": "Datos recibidos con éxito!"}
    return json.dumps(response), 201

if __name__ == '__main__':
    air_data_thread = threading.Thread(target=random_air_data)
    water_data_thread = threading.Thread(target=random_water_data)
    air_data_thread.daemon = True
    water_data_thread.daemon = True
    air_data_thread.start()
    water_data_thread.start()
    api.run(host="0.0.0.0",debug=True)