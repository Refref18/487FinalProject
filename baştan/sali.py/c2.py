import socket
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Create webdriver object
options = Options()
# Use an existing Chrome instance
options.add_argument("--remote-debugging-port=9222")
driver = webdriver.Chrome(options=options)

# Create a TCP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server (Computer 1)
server_address = ('CLIENT_1_IP_ADDRESS', CLIENT_1_PORT)
client_socket.connect(server_address)

# Function to send website content to the client


def send_website_content(website_content):
    client_socket.sendall(website_content.encode())

# Function to receive the URL from the client


def receive_url():
    url = ''
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        url += data.decode()
    return url

# Function to retrieve the page source from the URL


def get_page_source(url):
    driver.get(url)
    return driver.page_source


# Example usage
while True:
    url = receive_url()
    website_content = get_page_source(url)
    send_website_content(website_content)

# Close the client socket
client_socket.close()
