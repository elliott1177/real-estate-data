from selenium import webdriver
#Keyboard functionality
from selenium.webdriver.common.keys import Keys
#Search
from selenium.webdriver.common.by import By
#Wait for webpage to load
from selenium.webdriver.support.ui import WebDriverWait
#Wait for expected conditions to happen
from selenium.webdriver.support import expected_conditions as EC

#Instantiate webdriver which is in my systems PATH
from selenium.webdriver import Chrome
driver = Chrome()

#We're going to search zillow
driver.get("https://www.zillow.com/")

#search-box-input is the search element for zillow.
search = driver.find_element_by_class_name("Input-sc-4ry0fw-0 jbZScm react-autosuggest__input")

#Input and enter scraping as a search term.
search.send_keys("forest lake")
search.send_keys(Keys.RETURN)

#The class name we wait for contains all the search results.
search_results = WebDriverWait(driver, 20).until(
EC.presence_of_element_located((By.CLASS_NAME, "list-card-info"))
) 

#((By.CLASS_NAME, "list-card-price"))
#Lists of posts
posts = search_results.find_elements_by_class_name("list-card-price")

for post in posts:
  #header = post.find_element_by_tag_name("span")
  print(post)

driver.quit()