import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from webdriver_manager.chrome import ChromeDriverManager
import webbrowser
import socket
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import tkinter as tk
from tkinter import ttk
import socket
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tkhtmlview import HTMLLabel

# create webdriver object
#driver = webdriver.Chrome()
options = Options()
# Use an existing Chrome instance
options.add_argument("--remote-debugging-port=9222")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# get geeksforgeeks.org
website_url = driver.current_url
print(website_url)

prev = driver.current_url

def open_website_in_chrome(website_content):
   
    """if prev==driver.current_url:
        continue
    prev=driver.current_url"""
    print(website_content)
    # Create a temporary HTML file to store the website content
    with open('temp.html', 'w', encoding='utf-8') as file:
        file.write(website_content)

    # html_file = "D://2022-2023 2.dönem//487//487FinalProject//temp.html"
    # Get the path to the Chrome executable using ChromeDriverManager
    #chrome_path = ChromeDriverManager().install()
        
    chrome_path = "C://Program Files(x86)//Google//Chrome//Application//chrome.exe"
    print(chrome_path)
    webbrowser.register(
        'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.open('file://' + os.path.realpath("temp.html"))


while True:
    website_content = driver.page_source

    # Open the website content in a Chrome window
    open_website_in_chrome(website_content)
