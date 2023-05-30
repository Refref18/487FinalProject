import socket
import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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

# Function to display the website content in the GUI
def display_website_content(content):
    text.delete('1.0', tk.END)  # Clear the previous content
    text.insert(tk.END, content)

# Function to update the website content in the GUI
def update_website_content(url):
    send_url(url)
    website_content = receive_website_content()
    display_website_content(website_content)

# GUI setup
root = tk.Tk()
root.title("Website Viewer")

frame = ttk.Frame(root, padding="10")
frame.grid(column=0, row=0, sticky="nsew")

label = ttk.Label(frame, text="Enter URL:")
label.grid(column=0, row=0)

url_entry = ttk.Entry(frame, width=50)
url_entry.grid(column=1, row=0)

button = ttk.Button(frame, text="Go", command=lambda: update_website_content(url_entry.get()))
button.grid(column=2, row=0)

text = tk.Text(frame, height=20, width=80)
text.grid(column=0, row=1, columnspan=3)

# Example usage
prev_url = ""
while True:
    current_url = url_entry.get()
    if current_url != prev_url:
        update_website_content(current_url)
        prev_url = current_url
    root.update()

# Close the client socket
client_socket.close()
