#!/usr/bin/python3
"""
A python script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        x_id = requests.get(url).headers.get("X-Request-Id")
        print(x_id)
    except requests.RequestException as e:
        print("Error:", e)
