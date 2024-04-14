#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import hashlib
import os
import datetime


# Function to send alert
def send_alert(message):
    import requests
    url = 'https://api.pushover.net/1/messages.json'
    data = {
        'token': 'aapp_token',
        'user': 'user_token',
        'message': message
    }
    
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  # Raise an exception for 4XX and 5XX status codes
        print("Pushover notification sent successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Error sending pushover notification: {e}")

# Function to get the webpage content
def get_webpage_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        send_alert("Failed to retrieve webpage content")
        return None

# Function to calculate hash of content
def calculate_hash(content):
    return hashlib.md5(content).hexdigest()

# Function to check for changes in webpage content
def check_for_changes(url, hash_file):
    content = get_webpage_content(url)
    if content is not None:
        current_hash = calculate_hash(content)
        if os.path.exists(hash_file):
            with open(hash_file, 'r') as f:
                previous_hash = f.read()
            if current_hash != previous_hash:
                send_alert("Webpage content has changed at " + url)
                with open(hash_file, 'w') as f:
                    f.write(current_hash)
        else:
            with open(hash_file, 'w') as f:
                f.write(current_hash)
            send_alert("Initial hash saved.")
    else:
        send_alert("No content to check.")

# Main function
def main():
    url = "https://www.atsb.gov.au/publications/investigation_reports/2023/report/ao-2023-045"
    hash_file = "webpage_hash.txt"
    check_for_changes(url, hash_file)

    today = datetime.datetime.today().weekday()
    if today == 0:
        #print("VH-MSF Checker - Success Reminder")
        send_alert("VH-MSF Checker - Success Reminder")


if __name__ == "__main__":
    main()

