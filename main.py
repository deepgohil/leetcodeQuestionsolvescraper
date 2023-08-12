import requests
from bs4 import BeautifulSoup

url = "https://leetcode.com/deepgohil/"  

# Send an HTTP GET request
response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    target_div = soup.find("div", class_="text-[24px] font-medium text-label-1 dark:text-dark-label-1")

    if target_div:
        element_text = target_div.get_text()
        print("Scraped element text:", element_text)
    else:
        print("Desired div element not found.")
else:
    print("Failed to fetch the page:", response.status_code)
