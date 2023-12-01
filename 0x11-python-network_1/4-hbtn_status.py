#!/usr/bin/python3
"""Write a Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as res:
        html = res.read().decode("utf-8")
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
