@echo off
py -3 scraping2.py
py -3 convertHTML.py
py -3 formatHTML.py
del index_before.html
del index_before.001.png
py -m http.server 8080 &