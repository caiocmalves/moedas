import requests

CURRENCY_NAMES = {
    "USD": 'Dólares dos Estados Unidos da América',
    "BRL": 'Real'
}

EXCHANGE_RATE = {
    "USD":{
        "BRL": 5.80,
        "EUR": 0.85,
    },
    "BRL":{
        "USD": 1 / 5.80,
        "EUR": 1 / 6.15
    }
}


def get_exchange_rate(from_code, to_code):
    #return EXCHANGE_RATE[from_code][to_code]
    url = "https://economia.awesomeapi.com.br/last/{}-{}"
    r = requests.get(url.format(from_code,to_code))
    # tratar caso a resposta deste get não retornar 200
    rate = r.json()[f'{from_code}{to_code}']['ask']
    return float(rate)




