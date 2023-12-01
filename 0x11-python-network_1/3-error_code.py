#!/usr/bin/python3
"""
A python script that takes in a URL, sends a request
to the URL and displays the body of the response
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            body_cont = res.read().decode("utf-8")
            print(f"{body_cont}")
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
    except urllib.error.URLError as e:
        print("Error: ", e)
