#!/usr/bin/python3
"""
A python script that takes your GitHub credentials
and uses the GitHub API to display your id
"""
import requests
import sys
from requests.auth import *

if __name__ == "__main__":
    url = "https://api.github.com/user"
    autho = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    try:
        res = requests.get(url, auth=autho)
        print(res.json().get("id"))
    except requests.exceptions.RequestException as e:
        print("Error:", e)
