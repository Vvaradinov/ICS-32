# Vladislav Varadinov 32979197

import json
import urllib.parse
import urllib.request


MAPQUEST_API = "h65ENCb5Lx7EAdGnC5kFFt4T7wPqLKOP"
MAPQUEST_URL = "http://open.mapquestapi.com/directions/v2/"
API_ELEVATION = "http://open.mapquestapi.com/elevation/v1/"

def make_a_search(destinations: list):
    """
    Takes the city or street destinations and returns
    a str representing the url to the API
    """
    query_parameters = [
        ("key", MAPQUEST_API), ("from", destinations[0])]
    for obj in range(1,len(destinations),1):
        query_parameters.append(("to",destinations[obj]))

    return MAPQUEST_URL + "route?" + urllib.parse.urlencode(query_parameters)


def get_elevation(lat_long: str)-> str:
    """
    Takes the latitude and longtitude in a string format
    and returns the url for the elevation API
    """
    query_parameters = [
        ("key", MAPQUEST_API),("unit","f"),("latLngCollection",(lat_long))

    ]
    return API_ELEVATION + "profile?" + urllib.parse.urlencode(query_parameters)




def convert_to_python_obj(url: str)-> "json":
    """
    Takes the url in str format that we generated and
    returns the json information into a dictionary so
    that we can read it with python
    """
    server_connection = None

    try:
        server_connection = urllib.request.urlopen(url)
        json_format = server_connection.read().decode(encoding = 'utf-8')

        return json.loads(json_format)
    finally:
        if server_connection != None:
            server_connection.close()



