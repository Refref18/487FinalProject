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
driver = webdriver.Chrome()
# get geeksforgeeks.org
driver.get(
    "https://www.youtube.com/results?search_query=Large+scale+stock-flow+modeling+examples++")


def decrypt_response(response):
    # Implement your decryption logic
    # Example: Convert JSON string to response object
    decrypted_response = json.loads(response)
    return decrypted_response


def open_website_in_chrome(website_content):
    # Create a temporary HTML file to store the website content
    with open('temp.html', 'w', encoding='utf-8') as file:
        file.write(website_content)
    
    #html_file = "D://2022-2023 2.dönem//487//487FinalProject//temp.html"
    chrome_path = "C://Program Files(x86)//Google//Chrome//Application//chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.open('file://' + os.path.realpath("temp.html"))


    # Open the temporary HTML file in Chrome
    # Replace with the actual path to Chrome
    """chrome_path = "C://Program Files(x86)//Google//Chrome//Application//chrome.exe"
    webbrowser.register(
        'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open('file://' + 'temp.html')"""


website_content = driver.page_source

# Open the website content in a Chrome window
open_website_in_chrome(website_content)


