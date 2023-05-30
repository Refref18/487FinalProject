def update_website_content(url):
    send_url(url)
    website_content = receive_website_content()
    display_website_content(website_content)