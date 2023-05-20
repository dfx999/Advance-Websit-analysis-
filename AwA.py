import requests

from bs4 import BeautifulSoup

def analyze_website(url):

    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.content, 'html.parser')

        # Let's get wild and perform some hardcore website analysis

        # Unleash your creativity and extract any information you desire from the HTML

        # Brace yourself! This code will extract all the juicy email addresses from the webpage

        email_addresses = soup.find_all('a', href=lambda href: href and 'mailto:' in href)

        for email in email_addresses:

            print(email['href'][7:])

        # That's just the tip of the iceberg, my friend. You can do wonders with BeautifulSoup!

    else:

        print("Oops! The website couldn't be analyzed. Error code:", response.status_code)

# Buckle up and provide the URL of the website you want to analyze

website_url = 'https://www.example.com'

analyze_website(website_url)

