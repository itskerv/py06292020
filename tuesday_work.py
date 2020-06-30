#!/usr/bin/env python3

import requests

#issloc = {"message": "success", "timestamp": 1593527876, "iss_position": {"longitude": "27.7782", "latitude": "-48.7014"}}

#print(issloc["message"])
#print(issloc["timestamp"])
#print(issloc["iss_position"])



def main():
    print("The ISS location: ")
    
    res = requests.get("http://api.open-notify.org/iss-now.json")
    
    isspos = res.json()

   # print(isspos)
    
    print(isspos['timestamp'])
    print(isspos['iss_position'])

if __name__ == "__main__":
    main()

