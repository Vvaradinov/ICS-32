# Vladislav Varadinov 32979197

import json
import urllib.parse
import urllib.request
import mapquest_ui

MAPQUEST_API = "h65ENCb5Lx7EAdGnC5kFFt4T7wPqLKOP"

MAPQUEST_URL = "http://open.mapquestapi.com/directions/v2/"

def make_a_search(destinations: list): # it works with hard coded locations
    """
    """
    query_parameters = [
        ("key", MAPQUEST_API), ("from", destinations)]
    for obj in range(1, len(destinations)-1,1):
        query_parameters.append(("to",destinations[obj]))

    return MAPQUEST_URL + "route?" + urllib.parse.urlencode(query_parameters)


def convert_to_python_obj(url: str)-> "json": # it works
    """
    """
    server_connection = None

    try:
        server_connection = urllib.request.urlopen(url)
        json_format = server_connection.read().decode(encoding = 'utf-8')

        return json.loads(json_format)
    finally:
        if server_connection != None:
            server_connection.close()


