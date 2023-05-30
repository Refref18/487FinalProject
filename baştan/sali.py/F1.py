import socket
from flask import Flask, render_template, request
from urllib.parse import urlparse
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

# Create Flask web application
app = Flask(__name__)

# Route for the homepage


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        if is_valid_url(url):
            update_website_content(url)
        else:
            return render_template('index.html', error=True)
    return render_template('index.html', error=False)

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

# Function to update the website content


def update_website_content(url):
    send_url(url)
    website_content = receive_website_content()
    open_website_in_browser(website_content)

# Function to open the website content in the browser


def open_website_in_browser(content):
    with open('temp.html', 'w', encoding='utf-8') as file:
        file.write(content)
    driver.get('file://' + os.path.realpath("temp.html"))

# Function to check if the URL is valid


def is_valid_url(url):
    parsed_url = urlparse(url)
    return parsed_url.scheme and parsed_url.netloc


# Example usage
if __name__ == '__main__':
    app.run()

# Close the client socket
client_socket.close()
