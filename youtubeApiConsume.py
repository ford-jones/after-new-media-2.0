from pyyoutube import Api
from randomDateTime import get_dates
from randomLatlon import get_latlon
from randomWord import get_word
from handleMongo import db_connect
import os 

def getVideoId(video):
    return video.id.videoId 

def fetch():
    api = Api(api_key=os.environ.get('API_KEY'))
    dates = get_dates()
    latlon = get_latlon()
    word = get_word()

    r = api.search(
      location=format(latlon[0]) + ',' + format(latlon[1]), 
      location_radius="500mi",
      q=word,
      count=50,
      parts=["snippet"],
      search_type="video",
      order="viewCount",
      published_after=format(dates[0]) + 'Z',
     published_before=format(dates[1]) + 'Z',
    )
    videoIdList = list(map(getVideoId, r.items))
    length  = len(videoIdList)
    print('num of results: ', length)
    if length > 0:
      video = api.get_video_by_id(video_id=videoIdList[length - 1])
      print('last index ID: ', video.items[0])
      print('view count: ', video.items[0].statistics.viewCount)
    else:
      print('no results')

fetch()
db_connect(pw = os.environ.get('MONGODB_PW'))