
import tkinter as tk
from tkinter import ttk
import socket
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tkhtmlview import HTMLLabel
# create webdriver object
driver = webdriver.Chrome()
driver2 = webdriver.Firefox()
# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
 


import tkinter as tk
from tkinter import ttk
import socket
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tkhtmlview import HTMLLabel
from bs4 import BeautifulSoup

def decrypt_response(response):
    # Implement your decryption logic
    decrypted_response = json.loads(response)  # Example: Convert JSON string to response object
    return decrypted_response

def clean_html_content(html_content):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove unsupported or problematic CSS styles
    for tag in soup.find_all():
        if tag.has_attr('style'):
            del tag['style']

    # Return the cleaned HTML content
    return str(soup)

def open_website_in_gui(website_content):
    # Clean up the HTML content
    cleaned_content = clean_html_content(website_content)

    # Create a Tkinter window
    window = tk.Tk()

    # Create an HTML label widget to display the website content
    html_label = HTMLLabel(window, html=cleaned_content)
    html_label.pack(expand=True, fill='both')

    # Run the Tkinter event loop
    window.mainloop()

# Extract the website content from the decrypted response
website_content =  driver.page_source


# Open the website content in a GUI window
open_website_in_gui(website_content)

# Close the TCP connection
sock.close()

