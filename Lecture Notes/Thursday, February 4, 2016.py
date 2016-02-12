# youtube.py
#
# ICS 32 Winter 2016
# Code Example
#
# This program issues a search for YouTube videos, given a particular
# search query like "lakers clippers".

import json
import urllib.parse
import urllib.request


# You'll need to paste a valid Google API key here.  It needs to be one
# that has the YouTube Data API activated.  I've created such an API key
# for this course -- which I'll email out separately -- but you can also
# create your own, if you prefer.
GOOGLE_API_KEY = 'zzzzzzzzzz'

# All of the services provided by the YouTube Data API have URLs that
# begin like this; it's simply a matter of adding the rest of the URL
# and its query parameters to the end of this.
BASE_YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3'



def build_search_url(search_query: str, max_results: int) -> str:
    '''
    This function takes a search query and the maximum number of results
    to display, and builds and returns a URL that can be used to ask the
    YouTube Data API for information about videos matching the search
    request.
    '''

    # Here, we create a list of two-element tuples, which we'll convert to
    # URL query parameters using the urllib.parse.urlencode function.  The
    # reason we do this, rather than building the URL string ourselves, is
    # because there is a fair amount of complexity -- dealing with special
    # characters, etc. -- that will be difficult to get precisely correct,
    # but that urllib.parse.urlencode already knows how to do correctly.
    query_parameters = [
        ('key', GOOGLE_API_KEY), ('part', 'snippet'),
        ('type', 'video'), ('maxResults', str(max_results)),
        ('q', search_query)
    ]

    return BASE_YOUTUBE_URL + '/search?' + urllib.parse.urlencode(query_parameters)



def get_result(url: str) -> 'json':
    '''
    This function takes a URL and returns a Python object representing the
    parsed JSON response.
    '''
    response = None

    try:
        # Here, we open the URL and read the response, just as we did before.
        # After the second line, json_text will contain the text of the
        # response, which should be in JSON format.
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')

        # Given the JSON text, we can use the json.loads() function to convert
        # it to a Python object instead.
        return json.loads(json_text)

    finally:
        # We'd better not forget to close the response when we're done,
        # assuming that we successfully opened it.
        if response != None:
            response.close()



def print_title_and_description(json_result: 'json') -> None:
    '''
    This function takes a parsed JSON response from the YouTube Data API's
    search request and prints the titles and descriptions of all of the
    videos in the response.
    '''
    for item in json_result['items']:
        print(item['snippet']['title'])
        print(item['snippet']['description'])
        print()



if __name__ == '__main__':
    search_query = input('Query: ')
    result = get_result(build_search_url(search_query, 10))
    print_title_and_description(result)