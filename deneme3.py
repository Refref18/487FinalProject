import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from webdriver_manager.chrome import ChromeDriverManager


# create webdriver object
driver = webdriver.Chrome()
# get geeksforgeeks.org
driver.get(
    "https://www.youtube.com/results?search_query=Large+scale+stock-flow+modeling+examples++")

def open_website_in_chrome(website_content):
    #print(website_content)
    # Create a temporary HTML file to store the website content
    with open('temp.html', 'w', encoding='utf-8') as file:
        file.write(website_content)

    # html_file = "D://2022-2023 2.dönem//487//487FinalProject//temp.html"
    # Get the path to the Chrome executable using ChromeDriverManager
    chrome_path = ChromeDriverManager().install()
    print(chrome_path)
    #chrome_path = "C://Program Files(x86)//Google//Chrome//Application//chrome.exe"
    webbrowser.register(
        'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.open('file://' + os.path.realpath("temp.html"))



website_content = driver.page_source

# Open the website content in a Chrome window
open_website_in_chrome(website_content)
