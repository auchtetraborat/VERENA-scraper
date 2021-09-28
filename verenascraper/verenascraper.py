from .verenadownloader import VerenaDownloader
from .verenaextractor import VerenaExtractor


class VerenaScraper:
    """
    Downloads and extracts the current job listings from the VERENA portal.
    """

    def get(self):
        """
        Downloads and extracts the current job listings from the VERENA portal.

        Example of the json format can be found at ./example.json
        """
        result = []
        scraped_pages = VerenaDownloader().scrape()
        for idx, page in enumerate(scraped_pages):
            extract = VerenaExtractor(page).extract()
            result = result + extract
        return result


if __name__ == "__main__":
    vs = VerenaScraper()
    res = vs.get()
    print(res)
