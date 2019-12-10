from flask import Flask, render_template
from flask import request
import requests

app = Flask(__name__)


@app.route('/')
def search():
    return render_template('index.html')
@app.route('/', methods=['POST', 'GET'])
def get_weather():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=78c2cd272dcb82ff19017de3db518bdf'
    City=request.form['enter_city']
    r = requests.get(url.format(City)).json()
    weather={
        'City':r['name'],
        "temperature":r['main']['temp'],
        "description":r['weather'][0]['description'],
        "icon":r['weather'][0]['icon'],
        "Country":r['sys']['country']
    }
    return render_template('weather.html',weather=weather)
if __name__ == "__main__":
    app.run(debug=True)
