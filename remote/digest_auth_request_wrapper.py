# This file wrap the request to the Egauge server
import requests
from requests.auth import HTTPDigestAuth
from resources import constants


# This functions login using digest auth

def login(url):
    # Try to connect
    try:
        response = make_request(url)
        if response.status_code == 200:
            return response.content
        # For Debuging purposes
        # elif response.status_code == 404:
        #     print(url)
        #     # pass
        elif response.status_code == 401:
            print(url)
            # pass
    # if an error pass
    except requests.exceptions.ConnectionError:
        pass
    return None


def make_request(url):
    # Make a request.
    response = requests.get(url, timeout=50, auth=HTTPDigestAuth(constants.USER, constants.PASSWORD), stream=True,
                            headers={
                                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                              "Chrome/51.0.2704.103 Safari/537.36"})
    return response
