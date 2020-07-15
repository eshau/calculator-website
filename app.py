# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import model

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/eval', methods=['GET','POST'])
def evaluation():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        form = request.form
        output = model.eval(form["string"])
        return render_template('index.html', data=output)


