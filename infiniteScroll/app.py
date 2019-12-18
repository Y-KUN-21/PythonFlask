from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/contentpage", methods=['POST'])
def load():

    start = int(request.form.get("start") or 0)
    end = int(request.form.get("end") or (start + 9))

    data = []
    for i in range(start, end+1):
        data.append(f"Line #{i}")

    time.sleep(1)

    # Return list of posts.
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
