from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DataList.db'
db = SQLAlchemy(app)


class TODOLIST(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return '<Task %ds>' % self.id


db.create_all()


@app.route('/', methods=['POST', 'GET'])
def adding():
    global newtask
    if request.method == "POST":

        gettask = request.form['content']
        newtask = TODOLIST(content=gettask)

        if gettask != "":

            try:
                db.session.add(newtask)
                db.session.commit()
                return redirect('/')
            except:
                return render_template('index.html')
        else:
            return "Please enter task first."

    else:
        # tasks = TODOLIST.query.order_by(TODOLIST.id).all()
        return render_template('index.html')


@app.route('/viewtask/', methods=['POST', 'GET'])
def viewtask():
    global tasks

    tasks = TODOLIST.query.order_by(TODOLIST.id).all()
    return render_template('viewtask.html', tasks=tasks)


@app.route("/delete/<int:id>")
def delete(id):
    task_to_delete = TODOLIST.query.get_or_404(id)
    try:

        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect("/viewtask/")
    except:

        return render_template('viewtask.html')


@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    task_to_update = TODOLIST.query.get_or_404(id)

    if request.method == 'POST':

        task_to_update.content = request.form['content']

        try:
            db.session.commit()
            return redirect("/viewtask/")
        except:
            return render_template('viewtask.html')
    else:
        return render_template('update.html', task=task_to_update)


@app.route('/index/', methods=['POST', 'GET'])
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
