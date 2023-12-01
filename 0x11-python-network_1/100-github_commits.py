#!/usr/bin/python3
"""Print 10 GitHub commits"""
import sys
import requests

if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}"
    try:
        res = requests.get(url)
        commits = res.json()
        for commit in range(10):
            sha = commits[commit].get("sha")
            name = commits[commit].get("commit").get("author").get("name")
            print(f"{sha}: {name}")
    except requests.exceptions.RequestException as e:
        print("Error:", e)
