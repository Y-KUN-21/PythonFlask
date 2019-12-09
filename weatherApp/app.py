from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def search():
    return render_template('index.html')

@app.route('/get_weather/')
def get_weather():
    return "yes"


if __name__ == "__main__":
    app.run(debug=True)
