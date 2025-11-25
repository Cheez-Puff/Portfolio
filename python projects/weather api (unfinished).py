#3c6973818435ebd29b5c35ca2efe228f - weather api

import sys
import requests
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QApplication
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel("Temperature: N/A", self)
        self.emoji_label = QLabel("", self)
        self.description_label = QLabel("Description: N/A", self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("cityLabel")
        self.city_input.setObjectName("cityInput")
        self.get_weather_button.setObjectName("getWeatherButton")
        self.temperature_label.setObjectName("temperatureLabel")
        self.emoji_label.setObjectName("emojiLabel")
        self.description_label.setObjectName("descriptionLabel")

        self.setStyleSheet("""QLabel {
                                font-size: 18px; font-family: sans-serif;
                           }
                           QLineEdit {
                                font-size: 16px; font-family: sans-serif; padding: 5px;
                           }
                           QPushButton {
                                font-size: 16px; font-family: sans-serif; padding: 5px; background-color: #4CAF50; color: white; border: none; border-radius: 5px;
                           }
                            QPushButton:hover {
                                  background-color: #45a049; font-weight: bold;
                           }
                            QLabel#emojiLabel {
                                  font-size: 75px; font-family: Segoe UI Emoji;
                           }""")
        
        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "3c6973818435ebd29b5c35ca2efe228f"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError:
            print(response.status_code)
        except requests.exceptions.RequestException:
            pass

    def display_error(self, data):
        pass

    def display_weather(self, data):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())