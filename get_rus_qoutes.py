import investpy
import datetime
from datetime import timedelta


def get_ru_quotes(tiker):
    now = datetime.date.today().strftime('%d/%m/%Y')
    yesterday = (datetime.date.today() - timedelta(days=1)).strftime('%d/%m/%Y')

    df = investpy.get_stock_historical_data(stock=tiker,
                                            country='Russia',
                                            from_date=yesterday,
                                            to_date=now)
    return f'{df}'


def stock_except():
    return 'нет такого тикета'


