
# coding: utf-8

# In[ ]:


# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser


# In[ ]:


# URL of page to scrape
url = 'https://mars.nasa.gov/news/'
executable_path = {"executable_path": "./chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)


# In[ ]:


# Visit the NASA news URL
browser.visit(url)


# In[ ]:


# Scrape page using beautiful soup
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[ ]:


# See details in html 
#print (soup.prettify())


# In[ ]:


print(soup.prettify())


# In[ ]:


# Find the latest news, including title, paragraph and date
latest_news = soup.find("div", class_="list_text")
#print (latest_news)
latest_news_date = latest_news.find("div", class_="list_date").text
latest_news_title = latest_news.find("div", class_="content_title").text
latest_news_paragraph = latest_news.find("div", class_="article_teaser_body").text

print ("=======================")
print ("[The latest news]")
print (f"Title: {latest_news_title}")
print (f"Date: {latest_news_date}")
print (f"Article: {latest_news_paragraph}")
print ("=======================")


# In[ ]:


browser = Browser('chrome', headless=False)
news_url = 'https://mars.nasa.gov/news/'
browser.visit(news_url)
time.sleep(1)


# In[ ]:


html = browser.html
news_soup= BeautifulSoup(html, 'html.parser')


# In[ ]:


result = news_soup.find('div', class_='content_title')
news_title= result.next_element.get_text()
result1=news_soup.find('div', class_='article_teaser_body')
news_p = result1.get_text()

print(news_title)
print(news_p)


# In[1]:


JPL Mars Image


# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
from splinter import Browser
from bs4 import BeautifulSoup


# In[ ]:


browser = Browser('chrome', headless=False)
image_url  = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(image_url )
time.sleep(1)


# In[ ]:


html = browser.html
image_soup = BeautifulSoup(html, 'html.parser')


# In[ ]:


image = image_soup .find('div', class_='carousel_items')

image_url = image.article['style']

url = image_url.split('/s')[-1].split('.')[0]

featured_image_url= 'https://www.jpl.nasa.gov' +'/s'+ url + '.jpg'

print(featured_image_url )


# In[ ]:


MARS WEATHER


# In[ ]:


browser = Browser('chrome', headless=False)
weather_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(weather_url)
time.sleep(1)


# In[ ]:


html = browser.html
weather_soup = BeautifulSoup(html, 'html.parser')


# In[ ]:


weather = weather_soup.find('div', class_='js-tweet-text-container')

mars_weather= weather.p.text.lstrip()
print(mars_weather)


# In[ ]:


MARS FACTS


# In[ ]:


import pandas as pd
url4 = "https://space-facts.com/mars"
table_html = pd.read_html(url4)[0]
table_html.columns = ['Object','Mars']
table_html


# In[ ]:


html_table = df.to_html()
html_table


# In[ ]:


df.to_html('table.html')


# In[ ]:


mars_facts=df.to_dict('records')
mars_facts


# In[ ]:


facts_url = 'http://space-facts.com/mars/'


# In[ ]:


tables = pd.read_html(facts_url)
tables


# In[ ]:


MARS HEMISPHERES


# In[ ]:


# executable_path = {"executable_path": "./chromedriver"}
# browser = Browser("chrome", **executable_path, headless=False)
url5 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url5)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[ ]:


MarsHemis = []
Hemis = soup.findAll("div", class_="item")
for hemi in Hemis:
    downloadpage = hemi.find("a")["href"]
    browser.visit("https://astrogeology.usgs.gov"+downloadpage)
    html = browser.html
    soup2 = BeautifulSoup(html,'html.parser')
    image = soup2.find("div", class_="downloads")
    image_full = image.find("a")["href"]
    MarsHemis.append({'title': hemi.find("h3").text,
                      'img_url':image_full})
MarsHemis

