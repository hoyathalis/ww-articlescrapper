import requests
from utils import log_message

class Scraper:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        log_message(f"Scraping data from {self.url}")
        
        try:
            response = requests.get(self.url)
            response.raise_for_status() 
            return response.text
        except requests.exceptions.RequestException as e:
            log_message(f"Error during scraping: {e}")
            return None
        
    def bankrate_scrape(self):
        log_message(f"Scraping banrate data from {self.url}")
        try:
            response = requests.get(self.url)
            response.raise_for_status() 
            return response.text
        except requests.exceptions.RequestException as e:
            log_message(f"Error during scraping: {e}")
            return None