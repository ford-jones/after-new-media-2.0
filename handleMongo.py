import pymongo 
import certifi

ca = certifi.where()

def db_connect(usr, pw, db, cltn, vid):
  cluster = pymongo.MongoClient("mongodb+srv://"+usr+":"+pw+"@ytcrawler.0jhwpkg.mongodb.net/?retryWrites=true&w=majority", tlsCAFile = ca)
  database = cluster[db]
  collection = database[cltn]

  def dbPost():
    return collection.insert_one({"yt_id": vid.id})

  if vid.statistics.viewCount == '0':
    dbPost()
    print('video ID ', vid.id, ' posted!')
  else:
    print('nothing posted.')