#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    try:
        with urllib.request.urlopen(url) as res:
            body_cont = res.read()
            utf8_cont = body_cont.decode("utf-8")
            print("Body response:")
            print(f"\t- type: {type(body_cont)}")
            print(f"\t- content: {body_cont}")
            print(f"\t- utf8 content: {utf8_cont}")
    except urllib.error.URLError as e:
        print("Error:", e)
