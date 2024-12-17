from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import json


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)

url = 'https://www.inmotionhosting.com/'

try:
    driver.get(url)
    accept_cookies = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler')))
    
    accept_cookies.click() # Click on the accept all cookies link
    print('Successfully clicked on the accept cookies button')

    time.sleep(2) # Wait for the results

    #Get to the shared hosting page to compare results

    shared_hosting = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Compare Plans')))
    
    shared_hosting.click() # Click on the compare plans button link
    print('Successfully clicked on the Compare Plans link')

    time.sleep(2) # Wait for the results

    #Now that we are in the comparison plans webpage, let's scrape the plan names, features and pricing.
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    container = soup.find('div', class_='imh-rostrum-container')
    list_of_plans = soup.find
    plans = [] 
    for _ in container.find_all('div', class_='imh-rostrum-card'):
        plan = _.find('h3')#, class_='hr imh-rostrum-card-title')
        plan = plan.text
        
        price = _.find('div', class_='imh-rostrum-starting-at-price-discounted')
        price = price.text

        features = [] # we will create a list inside the for loop to store all the features of each plan
        feature_list = _.find_all('li', class_='fa fa-imh-arrow-right tooltips-rostrum')
        for feature in feature_list:
            features.append(feature.text)


        plans.append({
            'plan': plan,
            'price': price,
            'features': features   
        })

finally:
    driver.quit() # Close the browser

host_plan = json.dumps(plans, indent=2)

print(host_plan)
