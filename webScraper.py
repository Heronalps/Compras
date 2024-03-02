import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.amazon.com/Apple-MacBook-Laptop-12%E2%80%91core-18%E2%80%91core/dp/B0CM5BL45N/ref=sr_1_3?crid=MXUESMRA7JTB&dib=eyJ2IjoiMSJ9.NP_ReB7pv6X-XRWQg0E9Ic7JabYZBOTKBnbKJYpOo5sCFYViV3WoHKtbMBrewU6dQH6ENpAv5mZEJxCVZVQ8qewvADCf-7kzWO9gBDgqsY-USXrwQISdgqm6C9-XMjlvobLMaTWv6bFhw_v6VM_ZnRKdplUovZFKFgUb-11wfGvSREVmcYYAMZFGOh6dqkr_CaljG7pjEXY6lTHB3IMgZqipUPujLFTFpF6ydyxilwQ.0-7MRIO6hssBbV4qW-pPRsZG5fJfKziYwBqN3kQ1ueA&dib_tag=se&keywords=apple%2B2023%2Bmacbook%2Bpro&qid=1709412361&sprefix=apple%2B2023%2Bmacbook%2Bpro%2Caps%2C165&sr=8-3&th=1'

# send response to webpage
response = requests.get(url)
response.raise_for_status()

# parsing the HTML page
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting data using BeautifulSoup
product_title = soup.select_one('#productTitle').text.strip()
product_description = soup.select_one('#feature-bullets').text.strip()
product_specs = soup.select_one('#btfContent31_feature_div').text.replace('\n', ' ')
reviews_elements = soup.select('.review-text-content')
titles_elements = soup.select('.review-title')

# Extract titles and reviews
reviews_data = [{
    "product title": product_title,
    "product description": product_description,
    "product specifications": product_specs,
    "review title": title_element.text.strip(),
    "review contents": review_element.text.strip()
} for title_element, review_element in zip(titles_elements, reviews_elements)]

# Export to JSON
with open('reviews.json', 'w', encoding='utf-8') as f:
    json.dump(reviews_data, f, ensure_ascii=False, indent=4)

print("Data exported to reviews.json successfully.")