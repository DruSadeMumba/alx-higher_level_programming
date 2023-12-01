#!/usr/bin/python3
"""A python script that fetches https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = requests.get(url).text
    print("Body response:")
    print("\t- type:", type(req))
    print("\t- content:", req)
