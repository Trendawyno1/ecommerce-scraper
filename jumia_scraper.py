import requests
from bs4 import BeautifulSoup
from base_scraper import BaseScraper

class JumiaScraper(BaseScraper):
    BASE_URL = "https://www.jumia.com.eg"

    def search_products(self, keywords=None, category=None):
        products = []
        query = "+".join(keywords.split()) if keywords else ""
        url = f"{self.BASE_URL}/catalog/?q={query}"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Jumia: Failed to fetch results.")
            return products
        soup = BeautifulSoup(response.text, "lxml")
        product_divs = soup.select("article.prd")
        for div in product_divs:
            title = div.select_one("h3.name").get_text(strip=True)
            price = div.select_one("div.prc").get_text(strip=True)
            link = div.select_one("a.core")["href"]
            products.append({
                "name": title,
                "price": price,
                "url": f"{self.BASE_URL}{link}"
            })
        return products

    def extract_installment_info(self, product):
        product["installment_info"] = "Installments available through partner banks."
        return product
    