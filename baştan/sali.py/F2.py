import socket
from urllib.parse import urlparse, urlencode
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Create webdriver object
options = Options()
# Use an existing Chrome instance
options.add_argument("--remote-debugging-port=9222")
driver = webdriver.Chrome(options=options)

# Create a TCP server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server socket to a specific address and port
server_address = ('SERVER_IP_ADDRESS', SERVER_PORT)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

# Function to send website content to the client


def send_website_content(content, client_socket):
    client_socket.sendall(content.encode())

# Function to receive the URL or search query from the client


def receive_input(client_socket):
    data = ''
    while True:
        chunk = client_socket.recv(1024)
        if not chunk:
            break
        data += chunk.decode()
    return data.strip()

# Function to retrieve the page source from the URL or perform a search query


def get_page_source(input_data):
    parsed_url = urlparse(input_data)
    if parsed_url.scheme and parsed_url.netloc:
        driver.get(input_data)  # Complete URL, navigate to the page
    else:
        search_url = 'https://www.google.com/search?' + \
            urlencode({'q': input_data})
        driver.get(search_url)  # Search query, perform a search on Google
    return driver.page_source


# Accept incoming connections
print('Waiting for Client 1 to connect...')
client_socket, client_address = server_socket.accept()
print('Client 1 connected:', client_address)

# Example usage
while True:
    input_data = receive_input(client_socket)
    website_content = get_page_source(input_data)
    send_website_content(website_content, client_socket)

# Close the client socket
client_socket.close()

# Close the server socket
server_socket.close()
