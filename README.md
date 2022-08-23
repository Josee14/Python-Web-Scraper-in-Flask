# Python-Web-Scraper-in-Flask

 ### <u> What is a web scraper? </u>
 Websites currently contain a wealth of valuable information.When gathering this information, you will almost definitely find yourself manually copying and pasting.You need a simple and more automated method for this, which is where web scraping comes in.

 Web scraping is simply the automated extraction of a web page's unstructured HTML information in a specified format, structuring it, and storing it in a database or saving it as a CSV file for future consumption.

### How to scrape the web?
1. Find the URLs you want to scrape
2. Inspect the page
3. Identify the data you want to extract- find appropriate nest tags

### What tools can you use to scrape the web?
1. Beautiful Soup
2. Scrapy
3. Pandas
4. Parsehub

### In this tutorial, we'll look at web scraping using Beautiful Soup and Requests. We'll build a web scrapper app with Flask, Python's most lightweight web framework.
How it works
1. Load the application
2. Provide a target URL and a tag to be fetched example img,p, title
3. Receive a response - the requested element(s) content.
4. For images, there will be a download functionality that will save the images to your downloads directory


### app.py
We will utilize Flask, Beautiful Soup, and request libraries. First and foremost, we'll import some functionality from Flask and Beautiful Soup into the app.py file.

### We need to validate and parse the URLs we get, so we import the URL handling module for Python- urllib, as well as some other built-in libraries.

    from flask import (
    Flask,
    render_template,
    request,
    redirect,
    flash,
    url_for
    )
    import urllib.request 
    from urllib.parse import urlparse,urljoin
    from bs4 import BeautifulSoup
    import requests,validators,uuid,pathlib,os

### Next, for our first route, we'll construct a function that returns an HTML template, as seen below.
     @app.route("/",methods=("GET", "POST"), strict_slashes=False)
     def index():
     # parsing

     return render_template("index.html")

### To begin our scrap, we must ensure that the user has sent a Post request.
     if request.method == "POST":

### Parsing
check code line 39-...

### Downloading images

    
