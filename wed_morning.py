#!/usr/bin/ python3
'''
Write a Python script that accepts an IPv4 address from the user, and returns where that IP address is in the world along with any other
    info you'd like
    Optional Challenge 01 - Supply a list of IPs via an external file. Have your program look up each one, and write into the file where that IP address is located.
                          - alternative (or also) try passing command line arguments
    Optional Challenge 02 - Map the location on a map of the world :p Write the new image out as a stand-alone file (for example, as a .png or .jpg). Alternatively, you can write the program so it runs on a machine with a GUI (say, your local machine).
'''

import requests
import argparse


def main():

    if args.ip:
        ipToLookup = args.ip
    else:
        ipToLookup = input("What is the IP addess to lookup?  ")

    zresp = requests.get(f'http://ip-api.com/json/{ipToLookup }')
    print(zresp.json())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", help="The IP address to look up via the API service" )

    args = parser.parse_args()
    main()

#parser = argparse.ArgumentParser()
#parser.add_argument("square", help="display a square of a given number", type=int)


















'''
import urllib
import json
import requests

url = 'http://api.hostip.info/get_json.php'
info = json.loads(urllib.urlopen(url).read())
ip = info['ip']

urlLocation = "http://www.freegeoip.net/json/{0}".format(ip)
locationInfo = json.loads(urllib.urlopen(urlLocation).read())
print ('Country: ' + locationInfo['country_name'])
print ('City: ' + locationInfo['city'])
print ('')
print ('Latitude: ' + str(locationInfo['latitude']))
print ('Longitude: ' + str(locationInfo['longitude']))
print ('IP: ' + str(locationInfo['ip']))
'''




