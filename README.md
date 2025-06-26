📰 News Headline Scraper
This Python script fetches the HTML content from The Hindu website and extracts the page title along with all <h2> headlines. The extracted data is saved into a text file called news_headlines.txt.

📁 Files Included
news_scraper.py – The main Python script to fetch and parse news headlines.
news_headlines.txt – Output file containing the scraped headlines (auto-generated after running the script).

📌 Features
Fetches HTML content using the requests module.
Parses content using BeautifulSoup (from bs4).

Extracts:
Web page title
All <h2> tag text (typically headlines)
Saves the extracted data to a text file.

🚀 Requirements
Make sure you have the required libraries installed:
pip install requests beautifulsoup4

▶️ How to Run
Open a terminal or command prompt.
Navigate to the folder containing the script.
Run the script:
python news_scraper.py
