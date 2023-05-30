from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from urllib.parse import urlparse, urlencode, parse_qs
# Create webdriver object
options = Options()
# Use an existing Chrome instance
options.add_argument("--remote-debugging-port=9222")
driver = webdriver.Chrome(options=options)

# Function to open website content in the existing Chrome window


def receive_url(client_socket):
    url = ''
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        url += data.decode()
    return url


def get_page_source(input_data):
    parsed_url = urlparse(input_data)
    if parsed_url.scheme and parsed_url.netloc:
        driver.get(input_data)  # Complete URL, navigate to the page
    else:
        search_url = 'https://www.google.com/search?' + \
            urlencode({'q': input_data})
        driver.get(search_url)  # Search query, perform a search on Google
    return driver.page_source



def open_website_in_chrome(website_content):
    # Create a temporary HTML file to store the website content
    with open('temp.html', 'w', encoding='utf-8') as file:
        file.write(website_content)

    # Open the HTML file in the existing Chrome window
    driver.get('file://' + os.path.realpath("temp.html"))


prev = driver.current_url
# Example usage
"""while True:
    if prev == driver.current_url:
        continue
    prev = driver.current_url
    website_content = driver.page_source
    open_website_in_chrome(website_content)"""

while True:
    current_url = input("Enter the URL: ")
    website_content=get_page_source(current_url)
    open_website_in_chrome(website_content)
        
