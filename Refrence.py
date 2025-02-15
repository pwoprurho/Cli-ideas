"""
Author: Akpojotor Oghenerurho
Email: akporurho@proton.me
Date:18/01/25
python script to scrawl the internet for links related to a keyword
"""
from googlesearch import search
query = input("What do you want to search for")
for url in search(query):
  print(url)
