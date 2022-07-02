#!/usr/bin/python3
import urllib
import http.client as httplib
import os.path

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
pushover_api_app_token = "placeholder"
pushover_api_user_key = "placeholder"
pushover_api_youtubedl_token = "placeholder"

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.


    print(f'if something is wrong the runner is at /Users/corbin/Developer/pinger/main.py')
    filepath = "/tmp/startrektweeter.err"
    if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
        print(f'if something is wrong the runner is at /Users/corbin/Developer/pinger/main.py')  # Press ⌘F8 to toggle the breakpoint.
        conn = httplib.HTTPSConnection("api.pushover.net:443")
        conn.request("POST", "/1/messages.json",
                     urllib.parse.urlencode({
                         "token": pushover_api_app_token,
                         "user": pushover_api_user_key,
                         "message": "Star Trek Tweeter is producing error messages."
                     }), {"Content-type": "application/x-www-form-urlencoded"})
        conn.getresponse()
        
    filepathforyt = '/tmp/youtubenotifier.err'
    if os.path.exists(filepathforyt) and os.path.getsize(filepathforyt) > 0:
        print(f'if something is wrong the runner is at /Users/corbin/Developer/pinger/main.py')
        conn = httplib.HTTPSConnection("api.pushover.net:443")
        conn.request("POST", "/1/messages.json",
                     urllib.parse.urlencode({
                         "token": pushover_api_youtubedl_token,
                         "user": pushover_api_user_key,
                         "message": "Youtube Downloader is producing error messages."
                     }), {"Content-type": "application/x-www-form-urlencoded"})
        conn.getresponse()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
