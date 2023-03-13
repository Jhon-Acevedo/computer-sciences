from flask import Flask, render_template, request
from flask_bootstrap5 import Bootstrap

from models.mean_square import mean_square_implementation
from models.linear_congruence import LinearCongruence
from models.multiplicative_congruence import MultiplicativeCongruence

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/mean-square')
def mean_square():
    return render_template('mean_square.html')


@app.route('/setAtributesMeanTest', methods=['POST'])
def mean_square_post():
    data = mean_square_implementation(request.form['seed'], (request.form['minimum']), request.form['maximum'],
                                      request.form['iterations'])
    return render_template('mean_square.html', data=data)


@app.route('/linear-congruence')
def linear_congruence():
    return render_template('linear_congruence.html')


@app.route('/linear-congruence', methods=["POST"])
def linear_congruence_data():
    context = {
        'x0': int(request.form.get('x0')),
        'k': int(request.form.get('k')),
        'c': int(request.form.get('c')),
        'g': int(request.form.get('g')),
        'minimum': int(request.form.get('minimum')),
        'maximum': int(request.form.get('maximum')),
        'iterations': int(request.form.get('iterations')),
    }
    linear = LinearCongruence(context['x0'], context['k'], context['g'], context['g'])
    datas = linear.linear_congruence(context['minimum'], context['maximum'], context['iterations'])
    return render_template('linear_congruence.html', datas=datas)


if __name__ == '__main__':
    app.run(debug=True)
