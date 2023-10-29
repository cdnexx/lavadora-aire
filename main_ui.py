# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\lavadora.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 230)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.water_level_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.water_level_bar.setGeometry(QtCore.QRect(570, 10, 41, 161))
        self.water_level_bar.setStyleSheet("QProgressBar {\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"     background-color: rgb(105, 195, 255);\n"
" }")
        self.water_level_bar.setProperty("value", 25)
        self.water_level_bar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.water_level_bar.setTextVisible(True)
        self.water_level_bar.setOrientation(QtCore.Qt.Vertical)
        self.water_level_bar.setInvertedAppearance(False)
        self.water_level_bar.setObjectName("water_level_bar")
        self.control_group_box = QtWidgets.QGroupBox(self.centralwidget)
        self.control_group_box.setGeometry(QtCore.QRect(10, 0, 211, 171))
        self.control_group_box.setObjectName("control_group_box")
        self.air_control_input = QtWidgets.QSpinBox(self.control_group_box)
        self.air_control_input.setGeometry(QtCore.QRect(120, 20, 81, 31))
        self.air_control_input.setObjectName("air_control_input")
        self.air_control_label = QtWidgets.QLabel(self.control_group_box)
        self.air_control_label.setGeometry(QtCore.QRect(10, 20, 81, 31))
        self.air_control_label.setObjectName("air_control_label")
        self.water_control_label = QtWidgets.QLabel(self.control_group_box)
        self.water_control_label.setGeometry(QtCore.QRect(10, 90, 81, 31))
        self.water_control_label.setObjectName("water_control_label")
        self.water_control_input = QtWidgets.QSpinBox(self.control_group_box)
        self.water_control_input.setGeometry(QtCore.QRect(120, 90, 81, 31))
        self.water_control_input.setObjectName("water_control_input")
        self.air_control_slider = QtWidgets.QSlider(self.control_group_box)
        self.air_control_slider.setGeometry(QtCore.QRect(10, 60, 191, 22))
        self.air_control_slider.setMaximum(30)
        self.air_control_slider.setProperty("value", 0)
        self.air_control_slider.setOrientation(QtCore.Qt.Horizontal)
        self.air_control_slider.setTickInterval(1)
        self.air_control_slider.setObjectName("air_control_slider")
        self.water_control_slider = QtWidgets.QSlider(self.control_group_box)
        self.water_control_slider.setGeometry(QtCore.QRect(10, 130, 191, 22))
        self.water_control_slider.setMaximum(30)
        self.water_control_slider.setOrientation(QtCore.Qt.Horizontal)
        self.water_control_slider.setObjectName("water_control_slider")
        self.readings_group = QtWidgets.QGroupBox(self.centralwidget)
        self.readings_group.setGeometry(QtCore.QRect(230, 0, 331, 171))
        self.readings_group.setObjectName("readings_group")
        self.air_readings_group = QtWidgets.QGroupBox(self.readings_group)
        self.air_readings_group.setGeometry(QtCore.QRect(10, 20, 311, 71))
        self.air_readings_group.setObjectName("air_readings_group")
        self.pm10_entry = QtWidgets.QLineEdit(self.air_readings_group)
        self.pm10_entry.setGeometry(QtCore.QRect(210, 40, 91, 21))
        self.pm10_entry.setReadOnly(True)
        self.pm10_entry.setObjectName("pm10_entry")
        self.pm10_label = QtWidgets.QLabel(self.air_readings_group)
        self.pm10_label.setGeometry(QtCore.QRect(210, 20, 91, 21))
        self.pm10_label.setObjectName("pm10_label")
        self.air_flux_label = QtWidgets.QLabel(self.air_readings_group)
        self.air_flux_label.setGeometry(QtCore.QRect(10, 20, 91, 21))
        self.air_flux_label.setObjectName("air_flux_label")
        self.pm25_label = QtWidgets.QLabel(self.air_readings_group)
        self.pm25_label.setGeometry(QtCore.QRect(110, 20, 91, 21))
        self.pm25_label.setObjectName("pm25_label")
        self.pm25_entry = QtWidgets.QLineEdit(self.air_readings_group)
        self.pm25_entry.setGeometry(QtCore.QRect(110, 40, 91, 21))
        self.pm25_entry.setReadOnly(True)
        self.pm25_entry.setObjectName("pm25_entry")
        self.air_flux_entry = QtWidgets.QLineEdit(self.air_readings_group)
        self.air_flux_entry.setGeometry(QtCore.QRect(10, 40, 91, 21))
        self.air_flux_entry.setReadOnly(True)
        self.air_flux_entry.setObjectName("air_flux_entry")
        self.water_readings_group = QtWidgets.QGroupBox(self.readings_group)
        self.water_readings_group.setGeometry(QtCore.QRect(10, 90, 311, 71))
        self.water_readings_group.setObjectName("water_readings_group")
        self.water_flux_label = QtWidgets.QLabel(self.water_readings_group)
        self.water_flux_label.setGeometry(QtCore.QRect(10, 20, 91, 21))
        self.water_flux_label.setObjectName("water_flux_label")
        self.tds_label = QtWidgets.QLabel(self.water_readings_group)
        self.tds_label.setGeometry(QtCore.QRect(110, 20, 91, 21))
        self.tds_label.setObjectName("tds_label")
        self.tds_entry = QtWidgets.QLineEdit(self.water_readings_group)
        self.tds_entry.setGeometry(QtCore.QRect(110, 40, 91, 21))
        self.tds_entry.setReadOnly(True)
        self.tds_entry.setObjectName("tds_entry")
        self.water_flux_entry = QtWidgets.QLineEdit(self.water_readings_group)
        self.water_flux_entry.setGeometry(QtCore.QRect(10, 40, 91, 21))
        self.water_flux_entry.setReadOnly(True)
        self.water_flux_entry.setObjectName("water_flux_entry")
        self.message_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.message_entry.setGeometry(QtCore.QRect(10, 180, 601, 22))
        self.message_entry.setInputMask("")
        self.message_entry.setText("")
        self.message_entry.setDragEnabled(False)
        self.message_entry.setReadOnly(True)
        self.message_entry.setPlaceholderText("")
        self.message_entry.setObjectName("message_entry")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.water_level_bar.setToolTip(_translate("MainWindow", "<html><head/><body><p>Nivel de agua en el estanque</p></body></html>"))
        self.control_group_box.setTitle(_translate("MainWindow", "Control"))
        self.air_control_input.setToolTip(_translate("MainWindow", "<html><head/><body><p>Control entrada de aire</p></body></html>"))
        self.air_control_label.setText(_translate("MainWindow", "Aire [L/min]"))
        self.water_control_label.setText(_translate("MainWindow", "Agua [L/min]"))
        self.water_control_input.setToolTip(_translate("MainWindow", "<html><head/><body><p>Control entrada de agua</p></body></html>"))
        self.air_control_slider.setToolTip(_translate("MainWindow", "<html><head/><body><p>Control entrada de aire</p></body></html>"))
        self.water_control_slider.setToolTip(_translate("MainWindow", "<html><head/><body><p>Control entrada de agua</p></body></html>"))
        self.readings_group.setTitle(_translate("MainWindow", "Lectura"))
        self.air_readings_group.setTitle(_translate("MainWindow", "Aire"))
        self.pm10_entry.setToolTip(_translate("MainWindow", "<html><head/><body><p>Lectura de material particulado en el aire de diámetro inferior a 10 micras</p></body></html>"))
        self.pm10_label.setText(_translate("MainWindow", "PM 10 [µg/m3]"))
        self.air_flux_label.setText(_translate("MainWindow", "Flujo [L/min]"))
        self.pm25_label.setText(_translate("MainWindow", "PM 2.5 [µg/m3]"))
        self.pm25_entry.setToolTip(_translate("MainWindow", "<html><head/><body><p>Lectura de material particulado en el aire de diámetro inferior a 2.5 micras</p></body></html>"))
        self.air_flux_entry.setToolTip(_translate("MainWindow", "<html><head/><body><p>Lectura de flujo de aire</p></body></html>"))
        self.water_readings_group.setTitle(_translate("MainWindow", "Agua"))
        self.water_flux_label.setText(_translate("MainWindow", "Flujo [L/min]"))
        self.tds_label.setText(_translate("MainWindow", "TDS [ppm]"))
        self.tds_entry.setToolTip(_translate("MainWindow", "<html><head/><body><p>Lectura del total de sólidos disueltos en el agua</p></body></html>"))
        self.water_flux_entry.setToolTip(_translate("MainWindow", "<html><head/><body><p>Lectura de flujo de agua</p></body></html>"))
        self.message_entry.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mensajes de información relevante</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
