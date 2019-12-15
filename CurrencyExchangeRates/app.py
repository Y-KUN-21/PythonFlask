from flask import Flask,render_template,jsonify,request
import requests


app=Flask(__name__)


@app.route('/')
def start():
    return render_template("index.html")

@app.route('/xrates/',methods=['POST','GET'])
def index():
    Currency = request.form.get("Currency")
    r=requests.get(url="http://data.fixer.io/api/latest?access_key=370cf3999772c30835f7fc0923a6a2f3",
    params = {"base": "EUR", "symbols":Currency })

    if r.status_code != 200:
        return jsonify({"success": False})
    else:
        return "UNSUCCSESSFUL"

    data =r.json()

    if Currency not in data['rates']:
        return jsonify({"success":True,"rate":data["rates"][Currency]})

    return render_template("index.html")
