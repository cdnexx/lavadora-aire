from flask import Flask, json, request
import threading, random, time

companies = [{"id": 1, "name": "Company1"}, {"id": 2, "name": "Company2"}]

expected_air_flow = 10
air_flow, pm25, pm10 = 0, 0, 0

expected_water_flow = 15
water_flow, tds = 0, 0

def random_air_data():
    global air_flow, pm25, pm10, expected_air_flow
    print('hilo aire iniciado')
    while True:
        air_flow = round(random.uniform(expected_air_flow*0.7, expected_air_flow*1.2), 2)
        pm25 = round(random.uniform(expected_air_flow, expected_air_flow*1.5), 2)
        pm10 = round(random.uniform(expected_air_flow, expected_air_flow*1.8), 2)
        time.sleep(0.5)

def random_water_data():
    global expected_water_flow, water_flow, tds
    print('hilo agua iniciado')
    while True:
        water_flow = round(random.uniform(expected_water_flow*0.7, expected_water_flow*1.2), 2)
        tds = round(random.uniform(expected_water_flow*15, expected_water_flow*18), 2)
        time.sleep(0.5)


api =  Flask(__name__)

@api.route('/api/data', methods=['GET'])
def get_data():
    global expected_air_flow, expected_water_flow
    air_query = request.args.get('expected_air_flow')
    if air_query:
        expected_air_flow = int(air_query)
    water_query = request.args.get('expected_water_flow')
    if water_query:
        expected_water_flow = int(water_query)

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

if __name__ == '__main__':
    air_data_thread = threading.Thread(target=random_air_data)
    water_data_thread = threading.Thread(target=random_water_data)
    air_data_thread.daemon = True
    water_data_thread.daemon = True
    air_data_thread.start()
    water_data_thread.start()
    api.run(host="0.0.0.0",debug=True)