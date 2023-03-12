from flask import Flask, render_template, request
from flask_bootstrap5 import Bootstrap

from models.mean_square import mean_square_implementation


app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def main():  # put application's code here
    return render_template('index.html')


@app.route('/mean-square')
def mean_square():
    return render_template('mean_square.html')


@app.route('/setAtributesMeanTest', methods=['POST'])
def mean_square_post():
    data = mean_square_implementation(request.form['seed'], (request.form['minimum']), request.form['maximum'],
                                      request.form['iterations'])
    return render_template('mean_square.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
