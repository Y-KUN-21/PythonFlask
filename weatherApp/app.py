from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def search():
    return render_template('index.html')

@app.route('/get_weather/')
def get_weather():
    url= 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=78c2cd272dcb82ff19017de3db518bdf'
    City='Mumbai'
    r=requests.get(url.format(City)).json()
    return (r)


if __name__ == "__main__":
    app.run(debug=True)
