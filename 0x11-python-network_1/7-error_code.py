#!/usr/bin/python3
"""
A python script that takes in a URL, sends a request
to the URL and displays the body of the response
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        res = requests.get(url)
        print(res.text)
        if res.status_code >= 400:
            print(f"Error code: {res.status_code}")
    except requests.exceptions.RequestException as e:
        print("Error:", e)
