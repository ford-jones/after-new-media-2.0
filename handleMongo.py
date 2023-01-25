import pymongo 
import certifi

ca = certifi.where()

def db_connect(usr, pw, db, cltn, vid):
  cluster = pymongo.MongoClient("mongodb+srv://"+usr+":"+pw+"@ytcrawler.0jhwpkg.mongodb.net/?retryWrites=true&w=majority", tlsCAFile = ca)
  database = cluster[db]
  collection = database[cltn]

  def db_post():
    return collection.insert_one({"yt_id": vid.id})

  if vid.statistics.viewCount == '0':
    db_post()
    print('video ID ', vid.id, ' posted!')
  else:
    print('nothing posted.')