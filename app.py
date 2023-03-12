from flask import Flask, render_template

from models.linear_congruence import LinearCongruence
from models.multiplicative_congruence import MultiplicativeCongruence

app = Flask(__name__)


@app.route('/')
def main(): 
    return render_template('index.html')


@app.route('/linear-congruence')
def linear_congruence(): 
    linear = LinearCongruence(1,4,3,7)
    datas = linear.linear_congruence(1,50,10)
    print(datas)
    return render_template('linear_congruence.html')



if __name__ == '__main__':
    app.run(debug=True)
