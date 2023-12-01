#!/usr/bin/python3
"""Write a Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    try:
        with urllib.request.urlopen(url) as res:
            html = res.read().decode("utf-8")
            print("Body response:")
            print("\t- type:", type(html))
            print("\t- content:", html)
    except urllib.error.URLError as e:
        print("Error:", e)
