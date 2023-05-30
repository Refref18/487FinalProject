import socket
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os 

# Create webdriver object
options = Options()
# Use an existing Chrome instance
options.add_argument("--remote-debugging-port=9222")
driver = webdriver.Chrome(options=options)

# Create a TCP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server (Computer 2)
server_address = ('SERVER_IP_ADDRESS', SERVER_PORT)
client_socket.connect(server_address)

# Function to send the URL to the server


def send_url(url):
    client_socket.sendall(url.encode())

# Function to receive website content from the server


def receive_website_content():
    website_content = ''
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        website_content += data.decode()
    return website_content

# Function to open the website content in the default web browser


def open_website_in_browser(content):
    with open('temp.html', 'w', encoding='utf-8') as file:
        file.write(content)
    #webbrowser.open('file://' + os.path.realpath("temp.html"))
    driver.get('file://' + os.path.realpath("temp.html"))

# Function to update the website content in the browser


def update_website_content(url):
    send_url(url)
    website_content = receive_website_content()
    open_website_in_browser(website_content)


# Example usage
prev_url = ""
while True:
    current_url = input("Enter the URL: ") #bu kısım URL 'i burdan yerine direk aratmadan alsa 
    if current_url != prev_url:
        update_website_content(current_url)
        prev_url = current_url

# Close the client socket
client_socket.close()
