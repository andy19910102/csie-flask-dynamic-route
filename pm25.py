import requests


class PM25:
    def __init__(self, d):
        self.name = d['SiteName']
        self.date = d['MonitorDate']
        self.amount = d['Concentration']
        self.unit = d['ItemUnit']


class PM25Collection:
    def __init__(self):
        self.data = []
        self.fetch_data()

    def fetch_data(self):
        # 取得 PM2.5 環保署公開資料
        # https://opendata.epa.gov.tw/api/index.html
        # API網址
        # https://opendata.epa.gov.tw/api/v1/PM25?%24skip=0&%24top=1000&%24format=json
        url = 'https://opendata.epa.gov.tw/api/v1/PM25?%24skip=0&%24top=1000&%24format=json'
        res = requests.get(url)
        json = res.json()
        for d in json:
            data = PM25(d)
            self.data.append(data)
