#import splinter and bs4
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

#executable path set up
executable_path={'executable_path':ChromeDriverManager().install()}
browser=Browser('chrome',**executable_path,headless=False)

#assign url and instruct the browser
# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
#optional delay for loading the page
browser.is_element_not_present_by_css('div.list_text',wait_time=1)

#set up html parser
html=browser.html
news_soup=soup(html,'html.parser')
side_elem=news_soup.select_one('div.list_text')

side_elem.find('div',class_='content_title')

#use the parent element to find the first 'a' tag and save it as 'news_title'
news_title=side_elem.find('div',class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = side_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images
#visit URL
url='https://spaceimages-mars.com'
browser.visit(url)

#find the click the full image button
full_image_elem=browser.find_by_tag('button')[1]
full_image_elem.click()

#parse the resulting html with soup
html=browser.html
img_soup=soup(html,'html.parser')

#find the relative image url
img_url_rel=img_soup.find('img',class_='fancybox-image').get('src')
img_url_rel

#use the base url to create an absolute url
img_url=f'https://spaceimages-mars.com/{img_url_rel}'
img_url

#scrape entire table by using pandas .read_html() function
df=pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description','Mars','Earth']
df.set_index('description',inplace=True)
df

#convert df into html via pandas to_html() function
df.to_html()

#end the session
browser.quit()





