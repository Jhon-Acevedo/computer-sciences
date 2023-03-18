from flask import Flask, render_template, request
from flask_bootstrap5 import Bootstrap

from models.mean_square import mean_square_implementation
from models.linear_congruence import LinearCongruence
from models.multiplicative_congruence import MultiplicativeCongruence
from models.normal_distribution import NormalDistribution
from models.uniform import uniform_distribution as uniform
from models.normal import normal_distribution as normal

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
    linear = LinearCongruence(
        context['x0'], context['k'], context['g'], context['g'])
    datas = linear.linear_congruence(
        context['minimum'], context['maximum'], context['iterations'])
    return render_template('linear_congruence.html', datas=datas)


@app.route('/multiplicative-congruence')
def multiplicative_congruence():
    return render_template('multiplicative_congruence.html')


@app.route('/multiplicative-congruence', methods=["POST"])
def multiplicative_congruence_data():
    context = {
        'x0': int(request.form.get('x0')),
        't': int(request.form.get('t')),
        'g': int(request.form.get('g')),
        'minimum': int(request.form.get('minimum')),
        'maximum': int(request.form.get('maximum')),
        'iterations': int(request.form.get('iterations')),
    }
    multiplicative = MultiplicativeCongruence(
        context['x0'], context['t'], context['g'])
    datas = multiplicative.multiplicative_congruence(
        context['minimum'], context['maximum'], context['iterations'])
    return render_template('multiplicative_congruence.html', datas=datas)


@app.route('/uniform-distribution')
def uniform_distribution():
    return render_template('uniform_distribution.html')


@app.route('/uniform-distribution', methods=["POST"])
def uniform_distribution_data():
    context = {
        'minimum': int(request.form.get('lower_limit')),
        'maximum': int(request.form.get('upper_limit')),
        'iterations': int(request.form.get('iterations')),
    }
    data = uniform(context['minimum'], context['maximum'], context['iterations'])
    return render_template('uniform_distribution.html', data=data)


@app.route('/std-normal-distribution')
def std_normal_distribution():
    return render_template('std_normal_distribution.html')


@app.route('/normal-distribution')
def normal_distribution():
    return render_template('normal_distribution.html')


@app.route('/std-normal-distribution', methods=["POST"])
def std_normal_distribution_post():
    context = {
        'mean': 0.0,
        'std_dev': 1.0,
        'iterations': int(request.form.get('iterations')),
    }
    datas = NormalDistribution(context['mean'], context['std_dev']).sample(context['iterations'])
    return render_template('std_normal_distribution.html', datas=datas)


@app.route('/normal-distribution', methods=["POST"])
def normal_distribution_post():
    data = normal(int(request.form['iterations']), request.form['mean'], (request.form['std']))
    return render_template('normal_distribution.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
