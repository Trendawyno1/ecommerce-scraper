import abc

class BaseScraper(abc.ABC):
    @abc.abstractmethod
    def search_products(self, keywords=None, category=None):
        pass

    @abc.abstractmethod
    def extract_installment_info(self, product):
        pass
    