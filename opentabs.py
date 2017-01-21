import requests
import webbrowser

# Create a txt file named 'search terms' and put the desired search terms each on a line of its own.

with open('search terms.txt') as f:
    content = f.readlines()
    for i in range(len(content)):
        search_term = content[i]
        var = requests.get(r'http://www.google.com/search?q=' + search_term + "athletic staff directory" + '&btnI')
        webbrowser.open(var.url)