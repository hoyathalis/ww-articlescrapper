# src/parser.py
from bs4 import BeautifulSoup
from utils import log_message
from tqdm import tqdm
class Parser:
    def __init__(self, baseurl, raw_data, tag):
        self.raw_data = raw_data
        self.tag=tag
        self.baseurl=baseurl

    def parse(self):
        log_message("Generic Parsing the scraped data...")
        
        if self.raw_data is None:
            log_message("No data to parse.")
            return {}
        return ""
    
    def bankrate_parse(self):
        log_message("Parsing the scraped data from bankrate...")
        
        if self.raw_data is None:
            log_message("No data to parse.")
            return {}

        soup = BeautifulSoup(self.raw_data, 'html.parser')

        if (self.tag in ["banking","mortgages","home-equity","insurance"]):
            articles = soup.select('#latest-articles .t-card__content')

            data = []

            for article in articles:
                title = article.find('h3', class_='t-card__title').get_text(strip=True)
                link = article.find('a', class_='t-card__link')['href']
                description = article.find('div', class_='t-card__body').get_text(strip=True)
                date = article.find('div', class_='t-byline__meta').get_text(strip=True)
                
                # Append the extracted information to the data list
                data.append({
                    'title': title,
                    'tag': self.tag,
                    'link': self.baseurl+link,
                    'description': description,
                    'date': date
                })

            return data
        else:
            articles = soup.select('#latest-articles li .Card')
            # List to store the extracted data
            data = []

            # Loop through each article and extract relevant information
            for article in articles:
                title = article.find('h2', class_='type-heading-four').get_text(strip=True)
                link = article.find('a', class_='Card-link')['href']
                description = article.find('p', class_='type-body-one').get_text(strip=True)
                date = article.find('span', class_='type-body-two').get_text(strip=True)
                
                # Append the extracted information to the data list
                data.append({
                    'title': title,
                    'tag': self.tag,
                    'link': link,
                    'description': description,
                    'date': date
                })
            return data