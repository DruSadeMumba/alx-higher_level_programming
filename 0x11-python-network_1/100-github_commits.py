#!/usr/bin/python3
"""Print 10 GitHub commits"""
import sys
import requests

if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    try:
        res = requests.get(url)
        commits = res.json()[:10]
        try:
            for commit in commits:
                sha = commit.get("sha")
                name = commit.get("commit").get("author").get("name")
                print(f"{sha}: {name}")
        except IndexError:
            pass
    except requests.exceptions.RequestException as e:
        print("Error:", e)
