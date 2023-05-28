from selenium import webdriver
import webbrowser
import os
html_file = "D://2022-2023 2.dönem//487//487FinalProject//temp.html"

chrome_path = "C://Program Files(x86)//Google//Chrome//Application//chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.open('file://' + os.path.realpath("temp.html"))

