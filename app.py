from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        from_currency = request.form['from']
        to_currency = request.form['to']
        amount = float(request.form['amount'])
        url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
        response = requests.get(url)
        data = response.json()
        result = round(data['result'], 2)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
