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
from selenium.webdriver import Edge
driver = Edge()

#We're going to search reddit
driver.get("https://www.reddit.com/")

#Q is the search element for reddit.
search = driver.find_element_by_name("q")

#Input and enter scraping as a search term.
search.send_keys("scraping")
search.send_keys(Keys.RETURN)

#The class name we wait for contains all the search results.
search_results = WebDriverWait(driver, 20).until(
EC.presence_of_element_located((By.CLASS_NAME, "rpBJOHq2PR60pnwJlUyP0"))
) 

#Lists of posts
posts = search_results.find_elements_by_css_selector("h3._eYtD2XCVieq6emjKBH3m")

for post in posts:
  header = post.find_element_by_tag_name("span")
  print(header.text)

driver.quit()