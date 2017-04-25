#!usr/bin/python
# -*- coding: utf-8 -*-

from items import BytSzjjItem
import sqlite3


class BytSzjjPipeline(object):
    def process_item(self, item, spider):
        if item.__class__ == BytSzjjItem:  # 此句非必要，在多个items时可能需要用到
            # conn = sqlite3.connect('C:/Program Files/DB Browser for SQLite/database/rmrb.db')
            conn = sqlite3.connect('C:/Program Files/DB Browser for SQLite/database/byt.db')
            cur = conn.cursor()
            sql = "insert into szjj(title,publish,link,text) values (?,?,?,?)"
            cur.execute(sql, (item['title'], item['publish'], item['link'], item['text'],))
            conn.commit()
            cur.close()
            conn.close()
        return item
