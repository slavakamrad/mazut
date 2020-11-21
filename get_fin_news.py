import feedparser
import pyshorteners


class Source(object):
    def __init__(self, link):
        self.link = link
        self.news = []
        self.refresh()

    def refresh(self):
        s = pyshorteners.Shortener()
        data = feedparser.parse(self.link)
        self.news = [
            ((i['title']), (i['link'])) for i in data['entries']]

        for i in self.news:
            link = s.tinyurl.short(i[1])

            return f"{i[0]}\nЧитать: {link}"


NewsYandex = Source('https://news.yandex.ru/finances.rss')
RBKNews = Source('http://static.feed.rbc.ru/rbc/logical/footer/news.rss')
InvestingNews = Source('https://ru.investing.com/rss/news.rss')
InvestIdea = Source('https://ru.investing.com/rss/market_overview_investing_ideas.rss')
PicksStocks = Source('https://ru.investing.com/rss/stock_stock_picks.rss')


def post_news():
    return f'{InvestingNews.refresh()}\n{InvestIdea.refresh()}\n{NewsYandex.refresh()}\n{PicksStocks.refresh()}' \
           f'\n{RBKNews.refresh()}'
