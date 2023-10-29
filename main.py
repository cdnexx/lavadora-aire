from PyQt5 import QtCore, QtGui, QtWidgets
from main_ui import Ui_MainWindow 
import typing
import threading

def input_changed(value: int, ui: Ui_MainWindow, fluid_type: str, change: str):
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.air_control_slider.valueChanged['int'].connect(lambda value: input_changed(value, ui, "air", "input"))
    ui.air_control_input.valueChanged['QString'].connect(lambda value: input_changed(value, ui, "air", "slider"))
    ui.water_control_slider.valueChanged['int'].connect(lambda value: input_changed(value, ui, "water", "input"))
    ui.water_control_input.valueChanged['QString'].connect(lambda value: input_changed(value, ui, "water", "slider"))
    
    ui.message_entry.setText("OK!")

    sys.exit(app.exec_())
