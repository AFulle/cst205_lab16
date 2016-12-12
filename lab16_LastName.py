# CST 205 Lab 16: URLS and HTMLS
# Yulian
# Lyndsay
# Ahdia

import urllib
import re
import os

# warm up
def makePage():
  #replace the directory in the line below with the path to your file
  file = open("C:\\Users\\sag12\\Desktop\\Python\\webFile.html", "wt")
  file.write("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 
  Transition//EN" "http://www.w3.org/TR/html4/loose.dtd">
  
  <html>
  <head><title>I made this page with Python!</title>
  </head>
  <body>
  <h1>MY PYTHON PAGE!!!</h1>
  </body>
  </html>""")
  
  file.close()
  
  # code here for scraping text of frequently used webpage
def parse_arstechnica_homepage():
  verge_homepage = urllib.urlopen('https://arstechnica.com').read()
  matches = re.findall(r'<header>\n *<h2><a href=\"(.*)\">(.*)<\/a><\/h2>', verge_homepage)
  author_matches = re.findall(r'<span (?:class=\"author\")? ?itemprop=\"name\">(.*)<\/span>', verge_homepage)
  date_matches = re.findall(r'<time class="date" .*>(.*)<\/time>', verge_homepage)
  
  #code here for creating a new web page that only displays information collected
  header = """
    <html>
    <head><title>The Verge Headlines</title></head>
    <body>
      <table>
        <h2>Ars Technica Latest News</h2>
        <table><tr><th>Date</th><th>Title</th><th>Author</th></tr>
        """
  news = ''
  for news_item in zip(matches, author_matches, date_matches):
    row = '<tr><td>' + news_item[2] + '</td><td><a href="'+ news_item[0][0] + '">' + news_item[0][1] + '</a></td><td>' + news_item[1] + '</td></tr>\n        '
    news = news + row
  
  footer = """
      </table>
     </body>
   </html>"""
   
  file = open(os.path.dirname(os.path.realpath(__file__)) + '/ars.html', 'wt')
  file.write(header+news+footer)
  file.close()
  
  
parse_arstechnica_homepage()