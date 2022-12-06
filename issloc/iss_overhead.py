#!/usr/bin/python3
"""Alta3 Research | <your name here>
   Using an HTTP GET to determine when the ISS will pass over head"""

# python3 -m pip install requests
import requests

# Import JSON to manipulate JSON to python
import json

URL = 'http://api.open-notify.org/iss-now.json'

def main():
    """your code goes below here"""
    resp = requests.get(URL).json()    
    # stuck? you can always write comments
    # Try describe the steps you would take manually

    jsonstring = json.dumps(resp)

    long = resp["iss_position"]["longitude"]
    lat = resp["iss_position"]["latitude"]
    # print(jsonstring)

    print(f"THE CURRENT LOCATION OF THE ISS: ")
    print(f"Lonitude: {long}")
    print(f"Latitude: {lat}")
if __name__ == "__main__":
    main()

