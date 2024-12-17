from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pprint  # To tidy up


#Using Selenium to navigate to the website
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
options.add_argument('--start-maximized')


driver = webdriver.Chrome(options=options)  # It will open the browser in incognito mode

# url = "https://www.rottentomatoes.com/browse/movies_at_home/critics:certified_fresh"
# driver.get(url)

# soup = BeautifulSoup(driver.page_source, 'html.parser')
# movies = soup.find_all(attrs={"data-qa": "discovery-media-list-item"})

# for movie in movies:
#     title = [item.get_text() for item in soup.find_all(class_= 'p--small')]
#     score = [item.get_text() for item in soup.find_all(slot= 'criticsScore')]
#     release_date = [item.get_text() for item in soup.find_all(class_= 'smaller')]

#     print(f"Title: {title}")
#     print(f"Score: {score}")
#     print(f"Release Date: {release_date}")
#     print("-------------")
# driver.quit()

# Exercise 4: Scrape and Cateogrize News Articles From A JavaScript-Enabled News Site
# Extract news article titles and publication dates.
# Categorize the articles by their publication monhts.

url1 = 'https://www.bbc.com/innovation/technology'

driver.get(url1)
soup = BeautifulSoup(driver.page_source, 'html.parser')

# wait = WebDriverWait(driver, 10)
# articles = soup.find_all(attrs={"data-testid": "card-headline"})
# print(articles)

# articles_list =[]
# dates_list = []
# for article in articles:
#     title = article.find(attrs={"data-testid": "card-headline"})
#     date = article.find(attrs={"data-testid": "card-metadata-lastupdated"})
#     articles_list.append(title)
#     dates_list.append(date)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# options = Options()
# options.add_argument("--start-maximized")
# driver = webdriver.Chrome(service=Service(), options=options)

article_list = {}

# try:
#     driver.get("https://www.bbc.com/innovation/technology")
#     time.sleep(5)  
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
grid_container = soup.find('div', class_="nevada-grid-6")
    
if grid_container:
        article_elements = grid_container.find_all('div', class_="edinburgh-card")  # Updated to get all article cards

        for article in article_elements:
            title_tag = article.find('h2', {'data-testid': 'card-headline'})
            description_tag = article.find('p', class_="card-description")

            title = title_tag.text.strip() if title_tag else 'No title'
            description = description_tag.text.strip() if description_tag else 'No description'

            article_list.append({'Title': title, 'Description': description})
#             article_list.append({'Title': title, 'Description': description})

#             print(f"Title: {article['Title']}")
#             print(f"Description: {article['Description']}")
#             print("-" * 40)

# except Exception as e:
#     print(f"An error occurred: {e}")

# finally:
#     driver.quit()

print(article_list)
print(articles_list)
print(dates_list)

driver.quit()



