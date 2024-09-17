# src/parser.py
from bs4 import BeautifulSoup
from utils import log_message
from tqdm import tqdm
import re

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
                    'link': self.baseurl+link,
                    'description': description,
                    'date': date
                })
            return data
    def wsj_parse(self):
        log_message("Parsing the scraped data from wsj...")
        
        if self.raw_data is None:
            log_message("No data to parse.")
            return {}

        soup = BeautifulSoup(self.raw_data, 'html.parser')

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
    
    def experian_parse(self):
        log_message("Parsing the scraped data from experian...")

        if self.raw_data is None:
            log_message("No data to parse.")
            return {}

        soup = BeautifulSoup(self.raw_data, 'html.parser')

        # Find the container with the id artBlk
        articles = soup.select('#artBlk .post.flx.flx-yc.flx-jc-xc')

        data = []

        for article in articles:
            link_tag = article.find('a')
            if not link_tag:
                continue
            
            # Extract article details
            link = link_tag['href']
            title = link_tag.find('h5').get_text(strip=True)
            description_tag = link_tag.find('span', class_='hidden-xs hidden-sm')
            description = description_tag.get_text(strip=True) if description_tag else ""
            date_tag = link_tag.find('p', class_='date')

            date_tag = link_tag.find('p', class_='date')
            if date_tag:
                # Use regex to extract the date portion before "•"
                date = re.search(r"^(.*?)(?:\s+•|$)", date_tag.get_text(strip=True)).group(1)
            else:
                date = ""
            # Append the extracted information to the data list
            data.append({
                'title': title,
                'tag': self.tag,
                'link': link,
                'description': description,
                'date': date
            })

        return data

            