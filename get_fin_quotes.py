from alpha_vantage.timeseries import TimeSeries


def get_fin_quotes(ticker_symbol):
    ts = TimeSeries(key="QG9CQILAD7ASQXK0")
    data = ts.get_intraday(ticker_symbol, interval='1min')
    return str(data[0][max(data[0].keys())])


# QG9CQILAD7ASQXK0


