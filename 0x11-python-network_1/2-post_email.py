#!/usr/bin/python3
"""
A python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
"""
import sys
import urllib.request
import urllib.parse
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]
    email_data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("utf-8")
    try:
        with urllib.request.urlopen(url, data=email_data) as res:
            body_cont = res.read().decode("utf-8")
            print(f"{body_cont}")
    except urllib.error.URLError as e:
        print("Error: ", e)
