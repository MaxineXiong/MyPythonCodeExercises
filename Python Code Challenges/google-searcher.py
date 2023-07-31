# Create a script that let the user type in a search term and then the program opens the browser and searches the term on Google.
from selenium import webdriver
import time


query = input('What would you like to search? Enter it here: ')

driver = webdriver.Chrome()
driver.get('https://www.google.com/search?q=' + query.replace(' ', '+'))

while True:
    close = input('Type YES to close this session: ')
    if close == 'YES':
        break
