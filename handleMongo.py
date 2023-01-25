import pymongo 
import certifi

ca = certifi.where()

def db_connect(pw, vid):
  
  cluster = pymongo.MongoClient("mongodb+srv://zeroViews:"+pw+"@ytcrawler.0jhwpkg.mongodb.net/?retryWrites=true&w=majority", tlsCAFile = ca)
  db = cluster['python_crawler']
  collection = db['unwatched_id']

  def dbPost():
    return collection.insert_one({"yt_id": vid.id})

  if vid.statistics.viewCount == '0':
    dbPost()
    print('video ID ', vid.id, ' posted!')
  else:
    print('nothing posted.')
  