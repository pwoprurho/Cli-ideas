"""
Author: Akpojotor Oghenerurho
Email: akporurho@proton.me
Date: 21/01/25
python script to download youtube videoes
"""
#Youtube downloader
from ytube_api import Auto
query = input("Enter your video url here: ")
Auto(query=query)