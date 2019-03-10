from flask import *
from io import BytesIO, StringIO
import base64
from numpy import *
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)
x_min = '-6'
x_max = '6'
delta_x = '0.1'
equation = 'x'

@app.route('/')
def index():
    return render_template('index.html', equation=equation, x_min=x_min, x_max=x_max, delta_x=delta_x);

@app.route('/plot', methods=['POST'])
def plot():
    plt.clf()
    figure = BytesIO() #File like object to save png
    equation = request.form['equation']
    x_min = float(request.form['x_min'])
    x_max = float(request.form['x_max'])
    delta_x = float(request.form['delta_x'])

    print("Equation:", equation)
    X = np.arange(x_min, x_max, delta_x)
    Y = [eval(equation) for x in X]    
    plt.plot(X, Y)
    plt.ylabel(equation)
    plt.xlabel('x')
    plt.savefig(figure, format='png')
    figure.seek(0)
    # Encode data with base64 so it can be served
    figure = base64.standard_b64encode(figure.read()).decode()

    return render_template('index.html', figure=figure, equation=equation, x_min=x_min, x_max=x_max, delta_x=delta_x)


app.run(host='127.0.0.1', port='80',debug=True)
