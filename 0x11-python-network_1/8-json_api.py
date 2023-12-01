#!/usr/bin/python3
"""
A python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    try:
        res = requests.post(url, data={"q": letter})
        try:
            result = res.json()
            if result:
                print(f"[{result.get('id')}] {result.get('name')}")
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    except requests.exceptions.RequestException as e:
        print("Error:", e)
