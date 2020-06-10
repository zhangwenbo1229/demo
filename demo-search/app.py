import math
import json
import pymysql
from flask import *
from flask_sqlalchemy import SQLAlchemy

import config
app = Flask(__name__)
app.config.from_object(__name__)


def db_execute(keyword):
    conn = pymysql.connect('localhost',
                           'zwb',
                           '123456',
                           'bqb',
                           cursorclass=pymysql.cursors.DictCursor)

    query = 'select image_url,image_des from bqb_scrapy where image_des like "%{}%" limit 2;'.format(
        keyword)
    cur = conn.cursor()
    cur.execute(query)
    res = cur.fetchall()
    cur.close()
    conn.close()
    return res


def get_page(total, p):
    show_page  = 5  # 显示的页码数
    pageoffset = 2  # 偏移量
    start      = 1  # 分页条开始
    end        = total  # 分页条结束

    if total > show_page:
        if p > pageoffset:
            start = p - pageoffset
            if total > p + pageoffset:
                end = p + pageoffset
            else:
                end = total
        else:
            start = 1
            if total > show_page:
                end = show_page
            else:
                end = total
        if p + pageoffset > total:
            start = start - (p + pageoffset - end)
    # 用于模版中循环
    dic = range(start, end + 1)
    return dic


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gets/', methods=['POST', 'GET'])
def search():
    global db
    #conn = pymysql.connect('localhost','zwb','123456','bqb',cursorclass=pymysql.cursors.DictCursor)
    # datas = db_execute(s)


    page = int(request.args.get('page', 1))
    show_shouye_status = 0
    limit_start = (int(page) - 1) * 10  # 起始
    db = config.SQLManager()
    word = str(request.args.get('word', "我"))
    s = str(request.values.get('question',"我"))

    if page > 1:
        show_shouye_status = 1
    if page > 1:
        data = db.get_list('select image_url,image_des from bqb_scrapy where image_des like "%{}%" limit {},2'.format(word,limit_start))
    else:
        data = db.get_list('select image_url,image_des from bqb_scrapy where image_des like "%{}%" limit {},2'.format(s,limit_start))
    # sql   = 'select image_url,image_des from bqb_scrapy where image_des like "%{}%" limit {},2;'.format(s,limit_start)
    if page > 1:
        sql = " select count(image_des) as total from bqb_scrapy where image_des like '%" + word + "%'"
    else:
        sql = " select count(image_des) as total from bqb_scrapy where image_des like '%" + s + "%'"
    count = db.get_one(sql)['total']  # 总记录
    total = int(math.ceil(count / 10.0))  # 总页数
    dic = get_page(total, page)
    page = int(page)
    db.close()

    return render_template('search.html', data=data, count=count,show_shouye_status=show_shouye_status, total=total, dic_list=dic, page=page,s = s,word=word)



if __name__ == '__main__':
    app.run()
