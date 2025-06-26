import requests
from bs4 import BeautifulSoup

def fetch_web_content(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except requests.RequestException as err:
        print("HTTP error occurred:", err)
        return None

def extract_headlines(html):
    soup = BeautifulSoup(html, 'html.parser')
    title_text = soup.title.string.strip() if soup.title else "No title found"
    h2_list = [tag.get_text(strip=True) for tag in soup.select('h2')]
    return title_text, h2_list

def save_to_file(title, h2s, filename="news_headlines.txt"):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("Page Title:\n" + title + "\n\n")
            f.write("H2 Headlines:\n")
            for item in h2s:
                f.write(item + "\n")
        print(f"Data successfully written to {filename}")
    except Exception as file_err:
        print("Error writing to file:", file_err)


if __name__ == "__main__":
    target_url = "https://www.thehindu.com/"
    html_data = fetch_web_content(target_url)

    if html_data:
        page_title, h2_tags = extract_headlines(html_data)
        save_to_file(page_title, h2_tags, filename="news_headlines.txt")
