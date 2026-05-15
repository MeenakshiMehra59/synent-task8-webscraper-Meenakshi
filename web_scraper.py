import requests
from bs4 import BeautifulSoup
import csv

def web_scraper():
    print("--- Synent Web Scraper (News Headlines) ---")
    
    # We will scrape a simple, public site like 'Quotes to Scrape' or a news site
    url = "http://quotes.toscrape.com/"
    
    try:
        response = requests.get(url)
        # Check if the website is accessible
        if response.status_status == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Finding all quotes and authors on the page
            quotes = soup.find_all('span', class_='text')
            authors = soup.find_all('small', class_='author')
            
            # Store in a CSV file as required by the internship
            with open('scraped_quotes.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Quote", "Author"])
                
                for i in range(len(quotes)):
                    writer.writerow([quotes[i].get_text(), authors[i].get_text()])
            
            print("Successfully scraped data and saved to 'scraped_quotes.csv'!")
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    web_scraper()