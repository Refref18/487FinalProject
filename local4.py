import socket
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tkinter as tk


def encrypt_request(request):
    # Implement your encryption logic
    encrypted_request = json.dumps(request)  # Example: Convert request to JSON string
    return encrypted_request



def decrypt_response(response):
    # Implement your decryption logic
    decrypted_response = json.loads(response)  # Example: Convert JSON string to response object
    return decrypted_response



def open_website_in_chrome(website_content):
    # Create a Tkinter window
    window = tk.Tk()

    # Create a Tkinter text widget to display the website content
    text_widget = tk.Text(window)
    text_widget.pack()

    # Insert the website content into the text widget
    text_widget.insert(tk.END, website_content)

    # Run the Tkinter event loop
    window.mainloop()


# Connect to the proxy server
proxy_address = ('133.18.234.13', 80)  # Replace with your actual proxy server address and port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(proxy_address)

# Initialize the WebDriver
options = Options()
# Add any necessary options for Chrome
driver = webdriver.Chrome(options=options)

# Start the main loop
while True:
    # Retrieve the website URL from the active Chrome browser
    website_url = driver.current_url

    # Create the request dictionary
    request = {
        "myIP": "...",
        "website": website_url
    }

    website_url = driver.current_url  #şuan olduğumuz yeri çekiyor search'e yazdığımızı çekmeli (google' a yollamak)
    print(website_url)

    # Encrypt the request

    #if website_url eskisinden farklıysa

    encrypted_request = encrypt_request(request)
    print(encrypted_request)
    """website_url = driver.current_url
    i=0
    while i<30000000:
        i+=1
    print(i)
    print(driver.current_url)"""

    # Send the encrypted request to the proxy server
    sock.send(encrypted_request.encode())

    # Receive the encrypted response from the proxy server
    encrypted_response = sock.recv(4096).decode() #gelene kadar beklemeli birden fazla thread 

    # Decrypt the response
    decrypted_response = decrypt_response(encrypted_response)

    # Process the decrypted response
    # ...

    # Open the website in Chrome browser on the local machine
    open_website_in_chrome(decrypted_response['website'])  # html dönmeli THINKER 

# Close the TCP connection
sock.close()
