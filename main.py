from amazon_egypt_scraper import AmazonEgyptScraper
from jumia_scraper import JumiaScraper

SCRAPERS = [AmazonEgyptScraper(), JumiaScraper()]

def scrape_all_stores(keywords=None, category=None):
    all_products = []
    for scraper in SCRAPERS:
        print(f"Scraping with {scraper.__class__.__name__}...")
        try:
            products = scraper.search_products(keywords, category)
            for product in products:
                product = scraper.extract_installment_info(product)
                all_products.append(product)
        except Exception as e:
            print(f"Error while scraping with {scraper.__class__.__name__}: {e}")
    return all_products

if __name__ == "__main__":
    keywords = input("Enter keywords (e.g., iPhone, TV): ").strip()
    category = input("Enter category (optional): ").strip()
    products = scrape_all_stores(keywords, category)
    for product in products:
        print(f"{product['name']} - {product['price']} - {product['url']}")
    