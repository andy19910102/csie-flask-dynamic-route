from flask import Flask, render_template
import csv
from stock import Stock

app = Flask(__name__)

# 站內要顯示的個股列表
stocks = []

# 打開stock_list.csv
with open('stock_list.csv', newline='', encoding='utf-8') as stock_csv:
    # 把csv檔案格式轉換為list
    temp = list(csv.reader(stock_csv))


@app.route('/')
# 首頁路由
def index_page():
    return render_template('index.html')


@app.route('/stock/<sid>')
# 個股詳情頁路由
def stock_detail_page(sid):
    return render_template('stock-detail.html')


@app.route('/pm25-list/<page_id>')
# PM25列表頁面
def pm25_list_page(page_id):
    return render_template('pm25-list.html')


if __name__ == '__main__':
    app.run(debug=True)
