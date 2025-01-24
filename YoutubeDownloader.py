"""
Author: Akpojotor Oghenerurho
Email: akporurho@proton.me
Date: 21/01/25
python script to download youtube videoes
"""
from pytube import YouTube
video_url = "video_url"
yt = YouTube(video_url)
stream = yt.stream.grt_high_resolution()
stream.download()
