from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.foreignexchange import ForeignExchange


def get_fin_quotes(ticker_symbol):
    ts = TimeSeries(key="QG9CQILAD7ASQXK0")
    data = ts.get_quote_endpoint(ticker_symbol)
    symbol_search = ts.get_symbol_search(ticker_symbol)
    try:
        return str(symbol_search[0][0]['2. name']) \
               + ": Цена - " + str(data[0]['05. price']) \
               + " Объем - " + str(data[0]['06. volume']) \
               + " Процент изменений с последнего торгового дня - " + str(data[0]['10. change percent'])
    except ValueError:
        print("Неверный тикет")
    finally:
        print("Конец обработки исключения")


def exchange_rate_usd():
    ts = ForeignExchange(key='BK1STKHPQSJVPL20')
    data = ts.get_currency_exchange_rate(from_currency='USD', to_currency='RUB')
    return str(round(float(data[0]['5. Exchange Rate']), 2)) + "р."


def exchange_rate_euro():
    ts = ForeignExchange(key='BK1STKHPQSJVPL20')
    data = ts.get_currency_exchange_rate(from_currency='EUR', to_currency='RUB')
    return str(round(float(data[0]['5. Exchange Rate']), 2)) + "р."
