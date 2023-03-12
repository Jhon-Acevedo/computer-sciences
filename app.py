from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():  # put application's code here
    return render_template('index.html')


@app.route('/mean-square')
def mean_square():
    return render_template('mean_square.html')


if __name__ == '__main__':
    app.run()
