with open('temp.html', 'w', encoding='utf-8') as file:
        file.write(content)
    webbrowser.open('file://' + os.path.realpath("temp.html"))