from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    weatherApiKey = '68f4fa0d68fc858ac5aa55e4524ea24f'
    city = request.form['city']
    url = "http://api.openweathermap.org/data/2.5/weather?appid=" + weatherApiKey + "&q=" + city
    data = requests.get(url).json()

    if data["cod"] != "404":
        y = data["main"]

    current_temperature = y["temp"]
    current_temperature -= 274.04

    current_pressure = y["pressure"]
    current_pressure *= 0.0009869233

    current_humidity = y["humidity"]

    z = data["weather"]
    weather_description = z[0]["description"]

    degree_sign = u"\N{DEGREE SIGN}"

    temperature = "{:.0f}".format(current_temperature) + degree_sign + "C"
    pressure = "{:.0f}".format(current_pressure) + " atm"
    humidity = str(current_humidity) + "%"
    details = weather_description

    return render_template('weather.html', city=city, temperature=temperature, details=details, pressure=pressure, humidity=humidity)

if __name__ == '__main__':
    app.run(debug=True)
