from PyQt5 import QtCore, QtGui, QtWidgets
from main_ui import Ui_MainWindow 
import typing
import threading
import time
import random
import requests

air_flow, pm25, pm10 = 0,0,0
water_flow, tds = 0, 0

def input_changed(value: int, fluid_type: str, change: str):
    """
    Change the paired input
    """
    update = None
    if fluid_type == "air":
        if change == "input":
            update = ui.air_control_input
        elif change == "slider":
            update = ui.air_control_slider
    elif fluid_type == "water":
        if change == "input":
            update = ui.water_control_input
        elif change == "slider":
            update = ui.water_control_slider
    update.setValue(int(value))

def receive_data():
    global air_flow, pm25, pm10, water_flow, tds
    url = 'http://192.168.1.141:5000/api/data'
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            air_flow = data['air_flow']
            pm25 = data['pm25']
            pm10 = data['pm10']
            water_flow = data['water_flow']
            tds = data['tds']
            

def update_data():
    ui.air_flux_entry.setText(str(air_flow))
    ui.pm25_entry.setText(str(pm25))
    ui.pm10_entry.setText(str(pm10))
    ui.water_flux_entry.setText(str(water_flow))
    ui.tds_entry.setText(str(tds))

class MiWidget(QtCore.QObject):
    signal = QtCore.pyqtSignal(str)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    receive_data_thread = threading.Thread(target=receive_data)
    timer = QtCore.QTimer()
    timer.timeout.connect(update_data)
    timer.start(100)
    # water_level_thread = threading.Thread(target=random_water_data)

    # app.aboutToQuit.connect(close)

    ui.air_control_slider.valueChanged['int'].connect(lambda value: input_changed(value, "air", "input"))
    ui.air_control_input.valueChanged['QString'].connect(lambda value: input_changed(value, "air", "slider"))
    ui.water_control_slider.valueChanged['int'].connect(lambda value: input_changed(value, "water", "input"))
    ui.water_control_input.valueChanged['QString'].connect(lambda value: input_changed(value, "water", "slider"))
    
    ui.message_entry.setText("OK!")

    receive_data_thread.daemon = True
    receive_data_thread.start()

    sys.exit(app.exec_())