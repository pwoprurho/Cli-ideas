"""
Aurthor: Akpojotor Oghenerurho
Email: akporurho@proton.me
Date: 20/01/25
python code for loading trending searches in the command line interface(cli)
"""

from pytrends.request import TrendReq
pytrend = Trendreq()
region = input("Enter your country name: ")
results = pytrend.trending_searches(pn=region)
print(results)
