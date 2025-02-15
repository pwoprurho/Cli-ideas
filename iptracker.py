# Ip address information using python.
import os
import urllib.request as urlib2
import json

while True:
    ip = input("Enter target ip address here: ")
    url = "http://ip-api.com/json/"
    response = urlib2.urlopen(url+ip)
    data = response.read()
    values = json.load(data)
    
    print("IP: " +values["query"])
    print("CITY: " + values["city"])
    print("ISP: " + values["isp"])
    print("COUNTRY: " + values["country"])
    print("REGION: " + values["region"])
    print,("TIMEZONE:"+values[["timezone"]])
    break