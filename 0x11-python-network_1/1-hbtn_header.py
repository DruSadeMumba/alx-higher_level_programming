#!/usr/bin/python3
"""
A python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response
"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            x_id = res.headers.get("X-Request-Id")
            print(f"{x_id}")
    except urllib.error.URLError as e:
        print("Error: ", e)
