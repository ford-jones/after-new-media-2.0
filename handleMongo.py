import pymongo
import os

pw = os.environ.get('MONGODB_PW')

def db_connect():
  client = pymongo.MongoClient("mongodb+srv://zeroViews:{pw}@ytcrawler.0jhwpkg.mongodb.net/?retryWrites=true&w=majority")

  db = client.python_crawler
  collection = db.unwatched_id

  print('collection: ', collection)
  