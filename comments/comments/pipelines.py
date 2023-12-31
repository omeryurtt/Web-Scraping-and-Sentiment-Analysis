# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import mysql.connector


class CommentsPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host= "localhost",
            user= "root",
            passwd= "your_passwd",
            database= "amazon-review"
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute(""" DROP TABLE IF EXISTS protein_powder_reviews""")
        self.curr.execute("""CREATE TABLE protein_powder_reviews(
                        asin text,
                        user_name text,
                        review_star text,
                        review_title text,
                        text text,
                        date_and_country text,
                        product_name text)""")
                        
    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
                self.curr.execute("""INSERT INTO protein_powder_reviews(asin, user_name, review_star, review_title, text, date_and_country, product_name)
                                  VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                                  (item["asin"],
                                      item["user_name"],
                                   item["review_star"],
                                   item["review_title"],
                                   item["text"],
                                   item["date_and_country"],
                                   item["product_name"]))
                self.conn.commit()


