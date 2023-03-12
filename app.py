from flask import Flask, render_template
from flask_bootstrap5 import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def main():  # put application's code here
    return render_template('index.html')


@app.route('/mean-square')
def mean_square():
    return render_template('mean_square.html')


if __name__ == '__main__':
    app.run(debug=True)
