from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("iron.html")


metals=["Iron is a chemical element with symbol Fe and atomic number 26." \
       "It is a metal that belongs to the first transition series and " \
       "group 8 of the periodic table.",
       "Copper is a chemical element with the symbol Cu and atomic number 29." \
       " It is a soft, malleable, and ductile metal with very high thermal and electrical conductivity.",
        "Gold is a chemical element with the symbol Au and atomic number 79, " \
        "making it one of the highest atomic number elements that occur naturally."]


@app.route('/iron')
def iron():
    return metals[0]

@app.route('/copper')
def copper():
    return metals[1]

@app.route('/gold')
def gold():
    return metals[2]

if __name__ == "__main__":
    app.run(debug=True)
