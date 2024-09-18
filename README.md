# Web Scraper and Parser

This project is a Python-based web scraper designed to extract and process data from financial websites like **Bankrate**, **Nerdwallet**, and **Experian**. The script uses multi-threading to scrape multiple pages concurrently, improving efficiency and speed. It also parses the raw HTML data into structured CSV files for further analysis.

## Key Features

- **Concurrent Scraping**: Utilizes `ThreadPoolExecutor` for scraping multiple pages at the same time, speeding up the process.
- **Custom Parsing**: Parses raw HTML data from different websites using customized parsing methods based on the site's structure.
- **Data Export**: Saves the processed data into CSV files for easy access and analysis.
- **Error Handling**: Logs errors and successful scrapes, ensuring smooth execution.

## Project Structure

```bash
.
├── scraper.py        # Contains the Scraper class for handling HTTP requests
├── parser.py         # Contains the Parser class to process raw HTML data
├── utils.py          # Utility functions like logging and saving data
├── main.py           # The main script that executes the scraping and parsing
└── data/
    └── processed/    # Directory where processed CSV data is saved
## How to Use

### Install dependencies
Ensure you have all the required Python libraries:

```bash
pip install requests tqdm

### Run the scraper
Execute the main script to start scraping and parsing:

```bash
python main.py

### Customize the scraping targets
Modify the SUB_URL list in main.py to scrape different pages from the supported websites.
