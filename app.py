from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

API_KEY = '86d4ab9239a7e51aa9d81b64'
BASE_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/'

def get_rates(base):
    url = BASE_URL + base
    res = requests.get(url)
    data = res.json()
    if data['result'] == 'success':
        return data['conversion_rates']
    return None

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/converter', methods=['GET', 'POST'])
def converter():
    result = None
    rate = None
    currencies = []
    amount = 0
    from_currency = 'USD'
    to_currency = 'EUR'

    if request.method == 'POST':
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        amount = float(request.form['amount'])

        rates = get_rates(from_currency)
        if rates and to_currency in rates:
            rate = rates[to_currency]
            result = round(amount * rate, 2)
        currencies = list(rates.keys()) if rates else []
    else:
        rates = get_rates('USD')
        currencies = list(rates.keys()) if rates else []

    return render_template(
        'converter.html',
        result=result,
        currencies=currencies,
        from_currency=from_currency,
        to_currency=to_currency,
        amount=amount,
        rate=rate
    )

if __name__ == '__main__':
    app.run(debug=True)
