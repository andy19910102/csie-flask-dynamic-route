from urllib.request import urlopen


class Stock:
    # 個股包含以下屬性
    # 個股代號、名稱、成交價、買價、賣價
    def __init__(self, sid, name):
        self.id = sid
        self.name = None
        self.price = None
        self.bid = None
        self.offer = None

    # 定義爬取個股資訊的函式
    def get_data(self):
        # 爬取整個目標網頁
        page = urlopen('https://tw.stock.yahoo.com/q/q?s=' + self.id)
        # 使用big5解碼
        raw_html = page.read().decode('big5')
        # 使用PyQuery解析網站取得特定資訊
