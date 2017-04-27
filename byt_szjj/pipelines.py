#!usr/bin/python
# -*- coding: utf-8 -*-

from items import BytSzjjItem
import sqlite3


class BytSzjjPipeline(object):
    def process_item(self, item, spider):
        if item.__class__ == BytSzjjItem:  # 此句非必要，在多个items时可能需要用到
            # 数据库名即目录存放地址
            conn = sqlite3.connect('C:/Program Files/DB Browser for SQLite/database/database.db')
            cur = conn.cursor()
            # 表名是 byt_szjj
            sql = "insert into byt_szjj(title,publish,link,text) values (?,?,?,?)"
            cur.execute(sql, (item['title'], item['publish'], item['link'], item['text'],))
            conn.commit()
            cur.close()
            conn.close()
        return item
