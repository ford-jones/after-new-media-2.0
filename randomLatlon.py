import requests
import json
import random

def get_offset():
    url = 'http://geodb-free-service.wirefreethought.com/v1/geo/cities?hateoasMode=off'
    response = requests.request('GET', url)
    data = json.loads(response.text)
    countryCount = data['metadata']['totalCount']
    randCountryId = random.randint(0, countryCount - 1)
    return randCountryId
    
def get_city_object(countryId):    
    newUrl = "http://geodb-free-service.wirefreethought.com/v1/geo/cities?limit=1&offset={}&hateoasMode=off".format(countryId)
    randCountryResponse = requests.request('GET', newUrl)
    country = json.loads(randCountryResponse.text)
    return country['data'][0]

def get_latlon():
    countryId = get_offset()
    countryObject = get_city_object(countryId)
    return [countryObject['latitude'], countryObject['longitude']]
    