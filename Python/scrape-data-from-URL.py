# two ways of parsing html from URL
import pandas as pd

# method 1: requests + BeautifulSoup
import requests
from bs4 import BeautifulSoup

headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
r = requests.get('https://github.com/f/awesome-chatgpt-prompts/blob/main/prompts.csv', headers = headers)
c = r.content
soup = BeautifulSoup(c, 'html.parser')
html_1 = soup.prettify()


# method 2: selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# parse html without opening Chrome browser
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options = options)

driver.get('https://github.com/f/awesome-chatgpt-prompts/blob/main/prompts.csv')
html_2 = driver.page_source


dfs_1 = pd.read_html(html_1)
print(len(dfs_1))
df_1 = dfs_1[0]
print(df_1.shape)
print(df_1.columns)

dfs_2 = pd.read_html(html_2)
print(len(dfs_2))
df_2 = dfs_2[0]
print(df_2.shape)
print(df_2.columns)
