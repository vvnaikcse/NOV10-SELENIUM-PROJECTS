import pytest
import requests
global j
def test1():
    resp=requests.get("https://api.github.com/users/weigo")
    j=resp.json()
    print(j)
    print(j["name"])
    assert j["name"]=="Dirk Weigenand"
def test2():
    resp = requests.get("https://api.github.com/users/weigo")
    j = resp.json()
    print(j["location"])
    assert j["location"]=="Germany", "location mismatched"

