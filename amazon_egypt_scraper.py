import requests
from bs4 import BeautifulSoup
from base_scraper import BaseScraper

class AmazonEgyptScraper(BaseScraper):
    BASE_URL = "https://www.amazon.eg"

    def search_products(self, keywords=None, category=None):
        products = []
        query = "+".join(keywords.split()) if keywords else ""
        url = f"{self.BASE_URL}/s?k={query}"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Amazon Egypt: Failed to fetch results.")
            return products
        soup = BeautifulSoup(response.text, "lxml")
        product_divs = soup.select("div[data-component-type='s-search-result']")
        for div in product_divs:
            title = div.select_one("h2 a span").get_text(strip=True)
            price = div.select_one(".a-price .a-offscreen").get_text(strip=True)
            link = div.select_one("h2 a")["href"]
            products.append({
                "name": title,
                "price": price,
                "url": f"{self.BASE_URL}{link}"
            })
        return products

    def extract_installment_info(self, product):
        product["installment_info"] = "No installment info available yet"
        return product
    