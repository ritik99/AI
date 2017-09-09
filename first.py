

import webbrowser


def discern(data):
    if data == 'open facebook':
        call_fb()
    elif data == 'open gmail':
        call_gm()
    else:
        print("Sorry, couldn't understand")
        
def call_fb():
    url = 'http://facebook.com'
    
    # MacOS
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    
    # Windows
    # chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
    
    # Linux
    # chrome_path = '/usr/bin/google-chrome %s'
    
    webbrowser.get(chrome_path).open(url)
    
def call_gm():
    url = 'http:/gmail.com'
    
    # MacOS
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    
    # Windows
    # chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
    
    # Linux
    # chrome_path = '/usr/bin/google-chrome %s'
    
    webbrowser.get(chrome_path).open(url)
    
    
data = input()

discern(data)