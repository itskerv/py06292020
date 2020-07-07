#!/usr/bin/python3

import requests

# define the URL we want to use
NHLURL = "https://statsapi.web.nhl.com/api/v1/teams"

def main():
    # use requests library to send an HTTP GET
    resp = requests.get(NHLURL)

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson = resp.json()

    # display our PYTHONIC data (LIST / DICT)
    print(respjson)

    # JUST display the value of "ip"
    print(f"The current WAN IP is --> {respjson['teams']}")

if __name__ == "__main__":
    main()

