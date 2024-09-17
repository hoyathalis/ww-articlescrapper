from scraper import Scraper
from parser import Parser
from utils import save_data, log_message
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
import os

def scrape_and_parse(sub, page_num):
    SCRAPE_BASE_URL = sub["base"]
    SCRAPE_URL = SCRAPE_BASE_URL + sub["url"] + str(page_num)
    scraper = Scraper(SCRAPE_URL)
    raw_data = scraper.scrape()
    parser = Parser(SCRAPE_BASE_URL, raw_data, sub['tag'])
    
    if "bankrate" in SCRAPE_BASE_URL:
        parsed_data = parser.bankrate_parse()

    if "wsj" in SCRAPE_BASE_URL:
        parsed_data = parser.wsj_parse()  
    
    if "experian" in SCRAPE_BASE_URL:
        parsed_data = parser.experian_parse()

    path = f"data/processed/{sub['tag']}.csv"
    save_data(parsed_data, path)
    return f"Completed scraping and parsing for page {page_num} of {sub['tag']}"

def main():
    SUB_URL = [
        # {"base":"https://www.bankrate.com/", "url": "banking/?feed=banking-stories&page=", "pages": 127, "tag": "banking"},
        # {"base":"https://www.bankrate.com/", "url": "mortgages/?feed=mortgage-stories&page=", "pages": 77, "tag": "mortgages"},
        # {"base":"https://www.bankrate.com/", "url": "investing/?page=", "pages": 50,"tag": "investing"},
        # {"base":"https://www.bankrate.com/", "url": "credit-cards/?page=", "pages": 180,"tag": "credit-cards"},
        # {"base":"https://www.bankrate.com/", "url": "loans/?page=", "pages": 32,"tag": "loans"},
        # {"base":"https://www.bankrate.com/", "url": "home-equity/?feed=home-equity-stories&page=", "pages": 11, "tag": "home-equity"},
        # {"base":"https://www.bankrate.com/", "url": "insurance/?feed=insurance-stories&page=", "pages": 108, "tag": "insurance"},

        {"base":"https://www.experian.com/blogs/ask-experian/page/", "url": "", "pages": 318, "tag": "finance"},
       
    ]

    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    log_message("Starting the web scraping project...")

    for sub in SUB_URL:
        # Create a list of page numbers to scrape
        pages = range(1, sub["pages"] + 1)
        
        # Using ThreadPoolExecutor to scrape pages concurrently
        with ThreadPoolExecutor(max_workers=10) as executor:
            # Submit tasks to the executor
            futures = [executor.submit(scrape_and_parse, sub, page) for page in pages]
            
            # Process the results as they are completed
            for future in as_completed(futures):
                try:
                    result = future.result()
                    log_message(result)
                except Exception as e:
                    log_message(f"An error occurred: {e}")

    log_message("Web scraping completed!")

if __name__ == "__main__":
    main()
